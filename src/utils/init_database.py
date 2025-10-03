import json
import psycopg2.errors

from dao.db_connection import DBConnection

"""
with open("../data/ingredients.json", "r") as f:
    ingredients = json.load(f)
    with DBConnection().connection as connection:
        for ing in ingredients:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO ingredients(id_ingredient,ingredient_name,ingredient_type,alcoholic) VALUES"
                    "(%(id_ingredient)s, %(ingredient_name)s, %(ingredient_type)s, %(alcoholic)s)           "
                    "RETURNING id_ingredient;                                                               ",
                    {
                        "id_ingredient": ing["idIngredient"],
                        "ingredient_name": ing["strIngredient"],
                        "ingredient_type": ing["strType"],
                        "alcoholic": ing["strAlcohol"] == "Yes",
                    },
                )
                res = cursor.fetchone()
            if res is None or res['id_ingredient] != int(ing["idIngredient"]):
                print(f"Ingredient n°{ing['idIngredient']} not created! res = {res}")
"""

with open("../data/cocktails.json", "r") as f:
    cocktails = json.load(f)
    print(len(cocktails))
    with DBConnection().connection as connection:
        for cocktail in cocktails:
            with connection.cursor() as cursor:
                try:
                    cursor.execute(
                        "INSERT INTO cocktails(id_recipe,recipe_name,category,alcoholic,glass_type,instruction,cocktail_pic_url) VALUES"
                        "(%(id_recipe)s, %(recipe_name)s, %(category)s, %(alcoholic)s, %(glass_type)s, %(instruction)s, %(pic_url)s)"
                        "RETURNING id_recipe;                                                               ",
                        {
                            "id_recipe": cocktail["idDrink"],
                            "recipe_name": cocktail["strDrink"],
                            "category": cocktail["strCategory"],
                            "alcoholic": cocktail["strAlcoholic"] == "Yes",
                            "glass_type": cocktail["strGlass"],
                            "instruction": cocktail["strInstructions"],
                            "pic_url": cocktail["strDrinkThumb"]
                        }
                    )
                except psycopg2.Error as e:
                    connection.rollback()
                    print(e)
                    continue
                res = cursor.fetchone()
            if res is None or res['id_recipe'] != int(cocktail["idDrink"]):
                print(f"Cocktail n°{cocktail['idDrink']} not created! res = {res}")

    with DBConnection().connection as connection:
        for cocktail in cocktails:
            for i in range(1,16):
                ingredient_name = cocktail[f'strIngredient{i}']
                mesure = cocktail[f'strMeasure{i}']
                if mesure is None:
                    mesure = ''
                if ingredient_name is None:
                    break
                with connection.cursor() as cursor:
                    try:
                        cursor.execute(
                            "SELECT id_ingredient FROM ingredients WHERE ingredient_name = %(name)s",
                            {
                                'name': ingredient_name
                            }
                        )
                    except psycopg2.Error as e:
                        connection.rollback()
                        print(e)
                        print(f'aaahhah {ingredient_name}')
                        continue
                    res = cursor.fetchone()
                    if res is None:
                        print(f"{ingredient_name}'s id not found")
                        continue
                    id_ingredient = int(res['id_ingredient'])

                with connection.cursor() as cursor:
                    try:
                        cursor.execute(
                            "INSERT INTO composition(id_recipe, id_ingredient, quantity)"
                            "VALUES(%(id_recipe)s, %(id_ingredient)s, %(quantity)s)",
                            {
                                'id_recipe': int(cocktail['idDrink']),
                                'id_ingredient': id_ingredient,
                                'quantity': mesure
                            }
                        )
                    except psycopg2.errors.UniqueViolation as e:
                        connection.rollback()
                        continue
                    except psycopg2.Error as e:
                        connection.rollback()
                        print(e)
                        continue