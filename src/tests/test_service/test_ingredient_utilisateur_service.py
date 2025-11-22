import sys

sys.path.append("../src")

from unittest.mock import patch

import pytest

from business_object.ingredient import Ingredient
from business_object.utilisateur import Utilisateur
from service.ingredient_service import IngredientService
from service.ingredient_utilisateur_service import IngredientUtilisateurService as IUS
from service.utilisateur_service import UtilisateurService

# Tests


# Tests unitaires
class Test_ing_utilisateur_service_unitaires:
    """
    Tests unitaires pour la classe IngredientUtilisateurService


    Methodes testées
    ----------
        ajout_ingredient_utilisateur
        supprimer_ingredient_utilisateur
        liste_tous_ingredients_utilisateur
    """

    ##ajout_ingredient_utilisateur

    def test_ajout_ingredient_utilisateur_erreur_type(self):
        """
        Teste si une TypeError se lève bien dans le cas où le type des arguments est incorrect.
        """
        # GIVEN
        id_utilisateur = 2
        id_ingredient = 513
        utilisateur = Utilisateur(id_utilisateur, "pseudo", "mdp")
        ingredient = Ingredient(id_ingredient, "eau", "", "boisson", False, 0)

        # WHEN&THEN
        with pytest.raises(TypeError):
            IUS().ajout_ingredient_utilisateur(utilisateur, "ingredient")
            IUS().ajout_ingredient_utilisateur("utilisateur", ingredient)

    def test_ajout_ingredient_utilisateur_ok(self):
        """
        Teste si la méthode réussi bien.

        """
        # GIVEN
        id_utilisateur = 2
        id_ingredient = 513
        utilisateur = Utilisateur(id_utilisateur, "pseudo", "mdp")
        ingredient = Ingredient(id_ingredient, "eau", "", "boisson", False, 0)

        with patch(
            "dao.ingredient_utilisateur_dao.IngredientUtilisateurDao.ajouter",
            return_value=ingredient.id,
        ):
            # WHEN
            ingredient_ajoute = IUS().ajout_ingredient_utilisateur(utilisateur, ingredient)

        # THEN
        assert isinstance(ingredient_ajoute, Ingredient)
        assert ingredient_ajoute == ingredient

    def test_ajout_ingredient_utilisateur_ko(self):
        """
        Teste que l'ajout d'un ingrédient par un utilisateur échoue et lève une erreur.
        """
        # GIVEN
        id_utilisateur = 2
        id_ingredient = 513
        utilisateur = Utilisateur(id_utilisateur, "pseudo", "mdp")
        ingredient = Ingredient(id_ingredient, "eau", "", "boisson", False, 0)

        with patch(
            "dao.ingredient_utilisateur_dao.IngredientUtilisateurDao.ajouter", return_value=None
        ):
            # WHEN&THEN
            with pytest.raises(ValueError):
                IUS().ajout_ingredient_utilisateur(utilisateur, ingredient)

    ##supprimer_ingredient

    def test_supprimer_ingredient_utilisateur_erreur_type(self):
        """
        Teste si une TypeError se lève bien dans le cas où le type des arguments est incorrect.
        """
        # GIVEN
        id_utilisateur = 2
        id_ingredient = 513
        utilisateur = Utilisateur(id_utilisateur, "pseudo", "mdp")
        ingredient = Ingredient(id_ingredient, "eau", "", "boisson", False, 0)

        # WHEN&THEN
        with pytest.raises(TypeError):
            IUS().supprimer_ingredient_utilisateur(utilisateur, "ingredient")
            IUS().supprimer_ingredient_utilisateur("utilisateur", ingredient)

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
            "dao.ingredient_utilisateur_dao.IngredientUtilisateurDao.supprimer", return_value=True
        ):
            # WHEN
            resultat = IUS().supprimer_ingredient_utilisateur(utilisateur, ingredient)

        # THEN
        assert resultat is True

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
            "dao.ingredient_utilisateur_dao.IngredientUtilisateurDao.supprimer", return_value=False
        ):
            # WHEN
            resultat = IUS().supprimer_ingredient_utilisateur(utilisateur, ingredient)

        # THEN
        assert resultat is False

    ##liste_tous_ingrédients_utilisateur

    liste_ingredients = [
        Ingredient(1, "eau", "", "boisson", False, 0),
        Ingredient(2, "citron", "", "fruit frais", False, 0),
        Ingredient(3, "menthe", "", "herbe", False, 0),
    ]

    def test_list_tous_ingredient_utilisateur_erreur_type(self):
        """
        Teste si une TypeError se lève bien dans le cas où le type de l'argument est incorrect.
        """
        # WHEN&THEN
        with pytest.raises(TypeError):
            IUS().supprimer_ingredient_utilisateur("utilisateur")

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
            Ingredient(515, "citron", "", "fruit", False, 0),
        ]

        with patch(
            "dao.ingredient_utilisateur_dao.IngredientUtilisateurDao.lister_tous",
            return_value=liste_ingredients,
        ):
            # WHEN
            resultat = IUS().liste_tous_ingredients_utilisateur(utilisateur)

        # THEN
        assert len(resultat) == 3
        for i in range(3):
            assert resultat[i] == liste_ingredients[i]

    def test_liste_tous_ingredients_utilisateur_ko(self):
        """
        Teste que la liste des ingrédients de l'utilisateur n'est pas retournée
        (cas où le DAO retourne None, par exemple en cas d'erreur ou si l'utilisateur n'a
        aucun ingrédient).
        """
        # GIVEN
        id_utilisateur = 2
        utilisateur = Utilisateur(id_utilisateur, "pseudo", "mdp")

        with patch(
            "dao.ingredient_utilisateur_dao.IngredientUtilisateurDao.lister_tous", return_value=None
        ):
            # WHEN
            resultat = IUS().liste_tous_ingredients_utilisateur(utilisateur)

        # THEN
        assert resultat is None


# Tests d'intégration


class Test_ing_utilisateur_service_integration:
    """
    Tests d'intégration pour la classe IngredientUtilisateurService

    Methodes testées
    ----------
        ajout_ingredient_utilisateur
        supprimer_ingredient_utilisateur
        liste_tous_ingredients_utilisateur
    """

    ##ajout_ingredient_utilisateur

    def test_integ_aj_ing_ok(self):
        """
        Teste si la méthode renvoie bien l'id du cocktail si l'ajout aux ingrédients réussi
        """
        # GIVEN
        utilisateur = UtilisateurService().trouver_par_id(2)
        ingr = IngredientService().verifier_ingredient(312)

        # WHEN
        ingr_resultat = IUS().ajout_ingredient_utilisateur(utilisateur, ingr)
        ingr_util = IUS().liste_tous_ingredients_utilisateur(utilisateur)

        assert ingr_resultat.id == ingr.id
        assert 312 in [ingred.id for ingred in ingr_util]

    ##Supprimer_tous

    def test_integ_supp_tt_ing_util_ok(self):
        """
        Teste si la méthode supprime bien tous les ingrédients de l'utilisateur et renvoie True
        """
        # GIVEN
        utilisateur = UtilisateurService().trouver_par_id(2)

        # WHEN
        res = IUS().supprimer_tous(utilisateur)

        # THEN
        assert isinstance(res, bool)
        assert res
        assert IUS().liste_tous_ingredients_utilisateur(utilisateur) == []

    # liste_tous_ingredients_utilisateur

    def test_integ_list_ing_util_vide(self):
        """
        Teste si la liste des ingrédients d'un utilisateur est bien vide
        """
        # GIVEN
        utilisateur = UtilisateurService().trouver_par_id(2)

        # WHEN
        res = IUS().liste_tous_ingredients_utilisateur(utilisateur)

        # THEN
        assert res == []

    def test_integ_list_ing_util_ok(self):
        """
        Teste si un ingrédient est bien dans l'inventaire de l'utilisateur
        """
        # GIVEN
        utilisateur = UtilisateurService().trouver_par_id(1)

        # WHEN
        res = IUS().liste_tous_ingredients_utilisateur(utilisateur)

        # THEN
        assert isinstance(res, list)
        assert all([isinstance(ing, Ingredient) for ing in res])
        assert "Mint" in [ing.nom for ing in res]

    # supprimer_ingredient_utilisateur

    def test_integ_suppr_ingredient_utilisateur_ok(self):
        """
        Teste si la méthode supprime bien et renvoie un bool
        """
        # GIVEN
        utilisateur = UtilisateurService().trouver_par_id(1)
        ingr = IngredientService().verifier_ingredient(312)

        # WHEN
        res = IUS().supprimer_ingredient_utilisateur(utilisateur, ingr)
        ingr_util = IUS().liste_tous_ingredients_utilisateur(utilisateur)

        # THEN
        assert isinstance(res, bool)
        assert 312 not in [ingred.id for ingred in ingr_util]


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
