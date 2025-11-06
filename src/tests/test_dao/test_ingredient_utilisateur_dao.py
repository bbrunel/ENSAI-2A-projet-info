import os
import pytest

from unittest.mock import patch
from unittest.mock import MagicMock

from utils.reset_database import ResetDatabase
from utils.securite import hash_password

from dao.ingredient_utilisateur_dao import IngredientUtilisateurDao

from business_object.ingredient import Ingredient

from dao.db_connection import DBConnection


def test_ajouter_ok():
    """Ajout de l'ingrédient au bar personnel réussi."""

    # GIVEN
    id_utilisateur = 1
    id_ingredient = 513

    # WHEN
    ajout = IngredientUtilisateurDao().ajouter(
        id_utilisateur, 
        id_ingredient
    )

    # THEN
    print(ajout)
    print(id_ingredient)
    assert ajout == id_ingredient


def test_ajouter_ko():
    """Ajout de l'ingrédient échoué (id_utilisateur et id_ingredient
    incorrects)
    """

    # GIVEN
    id_utilisateur = 8888888
    id_ingredient = False

    # WHEN
    ajout = IngredientUtilisateurDao().ajouter(
        id_utilisateur, 
        id_ingredient
    )

    # THEN
    assert ajout is None


def test_supprimer_ok():
    """Suppression de l'ingrédient réussie."""

    # GIVEN
    id_utilisateur = 2
    id_ingredient = 305

    # WHEN
    suppression = IngredientUtilisateurDao().supprimer(
        id_utilisateur, 
        id_ingredient
    )

    # THEN
    assert suppression


def test_supprimer_ko():
    """Suppression de l'ingrédient échouée (id inconnu)."""

    # GIVEN
    id_utilisateur = 8888888888
    id_ingredient = 8888888888888

    # WHEN
    suppression = IngredientUtilisateurDao().supprimer(
        id_utilisateur, 
        id_ingredient
    )

    # THEN
    assert not suppression


def test_lister_tous():
    """Vérifie que la méthode renvoie une liste de Joueur
    de taille supérieure ou égale à 2
    """

    # GIVEN
    id_utilisateur = 1

    # WHEN
    ingredients = IngredientUtilisateurDao().lister_tous(id_utilisateur)

    # THEN
    assert isinstance(ingredients, list)
    for ing in ingredients:
        assert isinstance(ing, Ingredient)
    assert len(ingredients) >= 2
