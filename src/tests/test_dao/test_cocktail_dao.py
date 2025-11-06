from unittest.mock import MagicMock
from dao.cocktail_dao import CocktailDAO

from business_object.cocktail import Cocktail
from business_object.ingredient import Ingredient

def test_ingredient_cocktail():
    """
    Teste si la méthode renvoie bien les ingrédients qui composent un cocktail Mojito.
    """

    #GIVEN
    id_ingredients_mojito = [337, 305, 312, 476, 455]

    #WHEN
    ingredients = ingredients_ckt(11000)

    #THEN
    assert any([not (ing.id in id_ingredients_mojito) for ing in ingredients])
    assert len(ingredients) == 5


def test_list_tous_cocktails():
    """
    Vérifie si la fonction renvoie bien l'ensemble des cocktails de la base de données
    """

    #WHEN
    tous_cocktails = list_tous_cocktails()

    #THEN
    assert len(tous_cocktails) == n #/!\/!\/!\ n A DETERMINER /!\/!\/!\