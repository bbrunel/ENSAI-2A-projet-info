from unittest.mock import MagicMock
from service.cocktail_service import CocktailService

from business_object.cocktail import Cocktail
from business_object.ingredient import Ingredient

def test_verifier_cocktail_existance():
    """
    Teste si la méthode vérifie correctement l'existance d'un cocktail.
    """

    #GIVEN
    #nothing

    #WHEN
    cocktail = CocktailService().verifier_cocktail(11000)

    #THEN
    assert cocktail.nom == "Mojito"


def test_verifier_cocktail_inexistance():
    """
    Teste si un cocktail qui n'existe pas est recherché une erreur se lève bien.
    """

    #GIVEN

    #WHEN
    cocktail_inexistant = verifier_cocktail(1100000)

    #THEN
    with pytest.raises(ValueError):
            verifier_cocktail(1100000)
    

def test_ingredient_cocktail():
    """
    Teste si la méthode renvoie bien les ingrédients qui compose un cocktail.
    """

    #GIVEN
    id_ingredients_mojito = [337, 305, 312, 476, 455]

    #WHEN
    ingredients = CocktailService().ingredient_cocktail(11000)

    #THEN
    assert any([not (ing.id in id_ingredients_mojito) for ing in ingredients])


def test_list_tous_cocktails():
    """
    Vérifie si la fonction renvoie bien l'ensemble des cocktails de la base de données.
    """

    #WHEN
    tous_cocktails = list_tous_cocktails()

    #THEN
    assert len(tous_cocktails) == n     #   /!\/!\/!\   n A DETERMINER  /!\/!\/!\