import os
import pytest

from unittest.mock import patch

from utils.reset_database import ResetDatabase
from utils.securite import hash_password

from dao.ingredient_utilisateur_dao import IngredientUtilisateurDao

from business_object.ingredient import Ingredient


@pytest.fixture(scope="session", autouse=True)
def setup_test_environment():
    """Initialisation des données de test"""
    with patch.dict(os.environ, {"SCHEMA": "projet_test_dao"}):
        ResetDatabase().lancer(test_dao=True)
        yield


def test_ajouter_ok():
    """Ajout de l'ingrédient au bar personnel réussi."""

    # GIVEN
    id_utilisateur = 2
    id_ingredient = 513

    # WHEN
    ajout = IngredientUtilisateurDao().ajouter(id_utilisateur, id_joueur)

    # THEN
    assert ajout.id_ingredient == id_ingredient


def test_ajouter_ko():
    """Ajout de l'ingrédient échoué (id_utilisateur et id_ingredient incorrects)"""

    # GIVEN
    id_utilisateur = 8888888
    id_ingredient = False

    # WHEN
    ajout = IngredientUtilisateurDao().ajouter(id_utilisateur, id_ingredient)

    # THEN
    assert ajout is None


def test_supprimer_ok():
    """Suppression de l'ingrédient réussie."""

    # GIVEN
    id_utilisateur = 2
    id_ingredient = 305

    # WHEN
    suppression = IngredientUtilisateurDao().supprimer(id_utilisateur, id_ingredient)

    # THEN
    assert suppression

def test_supprimer_ko():
    """Suppression de Ingredient échouée (id inconnu)"""

    # GIVEN
    id_utilisateur = 8888888888
    id_ingredient = 8888888888888

    # WHEN
    suppression = IngredientUtilisateurDao().supprimer(id_utilisateur, id_ingredient)

    # THEN
    assert not suppression
