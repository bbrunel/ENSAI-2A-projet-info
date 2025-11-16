import sys
sys.path.append('../src')

from unittest.mock import MagicMock

from business_object.ingredient import Ingredient
from dao.ingredient_dao import IngredientDao
from service.ingredient_service import IngredientService


def test_ajout_ingredient_ok():
    """Ajout de l'ingredient réussi.
    """

    # GIVEN
    id, nom, desc, type_ing, alcoolise, abv = 88, "nom", "desc", "type_ing", False, 0
    ingredient = Ingredient(
        id,
        nom,
        desc,
        type_ing,
        alcoolise,
        abv
    )
    IngredientDao().ajouter = MagicMock(return_value=ingredient)

    # WHEN
    nouvel_ingredient = IngredientService().ajout_ingredient(
        nom,
        desc,
        type_ing,
        alcoolise,
        abv
    )

    # THEN
    assert nouvel_ingredient.nom == nom


def test_ajout_ingredient_ko():
    """Ajout de l'ingrédient échoué.
    """

    # GIVEN
    ingredient = Ingredient("nom", "desc", "type", False, 0)
    IngredientDao().ajouter = MagicMock(return_value=ingredient)

    # WHEN
    nouvel_ingredient = IngredientService().ajout_ingredient(ingredient)

    # THEN
    assert nouvel_ingredient is None


def test_supprimer_ingredient_ok():
    """Suppression de l'ingrédient réussie.
    """

    # GIVEN
    ingredient = Ingredient(513, "eau", "desc", "boisson", False, 0)
    IngredientDao().supprimer = MagicMock(return_value=True)

    # WHEN
    suppression = IngredientService().supprimer_ingredient_utilisateur(
        ingredient
    )

    # THEN
    assert suppression


def test_supprimer_ingredient_ko():
    """Suppression de l'ingrédient échouée.
    """

    # GIVEN
    ingredient = Ingredient(513, "eau", "", "boisson", False, 0)
    IngredientDao().supprimer = MagicMock(return_value=False)

    # WHEN
    suppression = IngredientService().supprimer_ingredient_utilisateur(
        ingredient
    )

    # THEN
    assert not suppression


def test_verifier_ingredient_true():
    """Vérification de l'existence de l'ingrédient réussie."""

    # GIVEN
    id = 513
    ingredient = Ingredient(513, "eau", "", "boisson", False, 0)
    IngredientDao().vérifier = MagicMock(return_value=[ingredient])

    # WHEN
    res = IngredientService().verifier_ingredient(id)

    # THEN
    assert res[0] == ingredient


def test_verifier_ingredient_false():
    """Vérification de l'ingrédient échouée."""

    # GIVEN
    id = 888888888888888

    # WHEN
    IngredientDao().verifier = MagicMock(return_value=None)
    res = IngredientService().verifier_ingredient(id)

    # THEN
    assert res is None


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
