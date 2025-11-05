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
    ingredient = Ingredient(nom="Test", desc="Test", type="Test", alcoolise=False, abv=0)

    # WHEN
    creation_ok = IngredientDao().ajouter(ingredient)

    # THEN
    assert creation_ok
    assert ingredient.id_ingredient


def test_ajouter_ko():
    """Ajout de l'ingrédient échouée (age et mail incorrects)"""

    # GIVEN
    ingredient = Ingredient(nom="Test", desc=12, type=True, alcoolise="False", abv="0")

    # WHEN
    creation_ok = IngredientDao().ajouter(ingredient)

    # THEN
    assert not creation_ok


def test_supprimer_ok():
    """Suppression de Joueur réussie"""

    # GIVEN
    joueur = Joueur(id_joueur=995, pseudo="miguel", age=1, mail="miguel@projet.fr")

    # WHEN
    suppression_ok = JoueurDao().supprimer(joueur)

    # THEN
    assert suppression_ok


def test_supprimer_ko():
    """Suppression de Joueur échouée (id inconnu)"""

    # GIVEN
    joueur = Joueur(id_joueur=8888, pseudo="id inconnu", age=1, mail="no@z.fr")

    # WHEN
    suppression_ok = JoueurDao().supprimer(joueur)

    # THEN
    assert not suppression_ok
