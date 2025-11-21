import sys
sys.path.append('../src')

import pytest
from unittest.mock import MagicMock, patch

from service.cocktail_service import CocktailService, CocktailDAO, Cocktail, Ingredient
from service.recherche_service import RechercheService, FiltreCocktail, FiltreIngredient
from service.favoris_service import FavorisService, FavorisDAO, Favori


class Test_favoris_service_unitaires:
    """
    Teste les méthodes de la classe FavorisService
    """
    ##aj_fav_cocktail

    def test_aj_fav_cocktail_erreur_type_id(self):
        """
        Teste si la TypeError est bien levée dans le cas où l'id_utilisateur ou id_cocktail
        ne sont pas des int.
        """
        #GIVEN
        id_utilisateur = "id"
        id_cocktail = "id_rdm"
        
        #WHEN&THEN
        with pytest.raises(TypeError):
            FavorisService().aj_fav_cocktail(id_utilisateur, 11000)
        with pytest.raises(TypeError):
            FavorisService().aj_fav_cocktail(2, id_cocktail)
        
    def test_aj_fav_cocktail_erreur_deja_fav(self):
        """
        Teste si une erreur se lève bien dans le cas où un cocktail est déjà favori.
        """
        #GIVEN
        id_utilisateur, id_cocktail = 1, 11000

        #WHEN
        with patch("dao.favoris_dao.FavorisDAO.aj_fav", return_value=None):
            
            #THEN
            with pytest.raises(ValueError):
                FavorisService().aj_fav_cocktail(id_utilisateur, id_cocktail)
    
    def test_aj_fav_cocktail_ok(self):
        """
        Teste si la fonction renvoie bien un cocktail, et le bon cocktail lorsqu'elle réussi.
        """
        #GIVEN
        id_cocktail = 11000

        #WHEN
        with patch("dao.favoris_dao.FavorisDAO.aj_fav", return_value=True):
            cocktail = FavorisService().aj_fav_cocktail(1, id_cocktail)
        
        #THEN
        assert isinstance(cocktail, Cocktail)
        assert cocktail.nom == "Mojito"
    

    ##suppr_fav_cocktail

    def test_suppr_fav_cocktail_erreur_type_id(self):
        """
        Teste si la TypeError est bien levée dans le cas où l'id_utilisateur ou id_cocktail
        ne sont pas des int.
        """
        #GIVEN
        id_utilisateur = "id"
        id_cocktail = "id_rdm"
        
        #WHEN&THEN
        with pytest.raises(TypeError):
            FavorisService().suppr_fav_cocktail(id_utilisateur, 11000)
        with pytest.raises(TypeError):
            FavorisService().suppr_fav_cocktail(2, id_cocktail)

    def test_suppr_fav_cocktail_erreur_pas_fav(self):
        """
        Teste si une erreur se lève bien dans le cas où le cocktail n'est pas favori de 
        l'utilisateur.
        """
        #GIVEN
        id_utilisateur, id_cocktail = 1, 11000

        #WHEN
        with patch("dao.favoris_dao.FavorisDAO.suppr_fav", return_value=False):

            #THEN
            with pytest.raises(ValueError):
                FavorisService().suppr_fav_cocktail(id_utilisateur, id_cocktail)
    
    def test_suppr_fav_cocktail_ok(self):
        """
        Teste si la fonction renvoie bien True lorsqu'elle réussi.
        """
        #GIVEN
        id_utilisateur, id_cocktail = 1, 11000

        #WHEN
        with patch("dao.favoris_dao.FavorisDAO.suppr_fav", return_value=True):
            res = FavorisService().suppr_fav_cocktail(id_utilisateur, id_cocktail)

        #THEN
        assert isinstance(res, bool)
        assert res
    

    ##supprimer_tous

    def test_supprimer_tous_erreur_id(self):
        """Teste si la fonction lève une TypeError dans le cas où l'id n'est pas un int.
        """
        #GIVEN
        id_utilisateur = "id"

        #WHEN&THEN
        with pytest.raises(TypeError):
            FavorisService().supprimer_tous(id_utilisateur)
    
    def test_supprimer_tous_ok(self):
        """
        Teste si la méthode renvoie bien True lorsqu'elle réussi.
        """
        #GIVEN
        id_utilisateur = 1

        #WHEN
        with patch("dao.favoris_dao.FavorisDAO.supprimer_tous", return_value=True):
            res = FavorisService().supprimer_tous(id_utilisateur)
        
        #THEN
        assert isinstance(res, bool)
        assert res
    

    ##list_all_fav_cocktails

    def test_list_all_fav_erreur_id(self):
        """
        Teste si la fonction lève une TypeError dans le cas où l'id n'est pas un int.
        """
        #GIVEN
        id_utilisateur = "id"

        #WHEN&THEN
        with pytest.raises(TypeError):
            FavorisService().list_all_fav_cocktails(id_utilisateur)
    
    def test_list_all_fav_erreur_fav_vide(self):
        """
        Teste si une erreur se lève bien dans le cas où l'utilisateur n'a aucun favori à supprimer.
        """
        #GIVEN
        id_utilisateur = 1

        #WHEN
        with patch("dao.favoris_dao.FavorisDAO.lister_ts_fav", return_value=None):
        
            #THEN
            with pytest.raises(ValueError):
                FavorisService().list_all_fav_cocktails(id_utilisateur)
    
    def test_list_all_fav_ok(self):
        """
        Teste si la méthode renvoie bien une liste de Favoris lorsqu'elle réussi.
        """
        #GIVEN
        id_utilisateur = 1
        liste = [Favori(id=11000, nom = "Mojito")]

        #WHEN
        with patch("dao.favoris_dao.FavorisDAO.lister_ts_fav", return_value=liste):
            res = FavorisService().list_all_fav_cocktails(id_utilisateur)
        
        #THEN
        assert isinstance(res, list)
        assert all([isinstance(fav, Favori) for fav in res])
        assert res[0].nom == "Mojito"


class Test_favoris_service_integration:
    """
    Tests d'intégration pour la classe FavorisService
    """
    ##list_all_fav_cocktails

    def test_list_all_fav_erreur_fav_vide(self):
        """
        Teste si une erreur se lève bien dans le cas où l'utilisateur n'a aucun favori à supprimer.
        """
        #GIVEN
        id_utilisateur = 2

        #WHEN
        res = FavorisService().list_all_fav_cocktails(id_utilisateur)

        # THEN
        assert res == []

    def test_list_all_fav_ok(self):
        """
        Teste si la méthode renvoie bien une liste de Favoris lorsqu'elle réussi.
        """
        #GIVEN
        id_utilisateur = 1

        #WHEN
        res = FavorisService().list_all_fav_cocktails(id_utilisateur)
        
        #THEN
        assert isinstance(res, list)
        assert all([isinstance(fav, Favori) for fav in res])
        assert res[0].nom == "Mojito"


    ##aj_fav_cocktail
    
    def test_aj_fav_cocktail_erreur_deja_fav(self):
        """
        Teste si une erreur se lève bien dans le cas où un cocktail est déjà favori.
        """
        #GIVEN
        id_utilisateur, id_cocktail = 1, 11000
        
        #WHEN&THEN
        with pytest.raises(ValueError):
            FavorisService().aj_fav_cocktail(id_utilisateur, id_cocktail)
    
    def test_aj_fav_cocktail_ok(self):
        """
        Teste si la fonction renvoie bien un cocktail, et le bon cocktail lorsqu'elle réussi.
        """
        #GIVEN
        id_utilisateur, id_cocktail = 2, 11000

        #WHEN
        cocktail = FavorisService().aj_fav_cocktail(id_utilisateur, id_cocktail)
        favoris = FavorisService().list_all_fav_cocktails(id_utilisateur)
        
        #THEN
        assert isinstance(cocktail, Cocktail)
        assert cocktail.nom == "Mojito"
        assert "Mojito" in [fav.nom for fav in favoris]
    

    ##suppr_fav_cocktail

    def test_suppr_fav_cocktail_erreur_pas_fav(self):
        """
        Teste si une erreur se lève bien dans le cas où le cocktail n'est pas favori de 
        l'utilisateur.
        """
        #GIVEN
        id_utilisateur, id_cocktail = 3, 11000

        #WHEN&THEN
        with pytest.raises(ValueError):
            FavorisService().suppr_fav_cocktail(id_utilisateur, id_cocktail)

    def test_suppr_fav_cocktail_ok(self):
        """
        Teste si la fonction renvoie bien True lorsqu'elle réussi.
        """
        #GIVEN
        id_utilisateur, id_cocktail = 2, 11000

        #WHEN
        res = FavorisService().suppr_fav_cocktail(id_utilisateur, id_cocktail)

        #THEN
        assert isinstance(res, bool)
        assert res
        assert FavorisService().list_all_fav_cocktails(id_utilisateur) == []
    

    ##supprimer_tous
    
    def test_supprimer_tous_ok(self):
        """
        Teste si la méthode renvoie bien True lorsqu'elle réussi.
        """
        #GIVEN
        id_utilisateur = 1

        #WHEN
        res = FavorisService().supprimer_tous(id_utilisateur)
        
        #THEN
        assert isinstance(res, bool)
        assert res
        assert FavorisService().list_all_fav_cocktails(id_utilisateur) == []