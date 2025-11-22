import sys

sys.path.append("../src")

from unittest.mock import patch

import pytest

from business_object.cocktail import Cocktail
from business_object.filtre_cocktail import FiltreCocktail
from business_object.ingredient import Ingredient
from service.cocktail_service import CocktailService
from service.recherche_service import RechercheService

# Tests unitaires


class Test_cocktail_service_unitaire:
    """
    Teste la classe CocktailService à travers des tests unitaires.

    Methodes testées
    ----------
        verifier_cocktail
        ingredient_cocktail
        nb_cocktails
        list_tous_cocktails
    """

    ##verifier_cocktail
    def test_verifier_cocktail_ingredient(self):
        """
        Teste si la méthode vérifie correctement l'existence d'un cocktail.
        """

        # GIVEN
        mojito = RechercheService().recherche_cocktail(FiltreCocktail(id=11000))[0]
        with patch(
            "service.recherche_service.RechercheService.recherche_cocktail", return_value=[mojito]
        ):
            # WHEN
            filtre = FiltreCocktail(id=11000)
            cocktail = CocktailService().verifier_cocktail(11000)

        # THEN
        assert isinstance(cocktail, Cocktail)
        assert cocktail.nom == "Mojito"

    def test_verifier_cocktail_erreur(self):
        """
        Teste si un cocktail qui n'existe pas est recherché une erreur se
        lève bien.
        """

        # WHEN
        filtre = FiltreCocktail(id=1100000)

        # THEN
        with pytest.raises(TypeError):
            CocktailService().verifier_cocktail(filtre)

    ##ingredient_cocktail

    def test_ingredient_cocktail_ok(self):
        """
        Teste si la méthode renvoie bien les ingrédients qui composent un
        cocktail.
        Valeur retournée par la DAO fixée auparavant.
        """

        # GIVEN
        id_ingredients_mojito = [337, 305, 312, 476, 455]
        with patch(
            "dao.cocktail_dao.CocktailDAO.ingredients_ckt",
            return_value=[
                Ingredient(305, "ingredient 1", "", "", False, 0),
                Ingredient(312, "ingredient 2", "", "", False, 0),
                Ingredient(337, "ingredient 3", "", "", False, 0),
                Ingredient(455, "ingredient 4", "", "", False, 0),
                Ingredient(476, "ingredient 5", "", "", False, 0),
            ],
        ):
            # WHEN
            ingredients = CocktailService().ingredient_cocktail(11000)

        # THEN
        assert all([(ing.id in id_ingredients_mojito) for ing in ingredients])

    def test_ingredient_cocktail_ko(self):
        """
        Teste si la méthode renvoie bien les ingrédients qui composent un
        cocktail.
        Valeur retournée par la DAO fixée auparavant.
        """

        # GIVEN
        id_ingredients_mojito = [337, 305, 312, 476, 455]
        with patch(
            "dao.cocktail_dao.CocktailDAO.ingredients_ckt",
            return_value=[
                Ingredient(305, "ingredient 1", "", "", False, 0),
                Ingredient(312, "ingredient 2", "", "", False, 0),
                Ingredient(337, "ingredient 3", "", "", False, 0),
                Ingredient(455, "ingredient 4", "", "", False, 0),
            ],
        ):
            # WHEN
            ingredients = CocktailService().ingredient_cocktail(11000)

        # THEN
        assert all([(ing.id in id_ingredients_mojito) for ing in ingredients])

    ##nb_cocktails

    def test_nb_cocktails_ok(self):
        """
        teste si ce qui est renvoyé est homogène à ce qui est attendu.
        """
        # GIVEN
        with patch("dao.cocktail_dao.CocktailDAO.nb_cocktails", return_value=12000):
            # WHEN
            res = CocktailService().nb_cocktails()

        # THEN
        assert isinstance(res, int)
        assert res > 1

    def test_nb_cocktails_ko(self):
        """
        teste si ce qui est renvoyé n'est pas homogène à ce qui est attendu.
        """
        # GIVEN
        with patch("dao.cocktail_dao.CocktailDAO.nb_cocktails", return_value=None):
            # WHEN
            res = CocktailService().nb_cocktails()

            # THEN
            assert not isinstance(res, int)

    ##list_tous_cocktails

    def test_list_tous_cocktails_ok(self):
        """
        Vérifie si la fonction renvoiebien l'ensemble des cocktails de la base
        de données.
        """
        # GIVEN
        with patch(
            "dao.cocktail_dao.CocktailDAO.list_ts_cocktails",
            return_value=[
                Cocktail(id=1, nom="cocktail 1"),
                Cocktail(id=2, nom="cocktail 2"),
                Cocktail(id=3, nom="cocktail 3"),
                Cocktail(id=4, nom="cocktail 4"),
            ],
        ):
            # WHEN
            tous_cocktails = CocktailService().lister_tous_cocktail()

        # THEN
        assert isinstance(tous_cocktails, list)
        assert all(isinstance(ckt, Cocktail) for ckt in tous_cocktails)
        assert len(tous_cocktails) > 1
        assert len(tous_cocktails) == 4

    def test_list_tous_cocktails_ko(self):
        """
        Vérifie si la fonction ne renvoie pas bien l'ensemble des cocktails de la base
        de données.
        """
        # GIVEN
        with patch("dao.cocktail_dao.CocktailDAO.list_ts_cocktails", return_value=[None]):
            # WHEN
            tous_cocktails = CocktailService().lister_tous_cocktail()

        # THEN
        assert isinstance(tous_cocktails, list)
        assert tous_cocktails[0] is None


# Tests d'intégration


class Test_cocktail_service_integration:
    """
    Teste la classe CocktailService à travers des tests d'intégration.

    Methodes testées
    ----------
        verifier_cocktail
        ingredient_cocktail
        nb_cocktails
        lister_tous_cocktails
    """

    ##verifier_cocktail

    def test_verifier_cocktail_existence(self):
        """
        Teste si la méthode vérifie correctement l'existance d'un cocktail.
        """

        # WHEN
        filtre = FiltreCocktail(id=11000)
        cocktail = CocktailService().verifier_cocktail(11000)

        # THEN
        assert cocktail.nom == "Mojito"

    def test_verifier_cocktail_inexistence(self):
        """
        Teste si un cocktail qui n'existe pas est recherché une erreur se
        lève bien.
        """

        # GIVEN

        # WHEN
        filtre = FiltreCocktail(id=1100000)

        # THEN
        with pytest.raises(TypeError):
            CocktailService().verifier_cocktail(filtre)

    # ingredient_cocktail

    def test_ingredient_cocktail(self):
        """
        Teste si la méthode renvoie bien les ingrédients qui composent
        un cocktail.
        """

        # GIVEN
        id_ingredients_mojito = [337, 305, 312, 476, 455]

        # WHEN
        ingredients = CocktailService().ingredient_cocktail(11000)

        # THEN
        assert all([(ing.id in id_ingredients_mojito) for ing in ingredients])

    # nb_cocktails

    def test_nb_cocktails(self):
        """
        teste si ce qui est renvoyé est homogène à ce qui est attendu.
        """
        assert isinstance(CocktailService().nb_cocktails(), int)

    # lister_tous_cocktails

    def test_list_tous_cocktails(self):
        """
        Vérifie si la fonction renvoiebien l'ensemble des cocktails de la base
        de données.
        """

        # WHEN
        tous_cocktails = CocktailService().lister_tous_cocktail()

        # THEN
        assert len(tous_cocktails) == CocktailService().nb_cocktails()
