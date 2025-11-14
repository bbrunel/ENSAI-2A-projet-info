import pytest
from unittest.mock import MagicMock
from service.cocktail_service import CocktailService

from business_object.cocktail import Cocktail
from business_object.ingredient import Ingredient
from business_object.filtre_cocktail import FiltreCocktail

def test_verifier_cocktail_existance():
    """
    Teste si la méthode vérifie correctement l'existance d'un cocktail.
    """

    #GIVEN
    #nothing

    #WHEN
    filtre = FiltreCocktail(id = 11000)
    cocktail = CocktailService().verifier_cocktail(11000)

    #THEN
    assert "Mojito" in [ckt.nom for ckt in cocktail]


def test_verifier_cocktail_inexistance():
    """
    Teste si un cocktail qui n'existe pas est recherché une erreur se lève bien.
    """

    #GIVEN

    #WHEN
    filtre = FiltreCocktail(id = 1100000)

    #THEN
    with pytest.raises(TypeError):
            CocktailService().verifier_cocktail(filtre)
    

def test_ingredient_cocktail():
    """
    Teste si la méthode renvoie bien les ingrédients qui composent un cocktail.
    """

    #GIVEN
    id_ingredients_mojito = [337, 305, 312, 476, 455]

    #WHEN
    ingredients = CocktailService().ingredient_cocktail(11000)
    
    #THEN
    assert not any([not (ing.id in id_ingredients_mojito) for ing in ingredients])


def test_nb_cocktails():
    """
    teste si 
    """
    assert isinstance(CocktailService().nb_cocktails(), int)

def test_list_tous_cocktails():
    """
    Vérifie si la fonction renvoiebien l'ensemble des cocktails de la base de données.
    """

    #WHEN
    tous_cocktails = CocktailService().lister_tous_cocktail()

    #THEN
    assert len(tous_cocktails) == CocktailService().nb_cocktails()