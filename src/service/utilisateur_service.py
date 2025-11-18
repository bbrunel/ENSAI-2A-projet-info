from tabulate import tabulate

from business_object.utilisateur import Utilisateur
from dao.utilisateur_dao import UtilisateurDao
from utils.log_decorator import log
from utils.securite import hash_password


class UtilisateurService:
    """Classe contenant les méthodes de service des utilisateurs"""

    @staticmethod
    @log
    def creer(nom_utilisateur: str, hash_mdp: str):
        """Création d'un utilisateur à partir de ses attributs"""
        nouvel_utilisateur = Utilisateur(None, nom_utilisateur, hash_mdp)
        return UtilisateurDao().creer(nouvel_utilisateur)

    @staticmethod
    @log
    def lister_tous(inclure_mdp: bool = False) -> list[Utilisateur]:
        """Lister tous les utilisateurs
        Si inclure_mdp=True, les mots de passe seront inclus
        Par défaut, tous les mdp des utilisateurs sont à None
        """
        utilisateurs = UtilisateurDao().lister_tous()
        if not inclure_mdp:
            for u in utilisateurs:
                u.mdp = None
        return utilisateurs

    @staticmethod
    @log
    def trouver_par_id(id_utilisateur: int) -> Utilisateur:
        """Trouver un utilisateur à partir de son id"""
        return UtilisateurDao().trouver_par_id(id_utilisateur)

    @staticmethod
    @log
    def trouver_par_nom(nom_utilisateur: str) -> Utilisateur:
        """Trouver un utilisateur à partir de son nom"""
        return UtilisateurDao().trouver_par_nom(nom_utilisateur)

    @staticmethod
    @log
    def modifier(utilisateur: Utilisateur) -> Utilisateur:
        """Modification d'un utilisateur"""

        # Re-hacher le mot de passe avec le nom d'utilisateur comme sel
        utilisateur.mdp = hash_password(utilisateur.mdp, utilisateur.nom_utilisateur)
        return utilisateur if UtilisateurDao().modifier(utilisateur) else None

    @staticmethod
    @log
    def supprimer(utilisateur: Utilisateur) -> bool:
        """Supprimer le compte d'un utilisateur"""
        return UtilisateurDao().supprimer(utilisateur)

    @staticmethod
    @log
    def se_connecter(nom_utilisateur: str, mot_de_passe: str) -> Utilisateur:
        """Se connecter à partir de nom_utilisateur et mot_de_passe"""
        return UtilisateurDao().se_connecter(
            nom_utilisateur, hash_password(mot_de_passe, nom_utilisateur)
        )

    @staticmethod
    @log
    def nom_utilisateur_deja_utilise(nom_utilisateur: str) -> bool:
        """Vérifie si le nom_utilisateur est déjà utilisé
        Retourne True si le nom_utilisateur existe déjà en BDD"""
        utilisateurs = UtilisateurDao().lister_tous()
        return nom_utilisateur in [u.nom_utilisateur for u in utilisateurs]

    @staticmethod
    @log
    def afficher_tous() -> str:
        """Afficher tous les utilisateurs
        Sortie : Une chaine de caractères mise sous forme de tableau
        """
        entetes = ["ID", "Nom d'utilisateur"]

        utilisateurs = UtilisateurDao().lister_tous()

        # Filtrer les utilisateurs spéciaux si nécessaire
        # for u in utilisateurs:
        #     if u.nom_utilisateur == "admin":
        #         utilisateurs.remove(u)

        utilisateurs_as_list = [u.as_list() for u in utilisateurs]

        str_utilisateurs = "-" * 100
        str_utilisateurs += "\nListe des utilisateurs \n"
        str_utilisateurs += "-" * 100
        str_utilisateurs += "\n"
        str_utilisateurs += tabulate(
            tabular_data=utilisateurs_as_list,
            headers=entetes,
            tablefmt="psql",
            floatfmt=".2f",
        )
        str_utilisateurs += "\n"

        return str_utilisateurs
