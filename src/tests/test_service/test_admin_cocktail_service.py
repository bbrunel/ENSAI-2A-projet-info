from unittest.mock import patch

import pytest

from service.admin_cocktail_service import AdminCocktailService
from service.cocktail_service import CocktailService

# variables pour du remplissage durant les tests
nom, tag, cat, iba, ver, alc, inst = "nom", ["tag"], "shot", "unforgettables", "jar", True, "inst"

from utils.reset_database import reset_database

reset_database()
# Tests unitaires


class Test_admin_cocktail_service_unitaire:
    """
    Tests unitaires sur la classe AdminCocktailService

    Methodes testées
    ----------
        ajout_cocktail
        supprimer_cocktail
    """

    ##ajout_cocktail

    def test_ajout_cocktail_erreur_type(self):
        """
        Teste si la methode lève bien une TypeError si les arguments rentrés sont du mauvais type.
        """
        # GIVEN
        nom0, tag0, cat0, iba0, alc0, ver0 = "nom", ["tag"], "cat", "iba", True, "ver"
        inst0, url_im0 = "inst", "url"
        nom, tag, cat, iba, alc, ver, inst, url_im = 0, "oui", 1, 2, "oui", 0, 3, 4

        arg0 = [nom0, tag0, cat0, iba0, alc0, ver0, inst0, url_im0]
        arg = [nom, tag, cat, iba, alc, ver, inst, url_im]

        # WHEN&THEN
        for i in range(len(arg)):
            arg0 = [nom0, tag0, cat0, iba0, alc0, ver0, inst0, url_im0]
            arg0[i] = arg[i]

            with pytest.raises(TypeError):
                AdminCocktailService().ajout_cocktail(
                    arg0[0], arg0[1], arg0[2], arg0[3], arg0[4], arg0[5], arg0[6], arg0[7]
                )

    def test_ajout_cocktail_erreur_ckt_existant(self):
        """
        Teste si la fonction lève une ValueError dans le cas où le cocktail qui doit être rajouté
        existe déjà dans la base de données.
        """
        # GIVEN
        with patch(
            "service.recherche_service.RechercheService.recherche_cocktail", return_value=None
        ):
            # WHEN&THEN
            with pytest.raises(ValueError):
                AdminCocktailService().ajout_cocktail(nom, tag, cat, iba, alc, ver, inst)

    def test_ajout_cocktail_erreur_ajout(self):
        """
        Teste si la fonction lève une ValueError dans le cas où le cocktail qui doit être rajouté
        n'a pas pu être rajouté.
        """
        # GIVEN
        with patch("dao.admin_cocktail_dao.AdminCocktailDAO.ajouter_ckt", return_value=None):
            # WHEN&THEN
            with pytest.raises(ValueError):
                AdminCocktailService().ajout_cocktail(nom, tag, cat, iba, alc, ver, inst)

    def test_ajout_cocktail_ok(self):
        """
        Teste si l'ajout de cocktail est réussi alors qu'il devrait l'être.
        """
        # GIVEN
        with patch("dao.admin_cocktail_dao.AdminCocktailDAO.ajouter_ckt", return_value=11000):
            # WHEN
            res = AdminCocktailService().ajout_cocktail(nom, tag, cat, iba, alc, ver, inst)

        # THEN
        assert isinstance(res, int)
        assert res == 11000

    # supprimer_cocktail

    def test_supprimer_cocktail_type_error(self):
        """
        Test si la méthode lève bien une TypeError si l'id rentré en argument n'est pas un int.
        """
        # GIVEN
        id = "11000"

        # WHEN&THEN
        with pytest.raises(TypeError):
            AdminCocktailService().supprimer_cocktail(id)

    def test_supprimer_cocktail_erreur_cocktail_inexistant(self):
        """
        Teste si une ValueError est bien levée dans le cas où l'id ne correspond pas à un cocktail.
        """
        # GIVEN
        id = 1100000

        # WHEN
        with patch("service.cocktail_service.CocktailService.verifier_cocktail", return_value=None):
            # THEN
            with pytest.raises(ValueError):
                AdminCocktailService().supprimer_cocktail(id)

    def test_supprimer_cocktail_erreur_non_suppression(self):
        """
        Teste si un échec de la suppression lève bien une ValueError
        """
        # GIVEN
        id = 11000

        # WHEN
        with patch("dao.admin_cocktail_dao.AdminCocktailDAO.suppr_ckt", return_value=False):
            # THEN
            with pytest.raises(ValueError):
                AdminCocktailService().supprimer_cocktail(id)

    def test_supprimer_cocktail_ok(self):
        """
        Teste si la fonction réussi dans un cas où elle devrait.
        """
        # GIVEN
        id = 11007

        # WHEN
        with patch("dao.admin_cocktail_dao.AdminCocktailDAO.suppr_ckt", return_value=True):
            res = AdminCocktailService().supprimer_cocktail(id)

        # THEN
        assert res


# Tests d'intégration


class Test_admin_cocktail_service_integration:
    """
    Tests d'intégration sur la classe AdminCocktailService

    Methodes testées
    ----------
        ajout_cocktail
        supprimer_cocktail
    """

    ##ajout_cocktail

    def test_ajout_cocktail_erreur_deja_existant(self):
        """
        Teste si la fonction lève une ValueError dans le cas où le cocktail qui doit être rajouté
        existe déjà dans la base de données.
        """
        # GIVEN
        id = 11001
        ckt = CocktailService().verifier_cocktail(id)

        # WHEN&THEN
        with pytest.raises(ValueError):
            AdminCocktailService().ajout_cocktail(
                ckt.nom,
                ckt.tags,
                ckt.categorie,
                ckt.iba,
                ckt.alcoolise,
                ckt.verre,
                ckt.instructions,
            )

    def test_ajout_cocktail_ok(self):
        """
        Teste si un cocktail qui est censé être ajouté l'est bien.
        """
        # WHEN
        res = AdminCocktailService().ajout_cocktail(nom, tag, cat, iba, alc, ver, inst)

        # THEN
        assert isinstance(res, int)
        assert res > 178300

    ##supprimer_cocktail

    def test_supprimer_cocktail_ok(self):
        """
        Teste si le cocktail est bien supprimé
        """
        # GIVEN
        id = 11002

        # WHEN
        res = AdminCocktailService().supprimer_cocktail(id)

        # THEN
        assert res
        with pytest.raises(ValueError):
            CocktailService().verifier_cocktail(id)
