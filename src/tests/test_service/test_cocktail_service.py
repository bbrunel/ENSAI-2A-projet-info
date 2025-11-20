import sys
sys.path.append('../src')

import pytest
from unittest.mock import MagicMock, patch
from service.cocktail_service import CocktailService
from service.recherche_service import RechercheService
from dao.cocktail_dao import CocktailDAO
from business_object.cocktail import Cocktail
from business_object.ingredient import Ingredient
from business_object.filtre_cocktail import FiltreCocktail


# Tests unitaires


def test_verifier_cocktail_ingredient():
    """
    Teste si la méthode vérifie correctement l'existence d'un cocktail.
    """

    # GIVEN
    RechercheService().recherche_cocktail = MagicMock(
        return_value=["Mojito"]
    )  # ???

    # WHEN
    filtre = FiltreCocktail(id=11000)
    cocktail = CocktailService().verifier_cocktail(11000)

    # THEN
    assert "Mojito" in [ckt.nom for ckt in cocktail]


def test_verifier_cocktail_erreur():
    """
    Teste si un cocktail qui n'existe pas est recherché une erreur se
    lève bien.
    """

    # GIVEN

    # WHEN
    filtre = FiltreCocktail(id=1100000)

    # THEN
    with pytest.raises(TypeError):
        CocktailService().verifier_cocktail(filtre)


def test_ingredient_cocktail_ok():
    """
    Teste si la méthode renvoie bien les ingrédients qui composent un
    cocktail.
    Valeur retournée par la DAO fixée auparavant.
    """

    # GIVEN
    id_ingredients_mojito = [337, 305, 312, 476, 455]
    CocktailDAO().ingredients_ckt = MagicMock(
        return_value=[
            Ingredient(305, "ingredient 1", "", "", False, 0),
            Ingredient(312, "ingredient 2", "", "", False, 0),
            Ingredient(337, "ingredient 3", "", "", False, 0),
            Ingredient(455, "ingredient 4", "", "", False, 0),
            Ingredient(476, "ingredient 5", "", "", False, 0)
        ]
    )

    # WHEN
    ingredients = CocktailService().ingredient_cocktail(11000)

    # THEN
    assert not any(
        [
            not (ing.id in id_ingredients_mojito) for ing in ingredients
        ]
    )


def test_ingredient_cocktail_ko():
    """
    Teste si la méthode renvoie bien les ingrédients qui composent un
    cocktail.
    Valeur retournée par la DAO fixée auparavant.
    """

    # GIVEN
    id_ingredients_mojito = [337, 305, 312, 476, 455]
    CocktailDAO().ingredients_ckt = MagicMock(
        return_value=[
            Ingredient(305, "ingredient 1", "", "", False, 0),
            Ingredient(312, "ingredient 2", "", "", False, 0),
            Ingredient(337, "ingredient 3", "", "", False, 0),
            Ingredient(455, "ingredient 4", "", "", False, 0),
            Ingredient(477, "ingredient 5", "", "", False, 0)
        ]
    )

    # WHEN
    ingredients = CocktailService().ingredient_cocktail(11000)

    # THEN
    assert all(
        [
            (ing.id in id_ingredients_mojito) for ing in ingredients
        ]
    )


def test_nb_cocktails_ok():
    """
    teste si
    """
    # GIVEN
    CocktailDAO().nb_cocktails = MagicMock(return_value=12000)

    # WHEN
    res = CocktailService().nb_cocktails()

    # THEN
    assert isinstance(res, int)
    assert res > 1


def test_nb_cocktails_ko():
    """
    teste si
    """
    # GIVEN
    with patch('__main__.CocktailDAO.nb_cocktail', return_value=None):
        #CocktailDAO().nb_cocktails = MagicMock(return_value=None)

        # WHEN
        res = CocktailService().nb_cocktails()

        # THEN
        assert not isinstance(res, int)


def test_list_tous_cocktails_ok():
    """
    Vérifie si la fonction renvoiebien l'ensemble des cocktails de la base
    de données.
    """
    # GIVEN
    CocktailDAO().list_ts_cocktails = MagicMock(
        return_value=[
            Cocktail(1, "cocktail 1", "", "", "", "", True, "", "", ""),
            Cocktail(2, "cocktail 2", "", "", "", "", True, "", "", ""),
            Cocktail(3, "cocktail 3", "", "", "", "", True, "", "", ""),
            Cocktail(4, "cocktail 4", "", "", "", "", True, "", "", "")
        ]
    )

    # WHEN
    tous_cocktails = CocktailService().lister_tous_cocktail()

    # THEN
    assert isinstance(tous_cocktails, list)
    assert all(isinstance(ckt, Cocktail) for ckt in tous_cocktails)
    assert len(tous_cocktails) > 1
    assert len(tous_cocktails) == 4


def test_list_tous_cocktails_ko():
    """
    Vérifie si la fonction renvoie bien l'ensemble des cocktails de la base
    de données.
    """
    # GIVEN
    CocktailDAO().list_ts_cocktails = MagicMock(return_value=[None])

    # WHEN
    tous_cocktails = CocktailService().lister_tous_cocktail()

    # THEN
    assert isinstance(tous_cocktails, list)
    assert all(isinstance(ckt, Cocktail) for ckt in tous_cocktails)


# Tests d'intégration


def test_verifier_cocktail_existence():
    """
    Teste si la méthode vérifie correctement l'existance d'un cocktail.
    """

    # GIVEN
    # nothing

    # WHEN
    filtre = FiltreCocktail(id=11000)
    cocktail = CocktailService().verifier_cocktail(11000)

    # THEN
    assert "Mojito" in [ckt.nom for ckt in cocktail]


def test_verifier_cocktail_inexistence():
    """
    Teste si un cocktail qui n'existe pas est recherché une erreur se
    lève bien.
    """

    # GIVEN

    # WHEN
    filtre = FiltreCocktail(id=1100000)

    # THEN
    with pytest.raises(TypeError):
        CocktailService().verifier_cocktail(filtre)


def test_ingredient_cocktail():
    """
    Teste si la méthode renvoie bien les ingrédients qui composent
    un cocktail.
    """

    # GIVEN
    id_ingredients_mojito = [337, 305, 312, 476, 455]

    # WHEN
    ingredients = CocktailService().ingredient_cocktail(11000)

    # THEN
    assert not any(
        [
            not (ing.id in id_ingredients_mojito) for ing in ingredients
        ]
    )


def test_nb_cocktails():
    """
    teste si
    """
    assert isinstance(CocktailService().nb_cocktails(), int)


def test_list_tous_cocktails():
    """
    Vérifie si la fonction renvoiebien l'ensemble des cocktails de la base
    de données.
    """

    # WHEN
    tous_cocktails = CocktailService().lister_tous_cocktail()

    # THEN
    assert len(tous_cocktails) == CocktailService().nb_cocktails()
