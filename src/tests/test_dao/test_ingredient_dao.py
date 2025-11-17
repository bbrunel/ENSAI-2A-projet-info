import sys
sys.path.append('../src')

import os
import pytest

from unittest.mock import patch
from unittest.mock import MagicMock

from utils.reset_database import ResetDatabase
from utils.securite import hash_password

from dao.ingredient_dao import IngredientDao

from business_object.ingredient import Ingredient

from dao.db_connection import DBConnection


def ajouter_ok():
    """Création de Joueur réussie"""

    # GIVEN
    nom = "Potion magique"
    desc = "Yay"
    type_ing = "Potion"
    alcoolise = False
    abv = 0

    # WHEN
    ajout = IngredientDao().ajouter(
        nom,
        desc,
        type_ing,
        alcoolise,
        abv
    )

    # THEN
    assert isinstance(ajout, Ingredient)
    assert ajout.nom == "Potion magique"


def ajouter_ko():
    """Création de l'ingrédient échouée (age et mail incorrects)"""

    # GIVEN
    nom = "Potion magique"
    desc = True
    type_ing = "Potion"
    alcoolise = False
    abv = 0

    # WHEN
    ajout = IngredientDao().creer(
        nom,
        desc,
        type_ing,
        alcoolise,
        abv
    )

    # THEN
    assert ajout is None


def supprimer_ok():
    """Suppression de l'ingrédient réussie."""

    # GIVEN
    id_ingredient = 513

    # WHEN
    suppression = IngredientDao().supprimer(
        id_ingredient
    )

    # THEN
    assert suppression


def supprimer_ko():
    """Suppression de l'ingrédient échouée (id inconnu)."""

    # GIVEN
    id_ingredient = 8888888888888

    # WHEN
    suppression = IngredientDao().supprimer(
        id_ingredient
    )

    # THEN
    assert not suppression
