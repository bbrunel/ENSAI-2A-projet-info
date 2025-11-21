from unittest.mock import MagicMock, patch

from service.ingredient_utilisateur_service import IngredientUtilisateurService

from dao.ingredient_utilisateur_dao import IngredientUtilisateurDao

from business_object.utilisateur import Utilisateur

from business_object.ingredient import Ingredient


liste_ingredients = [
    Ingredient(1, "eau", "", "boisson", False, 0),
    Ingredient(2, "citron", "", "fruit frais", False, 0),
    Ingredient(3, "menthe", "", "herbe", False, 0),
]


def test_ajout_ingredient_utilisateur_ok():
    """Ajout de l'ingrédient par l'utilisateur réussi."""

    # GIVEN
    utilisateur = Utilisateur(2, "pseudo", "mdp")
    ingredient = Ingredient(513, "eau", "", "boisson", False, 0)
    IngredientUtilisateurDao().ajouter = MagicMock(return_value=ingredient.id)

    # WHEN
    ajout = IngredientUtilisateurService().ajout_ingredient_utilisateur(
        utilisateur,
        ingredient
    )

    # THEN
    assert ajout == ingredient


def test_ajout_ingredient_utilisateur_ko():
    """Ajout de l'ingredient par l'utilisateur échoué."""

    # GIVEN
    utilisateur = Utilisateur(2, "pseudo", "mdp")
    ingredient = Ingredient(513, "eau", "", "boisson", False, 0)
    IngredientUtilisateurDao().ajouter = MagicMock(return_value=None)

    # WHEN
    ajout = IngredientUtilisateurService().ajout_ingredient_utilisateur(
        utilisateur,
        ingredient
    )

    # THEN
    assert ajout is None


def test_supprimer_ingredient_utilisateur_ok():
    """Suppression de l'ingrédient par l'utilisateur réussie."""

    # GIVEN
    utilisateur = Utilisateur(2, "pseudo", "mdp")
    ingredient = Ingredient(513, "eau", "", "boisson", False, 0)
    IngredientUtilisateurDao().supprimer = MagicMock(return_value=True)

    # WHEN
    suppression = IngredientUtilisateurService().supprimer_ingredient_utilisateur(
        utilisateur, 
        ingredient
    )

    # THEN
    assert suppression


def test_supprimer_ingredient_utilisateur_ko():
    """Suppression de l'ingrédient par l'utilisateur échouée.
    """

    # GIVEN
    utilisateur = Utilisateur(2, "pseudo", "mdp")
    ingredient = Ingredient(513, "eau", "", "boisson", False, 0)
    IngredientUtilisateurDao().supprimer = MagicMock(return_value=False)

    # WHEN
    suppression = IngredientUtilisateurService().supprimer_ingredient_utilisateur(
        utilisateur, 
        ingredient
    )

    # THEN
    assert not suppression


def test_liste_tous_ingredients_utilisateur_ok():
    """La liste des ingrédients de l'utilisateur est bien retournée.
    """

    # GIVEN
    utilisateur = Utilisateur(2, "pseudo", "mdp")
    IngredientUtilisateurDao().lister_tous = MagicMock(return_value=liste_ingredients)

    # WHEN
    res = IngredientUtilisateurService().liste_tous_ingredients_utilisateur(utilisateur)

    # THEN
    assert len(res) == 3
    for i in range(3):
        assert res[i] == liste_ingredients[i]


def test_liste_tous_ingredients_utilisateur_ko():
    """La liste des ingrédients de l'utilisateur n'est pas retournée.
    (Préciser dans quel(s) cas.)
    """

    # GIVEN
    utilisateur = Utilisateur(2, "pseudo", "mdp")
    IngredientUtilisateurDao().lister_tous = MagicMock(return_value=None)

    # WHEN
    res = IngredientUtilisateurService().liste_tous_ingredients_utilisateur(utilisateur)

    # THEN
    assert res is None


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
