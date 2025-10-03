import json

from dao.db_connection import DBConnection

with open('../data/ingredients.json','r') as f:
    ingredients = json.load(f)
    with DBConnection().connection as connection:
        for ing in ingredients:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO ingredients(id_ingredient,ingredient_name,ingredient_type,alcoholic) VALUES"
                    "(%(id_ingredient)s, %(ingredient_name)s, %(ingredient_type)s, %(alcoholic)s)           "
                    "RETURNING id_ingredient;                                                               ",
                    {
                        "id_ingredient": ing['idIngredient'],
                        "ingredient_name": ing['strIngredient'],
                        "ingredient_type": ing['strType'],
                        "acoholic": ing['strAlcohol'] == 'Yes'
                    }
                )
                res = cursor.fetchone()
            if res != ing['idIngredient']:
                print(f"Ingredient n°{ing['idIngredient']} not created!")


