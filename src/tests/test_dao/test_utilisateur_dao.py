import sys
import os
# Ajouter le chemin src au PYTHONPATH
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from unittest.mock import patch

import pytest

from business_object.utilisateur import Utilisateur
from dao.utilisateur_dao import UtilisateurDao


@pytest.fixture(scope="session", autouse=True)
def setup_test_environment():
    """Initialisation des données de test"""
    with patch.dict(os.environ, {"SCHEMA": "mock"}):
        yield


def test_trouver_par_id_existant():
    """Recherche par id d'un utilisateur existant"""

    # GIVEN
    id_utilisateur = 1

    # WHEN
    utilisateur = UtilisateurDao().trouver_par_id(id_utilisateur)

    # THEN
    assert utilisateur is not None
    assert utilisateur.id == 1
    assert isinstance(utilisateur, Utilisateur)


def test_trouver_par_id_non_existant():
    """Recherche par id d'un utilisateur n'existant pas"""

    # GIVEN
    id_utilisateur = 9999999999999

    # WHEN
    utilisateur = UtilisateurDao().trouver_par_id(id_utilisateur)

    # THEN
    assert utilisateur is None


def test_trouver_par_nom_existant():
    """Recherche par nom d'un utilisateur existant"""

    # GIVEN
    nom_utilisateur = "Gerald"

    # WHEN
    utilisateur = UtilisateurDao().trouver_par_nom(nom_utilisateur)

    # THEN
    assert utilisateur is not None
    assert utilisateur.nom_utilisateur == "Gerald"
    assert isinstance(utilisateur, Utilisateur)


def test_trouver_par_nom_non_existant():
    """Recherche par nom d'un utilisateur n'existant pas"""

    # GIVEN
    nom_utilisateur = "utilisateur_inexistant"

    # WHEN
    utilisateur = UtilisateurDao().trouver_par_nom(nom_utilisateur)

    # THEN
    assert utilisateur is None


def test_lister_tous():
    """Vérifie que la méthode renvoie une liste d'Utilisateur"""

    # GIVEN

    # WHEN
    utilisateurs = UtilisateurDao().lister_tous()

    # THEN
    assert isinstance(utilisateurs, list)
    for u in utilisateurs:
        assert isinstance(u, Utilisateur)
    assert len(utilisateurs) >= 2


def test_creer_ok():
    """Création d'Utilisateur réussie"""

    # GIVEN - Utiliser un nom unique avec timestamp
    import time
    nom_unique = f"TestUser_{int(time.time())}"
    utilisateur = Utilisateur(nom_utilisateur=nom_unique, mdp="motdepasse_hash")

    # WHEN
    resultat = UtilisateurDao().creer(utilisateur)

    # THEN
    assert resultat is not None
    assert resultat.id is not None
    assert resultat.id > 0


def test_creer_ko_username_existant():
    """Création d'Utilisateur échouée (username déjà existant)"""

    # GIVEN
    utilisateur = Utilisateur(
        nom_utilisateur="Gerald",  # Doit déjà exister dans les données de test
        mdp="motdepasse_hash",
    )

    # WHEN
    resultat = UtilisateurDao().creer(utilisateur)

    # THEN
    assert resultat is None  # Doit échouer car username existe déjà


def test_modifier_ok():
    """Modification d'Utilisateur réussie"""

    # GIVEN
    # Créer d'abord un utilisateur à modifier avec un nom unique
    import time
    nom_unique = f"TestModif_{int(time.time())}"
    utilisateur = Utilisateur(nom_utilisateur=nom_unique, mdp="ancien_mdp_hash")
    utilisateur_creer = UtilisateurDao().creer(utilisateur)
    
    # Vérifier que la création a réussi
    if utilisateur_creer is None:
        pytest.skip("La création d'utilisateur a échoué, impossible de tester la modification")
    
    nouveau_mdp = "nouveau_mdp_hash"
    utilisateur_modifie = Utilisateur(
        id=utilisateur_creer.id, 
        nom_utilisateur=nom_unique, 
        mdp=nouveau_mdp
    )

    # WHEN
    modification_ok = UtilisateurDao().modifier(utilisateur_modifie)

    # THEN
    assert modification_ok


def test_modifier_ko():
    """Modification d'Utilisateur échouée (id inconnu)"""

    # GIVEN
    utilisateur = Utilisateur(
        id=8888, nom_utilisateur="id_inconnu", mdp="mdp_hash"
    )

    # WHEN
    modification_ok = UtilisateurDao().modifier(utilisateur)

    # THEN
    assert not modification_ok


def test_supprimer_ok():
    """Suppression d'Utilisateur réussie"""
    
    # GIVEN
    # Créer d'abord un utilisateur à supprimer avec un nom unique
    import time
    nom_unique = f"TestSupprimer_{int(time.time())}"
    utilisateur = Utilisateur(nom_utilisateur=nom_unique, mdp="motdepasse_hash")
    utilisateur_creer = UtilisateurDao().creer(utilisateur)
    
    # Vérifier que la création a réussi
    if utilisateur_creer is None:
        pytest.skip("La création d'utilisateur a échoué, impossible de tester la suppression")

    # WHEN
    suppression_ok = UtilisateurDao().supprimer(utilisateur_creer)

    # THEN
    assert suppression_ok


def test_supprimer_ko():
    """Suppression d'Utilisateur échouée (id inconnu)"""

    # GIVEN
    utilisateur = Utilisateur(
        id=8888, nom_utilisateur="id_inconnu", mdp="mdp_hash"
    )

    # WHEN
    suppression_ok = UtilisateurDao().supprimer(utilisateur)

    # THEN
    assert not suppression_ok


if __name__ == "__main__":
    pytest.main([__file__])