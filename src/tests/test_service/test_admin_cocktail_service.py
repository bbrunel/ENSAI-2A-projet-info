from unittest.mock import MagicMock, patch
import pytest

from business_object.cocktail import Cocktail
from business_object.ingredient import Ingredient

from service.recherche_service import RechercheService
from service.admin_cocktail_service import AdminCocktailService
from service.cocktail_service import CocktailService

from dao.admin_cocktail_dao import AdminCocktailDAO

nom, tag, cat, iba, ver, alc, inst = "nom", ["tag"], "shot", "unforgettables", "jar", True, "inst" 
#Tests unitaires

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
        #GIVEN
        nom0, tag0, cat0, iba0, alc0, ver0 = "nom", ["tag"], "cat", "iba", True, "ver"
        inst0, url_im0 = "inst", "url"
        nom, tag, cat, iba, alc, ver, inst, url_im = 0, "oui", 1, 2, "oui", 0, 3, 4


        arg0 = [nom0, tag0, cat0, iba0, alc0, ver0, inst0, url_im0]
        arg = [nom, tag, cat, iba, alc, ver, inst, url_im]

        #WHEN&THEN
        for i in range(len(arg)):
            arg0 = [nom0, tag0, cat0, iba0, alc0, ver0, inst0, url_im0]
            arg0[i] = arg[i]

            with pytest.raises(TypeError):
                AdminCocktailService().ajout_cocktail(arg0[0],
                                        arg0[1],
                                        arg0[2],
                                        arg0[3],
                                        arg0[4],
                                        arg0[5],
                                        arg0[6],
                                        arg0[7])
    
    def test_ajout_cocktail_erreur_ckt_existant(self):
        """
        Teste si la fonction lève une ValueError dans le cas où le cocktail qui doit être rajouté
        existe déjà dans la base de données.
        """
        #GIVEN
        nom, tag, cat, iba, ver, alc, inst = "nom", ["tag"], "cat", "iba", "ver", True, "inst" 
        with patch("service.recherche_service.RechercheService.recherche_cocktail", 
        return_value = []):
        
            #WHEN&THEN
            with pytest.raises(ValueError):
                AdminCocktailService().ajout_cocktail(nom, tag, cat, iba, alc, ver, inst)
    
    def test_ajout_cocktail_erreur_ajout(self):
        """
        Teste si la fonction lève une ValueError dans le cas où le cocktail qui doit être rajouté
        n'a pas pu être rajouté.
        """
        #GIVEN
        with patch("dao.admin_cocktail_dao.AdminCocktailDAO.ajouter_ckt", return_value = None):
        
            #WHEN&THEN
            with pytest.raises(ValueError):
                AdminCocktailService().ajout_cocktail(nom, tag, cat, iba, alc, ver, inst)
    
    def test_ajout_cocktail_ok(self):
        """
        Teste si l'ajout de cocktail est réussi alors qu'il devrait l'être.
        """
        #GIVEN
        with patch("dao.admin_cocktail_dao.AdminCocktailDAO.ajouter_ckt", return_value=11000):
            
            #WHEN
            res = AdminCocktailService().ajout_cocktail(nom, tag, cat, iba, alc, ver, inst)
        
        #THEN
        assert isinstance(res, int)
        assert res == 11000