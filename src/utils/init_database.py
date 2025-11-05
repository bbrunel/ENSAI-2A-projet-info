import json

import psycopg2.errors

from dao.db_connection import DBConnection
from utils.diverse import unaccent

## Supression des tables
with DBConnection().connection as connection:
    with connection.cursor() as cursor:
        cursor.execute("DROP TABLE IF EXISTS composition;")
        cursor.execute("DROP TABLE IF EXISTS have;")
        cursor.execute("DROP TABLE IF EXISTS favorites;")
        cursor.execute("DROP TABLE IF EXISTS cocktails;")
        cursor.execute("DROP TABLE IF EXISTS ingredients;")
        cursor.execute("DROP TABLE IF EXISTS users;")

## Création des tables
with open("../data/init.sql", "r") as f:
    init_script = f.read()
    with DBConnection().connection as connection:
        with connection.cursor() as cursor:
            for statement in init_script.split(";"):
                stmt = statement.replace('\n','')
                stmt = stmt.replace('\t','')
                if stmt:
                    cursor.execute(stmt + ';')
 
## Remplissage des tables avec les données brutes de thecocktaildb.com
with open("../data/ingredients.json", "r") as f:
    ingredients = json.load(f)
    with DBConnection().connection as connection:
        for ing in ingredients:
            with connection.cursor() as cursor:
                abv = None
                if ing["strABV"] is not None:
                    abv = int(ing["strABV"])
                cursor.execute(
                    "INSERT INTO ingredients(id_ingredient,ingredient_name,ingredient_type,description,alcoholic,abv) VALUES"
                    "(%(id_ingredient)s, %(ingredient_name)s, %(ingredient_type)s, %(description)s, %(alcoholic)s,%(abv)s)           "
                    "RETURNING id_ingredient;                                                               ",
                    {
                        "id_ingredient": ing["idIngredient"],
                        "ingredient_name": unaccent(ing["strIngredient"]),
                        "ingredient_type": ing["strType"],
                        "description": ing["strDescription"],
                        "alcoholic": ing["strAlcohol"] == "Yes",
                        "abv": abv
                    },
                )
                res = cursor.fetchone()
                if res is None or res["id_ingredient"] != int(ing["idIngredient"]):
                    print(f"Ingredient n°{ing['idIngredient']} not created! res = {res}")

with open("../data/cocktails.json", "r") as f:
    cocktails = json.load(f)
    with DBConnection().connection as connection:
        for cocktail in cocktails:
            with connection.cursor() as cursor:
                try:
                    cursor.execute(
                        "INSERT INTO cocktails(id_recipe,recipe_name,category,alcoholic,glass_type,iba_category,instruction,cocktail_pic_url) VALUES"
                        "(%(id_recipe)s, %(recipe_name)s, %(category)s, %(alcoholic)s, %(glass_type)s, %(iba_category)s, %(instruction)s, %(pic_url)s)"
                        "RETURNING id_recipe;                                                               ",
                        {
                            "id_recipe": cocktail["idDrink"],
                            "recipe_name": cocktail["strDrink"],
                            "category": cocktail["strCategory"],
                            "alcoholic": cocktail["strAlcoholic"] == "Yes",
                            "glass_type": cocktail["strGlass"],
                            "iba_category": cocktail["strIBA"],
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
        unknown = {} # This dict saves unkown ingredients so I can add them in the database
        for cocktail in cocktails:
            for i in range(1,16):
                ingredient_name = cocktail[f'strIngredient{i}']
                measure = cocktail[f'strMeasure{i}']
                if ingredient_name == '':
                    continue
                if ingredient_name is None:
                    break
                with connection.cursor() as cursor:
                    try:
                        cursor.execute(
                            "SELECT id_ingredient FROM ingredients WHERE "
                            "UPPER(ingredient_name) = %(name)s;   ",
                            {
                                'name': unaccent(ingredient_name).upper()
                            }
                        )
                    except psycopg2.Error as e:
                        connection.rollback()
                        print(e)
                        continue
                    res = cursor.fetchone()
                    if res is None:
                        if ingredient_name not in unknown:
                            unknown[ingredient_name] = None
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
                                'quantity': measure
                            }
                        )
                    except psycopg2.errors.UniqueViolation as e:
                        connection.rollback()
                        print(e)
                        continue
                    except psycopg2.Error as e:
                        connection.rollback()
                        print(e)
                        continue
    for ing in unknown.keys():
        print(f'{ing}, ')
