import os
import pytest

from unittest.mock import patch

from utils.reset_database import ResetDatabase
from utils.securite import hash_password

from dao.ingredient_utilisateur_dao import IngredientUtilisateurDao

from business_object.ingredient import Ingredient


# Créer un mock ?


@pytest.fixture(scope="session", autouse=True)
def setup_test_environment():
    """Initialisation des données de test"""
    with patch.dict(os.environ, {"SCHEMA": "projet_test_dao"}):
        ResetDatabase().lancer(test_dao=True)
        yield


def test_ajouter_ok():
    """Ajout de l'ingrédient au bar personnel réussi."""

    # GIVEN
    id_utilisateur = 1
    id_ingredient = 513

    # WHEN
    ajout_ok = IngredientUtilisateurDao().ajouter(id_utilisateur, id_ingredient)

    # THEN
    assert ajout_ok == id_ingredient
    assert ajout_ok
    assert id_ingredient


def test_ajouter_ko():
    """Ajout de l'ingrédient échoué (id_utilisateur et id_ingredient incorrects)"""

    # GIVEN
    id_utilisateur = "1"
    id_ingredient = False

    # WHEN
    ajout_ok = IngredientUtilisateurDao().ajouter(ingredient)

    # THEN
    assert not ajout_ok


def test_supprimer_ok():
    """Suppression de l'ingrédient réussie."""

    # GIVEN
    id_utilisateur = 1
    id_ingredient = 513

    # WHEN
    suppression_ok = IngredientUtilisateurDao().supprimer(ingredient)

    # THEN
    assert suppression_ok

def test_supprimer_ko():
    """Suppression de Ingredient échouée (id inconnu)"""

    # GIVEN
    id_utilisateur = 8888888888
    id_ingredient = 8888888888888

    # WHEN
    suppression_ok = IngredientUtilisateurDao().supprimer(ingredient)

    # THEN
    assert not suppression_ok
