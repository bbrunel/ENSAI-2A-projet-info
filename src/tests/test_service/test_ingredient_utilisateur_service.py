import sys

sys.path.append("../src")

import pytest
from unittest.mock import MagicMock, patch

from service.ingredient_utilisateur_service import IngredientUtilisateurService
from dao.ingredient_utilisateur_dao import IngredientUtilisateurDao
from business_object.utilisateur import Utilisateur
from business_object.ingredient import Ingredient

# Tests  #Tests unitaires


class Test_ing_utilisateur_service_unitaires:
    """
    Teste les méthodes de IngredientUtilisateurService
    """



    def test_ajout_ingredient_utilisateur_ok(self):
        """
        Teste que l'ajout d'un ingrédient par un utilisateur retourne bien l'ingrédient ajouté.
        Utilise patch pour mocker la méthode 'ajouter' du DAO.
        """
        # GIVEN
        id_utilisateur = 2
        id_ingredient = 513
        utilisateur = Utilisateur(id_utilisateur, "pseudo", "mdp")
        ingredient = Ingredient(id_ingredient, "eau", "", "boisson", False, 0)

        with patch(
            "dao.ingredient_utilisateur_dao.IngredientUtilisateurDao.ajouter",
            return_value=ingredient.id
        ) as mock_ajouter:

           # WHEN
           ingredient_ajoute = IngredientUtilisateurService().ajout_ingredient_utilisateur(utilisateur, ingredient)

        # THEN
        assert isinstance(ingredient_ajoute, Ingredient)
        assert ingredient_ajoute == ingredient
        mock_ajouter.assert_called_once_with(id_utilisateur, id_ingredient)




    def test_ajout_ingredient_utilisateur_ko(self):
        """
        Teste que l'ajout d'un ingrédient par un utilisateur échoue et retourne None.
        """
        # GIVEN
        id_utilisateur = 2
        id_ingredient = 513
        utilisateur = Utilisateur(id_utilisateur, "pseudo", "mdp")
        ingredient = Ingredient(id_ingredient, "eau", "", "boisson", False, 0)

        with patch(
            "dao.ingredient_utilisateur_dao.IngredientUtilisateurDao.ajouter",
            return_value=None
        ) as mock_ajouter:
            # WHEN
            resultat = IngredientUtilisateurService().ajout_ingredient_utilisateur(utilisateur, ingredient)

        # THEN
        assert resultat is None
        mock_ajouter.assert_called_once_with(id_utilisateur, id_ingredient)




    def test_supprimer_ingredient_utilisateur_ok(self):
        """
        Teste que la suppression d'un ingrédient par un utilisateur réussit et retourne True.
        """
        # GIVEN
        id_utilisateur = 2
        id_ingredient = 513
        utilisateur = Utilisateur(id_utilisateur, "pseudo", "mdp")
        ingredient = Ingredient(id_ingredient, "eau", "", "boisson", False, 0)

        with patch(
            "dao.ingredient_utilisateur_dao.IngredientUtilisateurDao.supprimer",
            return_value=True
        ) as mock_supprimer:
            # WHEN
            resultat = IngredientUtilisateurService().supprimer_ingredient_utilisateur(utilisateur, ingredient)

        # THEN
        assert resultat is True
        mock_supprimer.assert_called_once_with(id_utilisateur, id_ingredient)



    def test_supprimer_ingredient_utilisateur_ko(self):
        """
        Teste que la suppression d'un ingrédient par l'utilisateur échoue et retourne False.
        """
        # GIVEN
        id_utilisateur = 2
        id_ingredient = 513
        utilisateur = Utilisateur(id_utilisateur, "pseudo", "mdp")
        ingredient = Ingredient(id_ingredient, "eau", "", "boisson", False, 0)

        with patch(
            "dao.ingredient_utilisateur_dao.IngredientUtilisateurDao.supprimer",
            return_value=False
        ) as mock_supprimer:
            # WHEN
            resultat = IngredientUtilisateurService().supprimer_ingredient_utilisateur(utilisateur, ingredient)

        # THEN
        assert resultat is False
        mock_supprimer.assert_called_once_with(id_utilisateur, id_ingredient)


    liste_ingredients = [
        Ingredient(1, "eau", "", "boisson", False, 0),
        Ingredient(2, "citron", "", "fruit frais", False, 0),
        Ingredient(3, "menthe", "", "herbe", False, 0),
    ]



    def test_liste_tous_ingredients_utilisateur_ok(self):
        """
        Teste que la liste des ingrédients de l'utilisateur est bien retournée.
        """
        # GIVEN
        id_utilisateur = 2
        utilisateur = Utilisateur(id_utilisateur, "pseudo", "mdp")
        liste_ingredients = [
            Ingredient(513, "eau", "", "boisson", False, 0),
            Ingredient(514, "sucre", "", "épice", False, 0),
            Ingredient(515, "citron", "", "fruit", False, 0)
        ]

        with patch(
            "dao.ingredient_utilisateur_dao.IngredientUtilisateurDao.lister_tous",
            return_value=liste_ingredients
        ) as mock_lister_tous:
            # WHEN
            resultat = IngredientUtilisateurService().liste_tous_ingredients_utilisateur(utilisateur)

        # THEN
        assert len(resultat) == 3
        for i in range(3):
            assert resultat[i] == liste_ingredients[i]
        mock_lister_tous.assert_called_once_with(id_utilisateur)


    def test_liste_tous_ingredients_utilisateur_ko(self):
        """
        Teste que la liste des ingrédients de l'utilisateur n'est pas retournée
        (cas où le DAO retourne None, par exemple en cas d'erreur ou si l'utilisateur n'a aucun ingrédient).
        """
        # GIVEN
        id_utilisateur = 2
        utilisateur = Utilisateur(id_utilisateur, "pseudo", "mdp")

        with patch(
            "dao.ingredient_utilisateur_dao.IngredientUtilisateurDao.lister_tous",
            return_value=None
        ) as mock_lister_tous:
            # WHEN
            resultat = IngredientUtilisateurService().liste_tous_ingredients_utilisateur(utilisateur)

        # THEN
        assert resultat is None
        mock_lister_tous.assert_called_once_with(id_utilisateur)


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
