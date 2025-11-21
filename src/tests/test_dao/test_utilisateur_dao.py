import os
from unittest.mock import patch

import pytest

from api.securite import get_password_hash
from business_object.utilisateur import Utilisateur
from dao.utilisateur_dao import UtilisateurDao


@pytest.fixture(scope="session", autouse=True)
def setup_test_environment():
    """Initialisation des données de test"""
    with patch.dict(os.environ, {"SCHEMA": "mock"}):
        # ResetDatabase().lancer(test_dao=True)
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
    """Vérifie que la méthode renvoie une liste d'Utilisateur
    de taille supérieure ou égale à 2
    """

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

    # GIVEN
    utilisateur = Utilisateur(nom_utilisateur="Noobie", mdp=get_password_hash("motdepasse"))

    # WHEN
    creation_ok = UtilisateurDao().creer(utilisateur)

    # THEN
    assert creation_ok
    assert utilisateur.id is not None
    assert utilisateur.id > 0


def test_creer_ko_username_existant():
    """Création d'Utilisateur échouée (username déjà existant) (###  il va falloir que username soit unique ou mettre la condition d'existance déja dans la fonction dans UtilisateurDao)"""

    # GIVEN
    utilisateur = Utilisateur(
        nom_utilisateur="Ismael",  # Doit déjà exister dans les données de test
        mdp=hash_password("motdepasse", "Ismael"),
    )

    # WHEN
    creation_ok = UtilisateurDao().creer(utilisateur)

    # THEN
    assert not creation_ok  # Doit échouer car username existe déjà


def test_modifier_ok():
    """Modification d'Utilisateur réussie"""

    # GIVEN
    nouveau_mdp = hash_password("nouveau_motdepasse", "Ismael")
    utilisateur = Utilisateur(id=5, nom_utilisateur="Mounkaila", mdp=nouveau_mdp)

    # WHEN
    modification_ok = UtilisateurDao().modifier(utilisateur)

    # THEN
    assert modification_ok


def test_modifier_ko():
    """Modification d'Utilisateur échouée (id inconnu)"""

    # GIVEN
    utilisateur = Utilisateur(
        id=8888, nom_utilisateur="id_inconnu", mdp=hash_password("mdp", "id_inconnu")
    )

    # WHEN
    modification_ok = UtilisateurDao().modifier(utilisateur)

    # THEN
    assert not modification_ok


def test_supprimer_ok():
    """Suppression d'Utilisateur réussie"""
    # à modifier en fonction de la base d'essaie
    # GIVEN
    utilisateur = Utilisateur(
        id=2, nom_utilisateur="Noobie", mdp=hash_password("motdepasse", "Noobie")
    )

    # WHEN
    suppression_ok = UtilisateurDao().supprimer(utilisateur)

    # THEN
    assert suppression_ok


def test_supprimer_ko():
    """Suppression d'Utilisateur échouée (id inconnu)"""

    # GIVEN
    utilisateur = Utilisateur(
        id=8888, nom_utilisateur="id_inconnu", mdp=hash_password("mdp", "id_inconnu")
    )

    # WHEN
    suppression_ok = UtilisateurDao().supprimer(utilisateur)

    # THEN
    assert not suppression_ok


def test_se_connecter_ok():
    """Connexion d'Utilisateur réussie"""

    # GIVEN
    nom_utilisateur = "Gerald"
    mdp = "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"

    # WHEN
    utilisateur = UtilisateurDao().se_connecter(nom_utilisateur, mdp)

    # THEN
    assert isinstance(utilisateur, Utilisateur)
    assert utilisateur.nom_utilisateur == nom_utilisateur


def test_se_connecter_ko_mauvais_mdp():
    """Connexion d'Utilisateur échouée (mauvais mot de passe)"""

    # GIVEN
    nom_utilisateur = "Gerald"
    mdp_incorrect = "mauvais_password"

    # WHEN
    utilisateur = UtilisateurDao().se_connecter(
        nom_utilisateur, hash_password(mdp_incorrect, nom_utilisateur)
    )

    # THEN
    assert utilisateur is None


def test_se_connecter_ko_utilisateur_inexistant():
    """Connexion d'Utilisateur échouée (utilisateur inexistant)"""

    # GIVEN
    nom_utilisateur = "utilisateur_inexistant"
    mdp = "quelconque"

    # WHEN
    utilisateur = UtilisateurDao().se_connecter(
        nom_utilisateur, hash_password(mdp, nom_utilisateur)
    )

    # THEN
    assert utilisateur is None


if __name__ == "__main__":
    pytest.main([__file__])
