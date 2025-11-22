import sys
import os
# Ajouter le chemin src au PYTHONPATH
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

import pytest
from unittest.mock import MagicMock, patch
from service.utilisateur_service import UtilisateurService
from business_object.utilisateur import Utilisateur
from dao.utilisateur_dao import UtilisateurDao

# Tests unitaires

class Test_utilisateur_service_unitaire:
    """
    Teste la classe UtilisateurService à travers des tests unitaires.

    Methodes testées
    ----------
        creer
        lister_tous
        trouver_par_id
        trouver_par_nom
        modifier
        supprimer
        nom_utilisateur_deja_utilise
        afficher_tous
    """

    ## creer

    def test_creer_ok(self):
        """
        Teste si la méthode crée bien un utilisateur.
        """
        # GIVEN
        nom_utilisateur, hash_mdp = "nouvel_utilisateur", "hash_password"
        utilisateur_attendu = Utilisateur(id=1, nom_utilisateur=nom_utilisateur, mdp=hash_mdp)
        
        with patch('dao.utilisateur_dao.UtilisateurDao.creer', 
                  return_value=utilisateur_attendu):
            
            # WHEN
            resultat = UtilisateurService.creer(nom_utilisateur, hash_mdp)

        # THEN
        assert resultat == utilisateur_attendu
        assert resultat.nom_utilisateur == nom_utilisateur

    def test_creer_echec(self):
        """
        Teste si la méthode retourne None en cas d'échec de création.
        """
        # GIVEN
        nom_utilisateur, hash_mdp = "nouvel_utilisateur", "hash_password"
        
        with patch('dao.utilisateur_dao.UtilisateurDao.creer', 
                  return_value=None):

            # WHEN
            resultat = UtilisateurService.creer(nom_utilisateur, hash_mdp)

        # THEN
        assert resultat is None

    ## lister_tous

    def test_lister_tous_inclure_mdp_true(self):
        """
        Teste si la méthode liste tous les utilisateurs avec mots de passe.
        """
        # GIVEN
        utilisateurs_attendus = [
            Utilisateur(id=1, nom_utilisateur="jean", mdp="hash_mdp_jean"),
            Utilisateur(id=2, nom_utilisateur="marie", mdp="hash_mdp_marie"),
        ]
        
        with patch('dao.utilisateur_dao.UtilisateurDao.lister_tous', 
                  return_value=utilisateurs_attendus):
            
            # WHEN
            resultat = UtilisateurService.lister_tous(inclure_mdp=True)

        # THEN
        assert resultat == utilisateurs_attendus
        assert all(utilisateur.mdp is not None for utilisateur in resultat)

    def test_lister_tous_inclure_mdp_false(self):
        """
        Teste si la méthode liste tous les utilisateurs sans mots de passe.
        """
        # GIVEN
        utilisateurs_attendus = [
            Utilisateur(id=1, nom_utilisateur="jean", mdp="hash_mdp_jean"),
            Utilisateur(id=2, nom_utilisateur="marie", mdp="hash_mdp_marie"),
        ]
        
        with patch('dao.utilisateur_dao.UtilisateurDao.lister_tous', 
                  return_value=utilisateurs_attendus):
            
            # WHEN
            resultat = UtilisateurService.lister_tous(inclure_mdp=False)

        # THEN
        assert all(utilisateur.mdp is None for utilisateur in resultat)

    ## trouver_par_id

    def test_trouver_par_id_existant(self):
        """
        Teste si la méthode trouve un utilisateur par ID existant.
        """
        # GIVEN
        id_utilisateur = 2
        utilisateur_attendu = Utilisateur(id=2, nom_utilisateur="marie", mdp="hash_mdp_marie")
        
        with patch('dao.utilisateur_dao.UtilisateurDao.trouver_par_id', 
                  return_value=utilisateur_attendu):
            
            # WHEN
            resultat = UtilisateurService.trouver_par_id(id_utilisateur)

        # THEN
        assert resultat == utilisateur_attendu
        assert resultat.id == id_utilisateur
        assert resultat.nom_utilisateur == "marie"

    def test_trouver_par_id_non_existant(self):
        """
        Teste si la méthode retourne None pour un ID non existant.
        """
        # GIVEN
        id_utilisateur = 999999999
        
        with patch('dao.utilisateur_dao.UtilisateurDao.trouver_par_id', 
                  return_value=None):

            # WHEN
            resultat = UtilisateurService.trouver_par_id(id_utilisateur)

        # THEN
        assert resultat is None

    ## trouver_par_nom

    def test_trouver_par_nom_existant(self):
        """
        Teste si la méthode trouve un utilisateur par nom existant.
        """
        # GIVEN
        nom_utilisateur = "marie"
        utilisateur_attendu = Utilisateur(id=2, nom_utilisateur="marie", mdp="hash_mdp_marie")
        
        with patch('dao.utilisateur_dao.UtilisateurDao.trouver_par_nom', 
                  return_value=utilisateur_attendu):
            
            # WHEN
            resultat = UtilisateurService.trouver_par_nom(nom_utilisateur)

        # THEN
        assert resultat == utilisateur_attendu
        assert resultat.nom_utilisateur == nom_utilisateur

    def test_trouver_par_nom_non_existant(self):
        """
        Teste si la méthode retourne None pour un nom non existant.
        """
        # GIVEN
        nom_utilisateur = "utilisateur_inexistant"
        
        with patch('dao.utilisateur_dao.UtilisateurDao.trouver_par_nom', 
                  return_value=None):

            # WHEN
            resultat = UtilisateurService.trouver_par_nom(nom_utilisateur)

        # THEN
        assert resultat is None

    ## modifier

    def test_modifier_ok(self):
        """
        Teste si la méthode modifie bien un utilisateur.
        """
        # GIVEN
        utilisateur = Utilisateur(id=1, nom_utilisateur="jean", mdp="nouveau_mdp")
        
        with patch('dao.utilisateur_dao.UtilisateurDao.modifier', 
                  return_value=True):
            
            # WHEN
            resultat = UtilisateurService.modifier(utilisateur)

        # THEN
        assert resultat == utilisateur
        assert resultat.nom_utilisateur == "jean"

    def test_modifier_echec(self):
        """
        Teste si la méthode retourne None en cas d'échec de modification.
        """
        # GIVEN
        utilisateur = Utilisateur(id=1, nom_utilisateur="jean", mdp="nouveau_mdp")
        
        with patch('dao.utilisateur_dao.UtilisateurDao.modifier', 
                  return_value=False):

            # WHEN
            resultat = UtilisateurService.modifier(utilisateur)

        # THEN
        assert resultat is None

    ## supprimer

    def test_supprimer_ok(self):
        """
        Teste si la méthode supprime bien un utilisateur.
        """
        # GIVEN
        utilisateur = Utilisateur(id=1, nom_utilisateur="jean", mdp="hash_mdp_jean")
        
        with patch('dao.utilisateur_dao.UtilisateurDao.supprimer', 
                  return_value=True):
            
            # WHEN
            resultat = UtilisateurService.supprimer(utilisateur)

        # THEN
        assert resultat is True

    def test_supprimer_echec(self):
        """
        Teste si la méthode retourne False en cas d'échec de suppression.
        """
        # GIVEN
        utilisateur = Utilisateur(id=1, nom_utilisateur="jean", mdp="hash_mdp_jean")
        
        with patch('dao.utilisateur_dao.UtilisateurDao.supprimer', 
                  return_value=False):

            # WHEN
            resultat = UtilisateurService.supprimer(utilisateur)

        # THEN
        assert resultat is False

    ## nom_utilisateur_deja_utilise

    def test_nom_utilisateur_deja_utilise_oui(self):
        """
        Teste si la méthode détecte un nom d'utilisateur déjà utilisé.
        """
        # GIVEN
        nom_utilisateur = "marie"
        utilisateurs = [
            Utilisateur(id=1, nom_utilisateur="jean", mdp="hash_mdp_jean"),
            Utilisateur(id=2, nom_utilisateur="marie", mdp="hash_mdp_marie"),
        ]
        
        with patch('dao.utilisateur_dao.UtilisateurDao.lister_tous', 
                  return_value=utilisateurs):
            
            # WHEN
            resultat = UtilisateurService.nom_utilisateur_deja_utilise(nom_utilisateur)

        # THEN
        assert resultat is True

    def test_nom_utilisateur_deja_utilise_non(self):
        """
        Teste si la méthode détecte un nom d'utilisateur non utilisé.
        """
        # GIVEN
        nom_utilisateur = "utilisateur_inexistant"
        utilisateurs = [
            Utilisateur(id=1, nom_utilisateur="jean", mdp="hash_mdp_jean"),
            Utilisateur(id=2, nom_utilisateur="marie", mdp="hash_mdp_marie"),
        ]
        
        with patch('dao.utilisateur_dao.UtilisateurDao.lister_tous', 
                  return_value=utilisateurs):
            
            # WHEN
            resultat = UtilisateurService.nom_utilisateur_deja_utilise(nom_utilisateur)

        # THEN
        assert resultat is False

    ## afficher_tous

    def test_afficher_tous_ok(self):
        """
        Teste si la méthode affiche correctement tous les utilisateurs.
        """
        # GIVEN
        utilisateurs = [
            Utilisateur(id=1, nom_utilisateur="jean", mdp="hash_mdp_jean"),
            Utilisateur(id=2, nom_utilisateur="marie", mdp="hash_mdp_marie"),
        ]
        
        with patch('dao.utilisateur_dao.UtilisateurDao.lister_tous', 
                  return_value=utilisateurs):
            
            # WHEN
            resultat = UtilisateurService.afficher_tous()

        # THEN
        assert isinstance(resultat, str)
        assert "Liste des utilisateurs" in resultat
        assert "jean" in resultat
        assert "marie" in resultat


# Tests d'intégration

class Test_utilisateur_service_integration:
    """
    Teste la classe UtilisateurService à travers des tests d'intégration.

    Methodes testées
    ----------
        trouver_par_id
        trouver_par_nom
        lister_tous
        nom_utilisateur_deja_utilise
        afficher_tous
    """

    ## trouver_par_id

    def test_trouver_par_id_existant(self):
        """
        Teste si la méthode trouve un utilisateur existant par ID.
        """
        # GIVEN
        # L'utilisateur Gerald a l'ID 1 dans ta base
        id_utilisateur = 1

        # WHEN
        resultat = UtilisateurService.trouver_par_id(id_utilisateur)

        # THEN
        assert resultat is not None
        assert resultat.id == id_utilisateur
        assert resultat.nom_utilisateur == "Gerald"

    def test_trouver_par_id_non_existant(self):
        """
        Teste si la méthode retourne None pour un ID non existant.
        """
        # GIVEN
        id_utilisateur = 999999

        # WHEN
        resultat = UtilisateurService.trouver_par_id(id_utilisateur)

        # THEN
        assert resultat is None

    ## trouver_par_nom

    def test_trouver_par_nom_existant(self):
        """
        Teste si la méthode trouve un utilisateur existant par nom.
        """
        # GIVEN
        nom_utilisateur = "Gerald"

        # WHEN
        resultat = UtilisateurService.trouver_par_nom(nom_utilisateur)

        # THEN
        assert resultat is not None
        assert resultat.nom_utilisateur == nom_utilisateur

    def test_trouver_par_nom_non_existant(self):
        """
        Teste si la méthode retourne None pour un nom non existant.
        """
        # GIVEN
        nom_utilisateur = "utilisateur_inexistant_12345"

        # WHEN
        resultat = UtilisateurService.trouver_par_nom(nom_utilisateur)

        # THEN
        assert resultat is None

    ## lister_tous

    def test_lister_tous_inclure_mdp_false(self):
        """
        Teste si la méthode liste tous les utilisateurs sans mots de passe.
        """
        # WHEN
        resultat = UtilisateurService.lister_tous(inclure_mdp=False)

        # THEN
        assert isinstance(resultat, list)
        assert len(resultat) >= 3  # Au moins Gerald, Hector, Bastien
        assert all(utilisateur.mdp is None for utilisateur in resultat)

    def test_lister_tous_inclure_mdp_true(self):
        """
        Teste si la méthode liste tous les utilisateurs avec mots de passe.
        """
        # WHEN
        resultat = UtilisateurService.lister_tous(inclure_mdp=True)

        # THEN
        assert isinstance(resultat, list)
        assert len(resultat) >= 3  # Au moins Gerald, Hector, Bastien
        # Au moins un utilisateur devrait avoir un mot de passe hashé
        assert any(utilisateur.mdp is not None and len(utilisateur.mdp) > 0 for utilisateur in resultat)

    ## nom_utilisateur_deja_utilise

    def test_nom_utilisateur_deja_utilise_oui(self):
        """
        Teste si la méthode détecte un nom d'utilisateur déjà utilisé.
        """
        # GIVEN
        nom_utilisateur = "Gerald"

        # WHEN
        resultat = UtilisateurService.nom_utilisateur_deja_utilise(nom_utilisateur)

        # THEN
        assert resultat is True

    def test_nom_utilisateur_deja_utilise_non(self):
        """
        Teste si la méthode détecte un nom d'utilisateur non utilisé.
        """
        # GIVEN
        nom_utilisateur = "utilisateur_inexistant_12345"

        # WHEN
        resultat = UtilisateurService.nom_utilisateur_deja_utilise(nom_utilisateur)

        # THEN
        assert resultat is False

    ## afficher_tous

    def test_afficher_tous(self):
        """
        Teste si la méthode affiche correctement tous les utilisateurs.
        """
        # WHEN
        resultat = UtilisateurService.afficher_tous()

        # THEN
        assert isinstance(resultat, str)
        assert "Liste des utilisateurs" in resultat
        # Vérifie que les utilisateurs de la base sont présents
        assert "Gerald" in resultat
        assert "Hector" in resultat
        assert "Bastien" in resultat


if __name__ == "__main__":
    pytest.main([__file__])