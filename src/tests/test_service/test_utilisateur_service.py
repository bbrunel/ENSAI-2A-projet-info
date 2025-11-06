import sys
import os
import pytest
from unittest.mock import MagicMock


# Ajoute le dossier src au chemin Python
current_file = __file__
tests_service_dir = os.path.dirname(current_file)  # dossier test_service
tests_dir = os.path.dirname(tests_service_dir)     # dossier tests  
src_dir = os.path.dirname(tests_dir)               # dossier src
sys.path.insert(0, src_dir)  # Ajoute au début de la liste


from service.utilisateur_service import UtilisateurService
from dao.utilisateur_dao import UtilisateurDao
from business_object.utilisateur import Utilisateur
from utils.securite import hash_password


# Liste mock d'utilisateurs pour les tests
liste_utilisateurs = [
    Utilisateur(id=1, nom_utilisateur="jean", mdp="hash_mdp_jean"),
    Utilisateur(id=2, nom_utilisateur="marie", mdp="hash_mdp_marie"),
    Utilisateur(id=3, nom_utilisateur="pierre", mdp="hash_mdp_pierre"),
]


def test_creer_ok():
    """Création d'Utilisateur réussie"""

    # GIVEN
    nom_utilisateur, mot_de_passe = "nouvel_utilisateur", "password123"
    UtilisateurDao().creer = MagicMock(return_value=True)

    # WHEN
    utilisateur = UtilisateurService().creer(nom_utilisateur, mot_de_passe)

    # THEN
    assert utilisateur is not None
    assert utilisateur.nom_utilisateur == nom_utilisateur
    expected_hash = hash_password(mot_de_passe, nom_utilisateur)
    assert utilisateur.mdp == expected_hash  # Compare avec le hash calculé


def test_creer_echec():
    """Création d'Utilisateur échouée
    (quand le méthode UtilisateurDao.creer retourne False)"""

    # GIVEN
    nom_utilisateur, mot_de_passe = "nouvel_utilisateur", "password123"
    UtilisateurDao().creer = MagicMock(return_value=False)

    # WHEN
    utilisateur = UtilisateurService().creer(nom_utilisateur, mot_de_passe)

    # THEN
    assert utilisateur is None


def test_lister_tous_inclure_mdp_true():
    """Lister les Utilisateurs en incluant les mots de passe"""

    # GIVEN
    UtilisateurDao().lister_tous = MagicMock(return_value=liste_utilisateurs)

    # WHEN
    res = UtilisateurService().lister_tous(inclure_mdp=True)

    # THEN
    assert len(res) == 3
    for utilisateur in res:
        assert utilisateur.mdp is not None


def test_lister_tous_inclure_mdp_false():
    """Lister les Utilisateurs en excluant les mots de passe"""

    # GIVEN
    UtilisateurDao().lister_tous = MagicMock(return_value=liste_utilisateurs)

    # WHEN
    res = UtilisateurService().lister_tous(inclure_mdp=False)

    # THEN
    assert len(res) == 3
    for utilisateur in res:
        assert utilisateur.mdp is None 


def test_nom_utilisateur_deja_utilise_oui():
    """Le nom d'utilisateur est déjà utilisé dans liste_utilisateurs"""

    # GIVEN
    nom_utilisateur = "marie"

    # WHEN
    UtilisateurDao().lister_tous = MagicMock(return_value=liste_utilisateurs)
    res = UtilisateurService().nom_utilisateur_deja_utilise(nom_utilisateur)

    # THEN
    assert res


def test_nom_utilisateur_deja_utilise_non():
    """Le nom d'utilisateur n'est pas utilisé dans liste_utilisateurs"""

    # GIVEN
    nom_utilisateur = "utilisateur_inexistant"

    # WHEN
    UtilisateurDao().lister_tous = MagicMock(return_value=liste_utilisateurs)
    res = UtilisateurService().nom_utilisateur_deja_utilise(nom_utilisateur)

    # THEN
    assert not res


def test_trouver_par_id_existant():
    """Trouver un utilisateur par ID existant"""

    # GIVEN
    id_utilisateur = 2
    utilisateur_mock = Utilisateur(id=2, nom_utilisateur="marie", mdp="hash_mdp_marie")
    UtilisateurDao().trouver_par_id = MagicMock(return_value=utilisateur_mock)

    # WHEN
    utilisateur = UtilisateurService().trouver_par_id(id_utilisateur)

    # THEN
    assert utilisateur is not None
    assert utilisateur.id == id_utilisateur
    assert utilisateur.nom_utilisateur == "marie"


def test_trouver_par_id_non_existant():
    """Trouver un utilisateur par ID non existant"""

    # GIVEN
    id_utilisateur = 999999999
    UtilisateurDao().trouver_par_id = MagicMock(return_value=None)

    # WHEN
    utilisateur = UtilisateurService().trouver_par_id(id_utilisateur)

    # THEN
    assert utilisateur is None


def test_se_connecter_ok():
    """Connexion d'utilisateur réussie"""

    # GIVEN
    nom_utilisateur, mot_de_passe = "jean", "mdp_jean"
    utilisateur_mock = Utilisateur(id=1, nom_utilisateur="jean", mdp="hash_mdp_jean")
    UtilisateurDao().se_connecter = MagicMock(return_value=utilisateur_mock)

    # WHEN
    utilisateur = UtilisateurService().se_connecter(nom_utilisateur, mot_de_passe)

    # THEN
    assert utilisateur is not None
    assert utilisateur.nom_utilisateur == nom_utilisateur


def test_se_connecter_echec():
    """Connexion d'utilisateur échouée"""

    # GIVEN
    nom_utilisateur, mot_de_passe = "jean", "mauvais_mdp"
    UtilisateurDao().se_connecter = MagicMock(return_value=None)

    # WHEN
    utilisateur = UtilisateurService().se_connecter(nom_utilisateur, mot_de_passe)

    # THEN
    assert utilisateur is None


def test_modifier_ok():
    """Modification d'utilisateur réussie"""

    # GIVEN
    utilisateur = Utilisateur(id=1, nom_utilisateur="jean", mdp="nouveau_mdp")
    UtilisateurDao().modifier = MagicMock(return_value=True)

    # WHEN
    resultat = UtilisateurService().modifier(utilisateur)

    # THEN
    assert resultat is not None
    assert resultat.nom_utilisateur == "jean"


def test_modifier_echec():
    """Modification d'utilisateur échouée"""

    # GIVEN
    utilisateur = Utilisateur(id=1, nom_utilisateur="jean", mdp="nouveau_mdp")
    UtilisateurDao().modifier = MagicMock(return_value=False)

    # WHEN
    resultat = UtilisateurService().modifier(utilisateur)

    # THEN
    assert resultat is None


def test_supprimer_ok():
    """Suppression d'utilisateur réussie"""

    # GIVEN
    utilisateur = Utilisateur(id=1, nom_utilisateur="jean", mdp="hash_mdp_jean")
    UtilisateurDao().supprimer = MagicMock(return_value=True)

    # WHEN
    resultat = UtilisateurService().supprimer(utilisateur)

    # THEN
    assert resultat is True


def test_supprimer_echec():
    """Suppression d'utilisateur échouée"""

    # GIVEN
    utilisateur = Utilisateur(id=1, nom_utilisateur="jean", mdp="hash_mdp_jean")
    UtilisateurDao().supprimer = MagicMock(return_value=False)

    # WHEN
    resultat = UtilisateurService().supprimer(utilisateur)

    # THEN
    assert resultat is False


def test_afficher_tous():
    """Affichage de tous les utilisateurs formaté"""

    # GIVEN
    UtilisateurDao().lister_tous = MagicMock(return_value=liste_utilisateurs)

    # WHEN
    resultat = UtilisateurService().afficher_tous()

    # THEN
    assert isinstance(resultat, str)
    assert "Liste des utilisateurs" in resultat
    assert "jean" in resultat
    assert "marie" in resultat
    assert "pierre" in resultat


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])