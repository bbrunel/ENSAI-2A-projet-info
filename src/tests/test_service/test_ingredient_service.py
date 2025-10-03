# Work in progress

from unittest.mock import MagicMock

from service.ingredient_service import IngredientService

from dao.ingredient_dao import IngredientDao

from business_object.ingredient import Ingredient


liste_ingredients = [
    Ingredient(id=1, nom="eau", desc="", type="boisson", alcoolise=False, abv=0),
    Ingredient(id=2, nom="citron", desc="", type="fruit frais", alcoolise=False, abv=0),
    Ingredient(id=3, nom="menthe", desc="", type="herbe", alcoolise=False, abv=0),
]


def test_ajout_ingredient_ok():
    """Ajout de l'ingredient réussi.
    """

    # GIVEN
    pseudo, mdp, age, mail, fan_pokemon = "jp", "1234", 15, "z@mail.oo", True
    IngredientDao().ajout_ingredient() = MagicMock(return_value=True)

    # WHEN
    joueur = IngredientService().ajout_ingredient(pseudo, mdp, age, mail, fan_pokemon)

    # THEN
    assert ingredient.pseudo == pseudo


def test_ajout_ingredient_echec():
    """Ajout de l'ingrédient échoué.
    """

    # GIVEN
    pseudo, mdp, age, mail, fan_pokemon = "jp", "1234", 15, "z@mail.oo", True
    IngredientDao().ajout_ingredient = MagicMock(return_value=False)

    # WHEN
    ingredient = IngredientService().ajout_ingredient(pseudo, mdp, age, mail, fan_pokemon)

    # THEN
    assert ingredient is None


def test_supprimer_ingredient_ok():
    """Suppression de l'ingrédient réussie.
    """

    # GIVEN
    JoueurDao().lister_tous = MagicMock(return_value=liste_joueurs)

    # WHEN
    res = JoueurService().lister_tous(inclure_mdp=True)

    # THEN
    assert len(res) == 3
    for joueur in res:
        assert joueur.mdp is not None


def test_supprimer_ingredient_echec():
    """Suppression de l'ingrédient échouée.
    """

    # GIVEN
    JoueurDao().lister_tous = MagicMock(return_value=liste_joueurs)

    # WHEN
    res = JoueurService().lister_tous()

    # THEN
    assert len(res) == 3
    for joueur in res:
        assert not joueur.mdp


def test_verifier_ingredient_ok():
    """Vérification de l'ingrédient réussie."""

    # GIVEN
    pseudo = "lea"

    # WHEN
    JoueurDao().lister_tous = MagicMock(return_value=liste_joueurs)
    res = JoueurService().pseudo_deja_utilise(pseudo)

    # THEN
    assert res


def test_verifier_ingredient_echec():
    """Vérification de l'ingrédient échouée."""

    # GIVEN
    pseudo = "chaton"

    # WHEN
    JoueurDao().lister_tous = MagicMock(return_value=liste_joueurs)
    res = JoueurService().pseudo_deja_utilise(pseudo)

    # THEN
    assert not res


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])