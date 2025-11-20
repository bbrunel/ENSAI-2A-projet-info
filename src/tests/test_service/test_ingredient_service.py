import sys
sys.path.append('../src')
import pytest
from unittest.mock import MagicMock, patch

from business_object.ingredient import Ingredient
from business_object.filtre_ingredient import FiltreIngredient
from dao.ingredient_dao import IngredientDao
from service.ingredient_service import IngredientService
from service.recherche_service import RechercheService


##TESTS UNITAIRES
class Test_ingredient_service_unitaire:
    def test_ajout_ingredient_ok(self):
        """Ajout de l'ingredient réussi.
        """

        # GIVEN
        rose = RechercheService().recherche_ingredient(FiltreIngredient(id=615))[0]
        with patch('dao.ingredient_dao.IngredientDao.ajouter', return_value=rose.id):

            # WHEN
            nouvel_ingredient = IngredientService().ajout_ingredient(
                rose.nom,
                rose.desc,
                rose.type_ing,
                rose.alcoolise,
                rose.abv
            )
            filtre = FiltreIngredient(id = rose.id)
            nouvel_ing = RechercheService().recherche_ingredient(filtre)[0]

        # THEN
        assert nouvel_ingredient.nom == rose.nom


    def test_ajout_ingredient_ko(self):
        """Ajout de l'ingrédient échoué.
        """

        # GIVEN
        nom, desc, type_ing, alcoolise, abv = "nom", "desc", "type_ing", False, 0
        with patch('dao.ingredient_dao.IngredientDao.ajouter', return_value=None):

            # WHEN
            nouvel_ingredient = IngredientService().ajout_ingredient(
                nom,
                desc,
                type_ing,
                alcoolise,
                abv
            )

        # THEN
        assert nouvel_ingredient is None


    def test_supprimer_ingredient_ok(self):
        """Suppression de l'ingrédient réussie.
        """

        # GIVEN
        ingredient = Ingredient(513, "eau", "desc", "boisson", False, 0)
        with patch('dao.ingredient_dao.IngredientDao.supprimer', return_value=True):

            # WHEN
            suppression = IngredientService().supprimer_ingredient(
                ingredient
            )

        # THEN
        assert suppression


    def test_supprimer_ingredient_ko(self):
        """Suppression de l'ingrédient échouée.
        """

        # GIVEN
        ingredient = Ingredient(513, "eau", "", "boisson", False, 0)
        with patch('dao.ingredient_dao.IngredientDao.supprimer', return_value=False):

            # WHEN
            suppression = IngredientService().supprimer_ingredient(
                ingredient
            )

        # THEN
        assert not suppression


    def test_verifier_ingredient_true(self):
        """Vérification de l'existence de l'ingrédient réussie."""

        # GIVEN
        id = 513
        ingredient = Ingredient(513, "Eau", "", "boisson", False, 0)
        with patch('service.recherche_service.RechercheService.recherche_ingredient', return_value=[ingredient]):

            # WHEN
            ingredient_verifie = IngredientService().verifier_ingredient(id)

        # THEN
        assert ingredient_verifie == ingredient


    def test_verifier_ingredient_false(self):
        """Vérification de l'ingrédient échouée."""
        
        # GIVEN
        id = 888888888888888

        # THEN
        with pytest.raises(ValueError):
                IngredientService().verifier_ingredient(id)


##TESTS D'INTEGRATION
class Test_ingredient_service_integration:
    """
    """
    def test_ajout_ingredient_ok_integration(self):
        """Ajout de l'ingredient réussi dans la base de données.
        """

        # GIVEN
        id_max = IngredientDao().id_ing_max()
        id, nom, desc, type_ing, alcoolise, abv = id_max+1, "nom", "desc", "type_ing", False, 0
        ingredient = Ingredient(
            id,
            nom,
            desc,
            type_ing,
            alcoolise,
            abv
        )

        # WHEN
        
        id_ing_test = IngredientDao().ajouter(
            nom,
            desc,
            type_ing,
            alcoolise,
            abv
        )
        filtre = FiltreIngredient(id = id_ing_test)
        recherche_test = RechercheService().recherche_ingredient(filtre)

        # THEN
        assert recherche_test != []
        assert recherche_test[0].nom == nom

    def test_recherche_ingredient_filtre_id(self):
        """
        Teste si la fonction renvoie bien les cocktails dont le nom correspond à 'Mauresque'.
        """
        
        #GIVEN
        filtre = FiltreIngredient(id = 305)

        #WHEN
        recherche = RechercheService().recherche_ingredient(filtre)

        #THEN
        assert "Light Rum" in [ing.nom for ing in recherche]


    def test_verifier_ingredient_true(self):
        """Vérification de l'existence de l'ingrédient réussie."""

        # GIVEN
        id = 513

        # WHEN
        ingredient_verifie = IngredientService().verifier_ingredient(id)

        # THEN
        assert ingredient_verifie.nom == "Water"


    def test_supprimer_ingredient_ok(self):
        """Suppression de l'ingrédient réussie.
        """

        # GIVEN
        ingredient = IngredientService().verifier_ingredient(513)

        # WHEN
        suppression = IngredientService().supprimer_ingredient(ingredient)

        # THEN
        assert suppression


    def test_verifier_ingredient_false(self):
        """Vérification de l'ingrédient échouée."""

        # GIVEN
        id = 888888888888888

        # THEN
        with pytest.raises(ValueError):
                IngredientService().verifier_ingredient(id)


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
