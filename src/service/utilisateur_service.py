from tabulate import tabulate

from business_object.utilisateur import Utilisateur

from dao.utilisateur_dao import UtilisateurDao

from utils.log_decorator import log


class UtilisateurService:
    """
    Classe contenant les méthodes de service des utilisateurs
    
    Methodes
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

    @staticmethod
    @log
    def creer(nom_utilisateur: str, hash_mdp: str):
        """Création d'un utilisateur à partir de ses attributs

        Parameters
        ----------
        nom_utilisateur : str
        hash_mdp : str

        Returns
        -------
            l'utilisateur si la création est un succès et None sinon.
        """
        nouvel_utilisateur = Utilisateur(None, nom_utilisateur, hash_mdp)
        return UtilisateurDao().creer(nouvel_utilisateur)

    @staticmethod
    @log
    def lister_tous(inclure_mdp: bool = False) -> list[Utilisateur]:
        """Liste tous les utilisateurs.

        Si inclure_mdp=True, les mots de passe seront inclus
        Par défaut, tous les mdp des utilisateurs sont à None

        Parameters
        ----------
        inclure_mdp : bool

        Returns
        -------
        list[Utilisateur]
            Liste des utilisateurs.
        """
        utilisateurs = UtilisateurDao().lister_tous()
        if not inclure_mdp:
            for u in utilisateurs:
                u.mdp = None
        return utilisateurs

    @staticmethod
    @log
    def trouver_par_id(id_utilisateur: int) -> Utilisateur:
        """Trouver un utilisateur à partir de son id

        Parameters
        ----------
        id_utilisateur : int
            Identifiant de l'utilisateur à retrouver.

        Returns
        -------
        Utilisateur
            Utilisateur retrouvé à partir de l'identifiant.
        """
        return UtilisateurDao().trouver_par_id(id_utilisateur)

    @staticmethod
    @log
    def trouver_par_nom(nom_utilisateur: str) -> Utilisateur:
        """Trouve un utilisateur à partir de son nom.

        Parameters
        ----------
        nom_utilisateur : str
            Nom de l'utilisateur à retrouver.

        Returns
        -------
        Utilisateur
            Utilisateur trouvé à partir du nom.
        """
        return UtilisateurDao().trouver_par_nom(nom_utilisateur)

    @staticmethod
    @log
    def modifier(utilisateur: Utilisateur) -> Utilisateur:
        """Modification d'un utilisateur

        Parameters
        ----------

        Returns
        -------
        
        """
        return utilisateur if UtilisateurDao().modifier(utilisateur) else None

    @staticmethod
    @log
    def supprimer(utilisateur: Utilisateur) -> bool:
        """Supprime le compte d'un utilisateur.

        Parameters
        ----------
        utilisateur : Utilisateur
            Utilisateur dont on veut supprimer le compte.

        Returns
        -------
        bool
            True si le compte a bien été supprimé.        
        """
        return UtilisateurDao().supprimer(utilisateur)

    @staticmethod
    @log
    def nom_utilisateur_deja_utilise(nom_utilisateur: str) -> bool:
        """Vérifie si le nom_utilisateur est déjà utilisé.

        Parameters
        ----------
        nom_utilisateur : str
            Nom de l'utilisateur à vérifier.

        Returns
        -------
        bool
            True si le nom de l'utilisateur existe déjà dans
            la base de données.
        """
        utilisateurs = UtilisateurDao().lister_tous()
        return nom_utilisateur in [u.nom_utilisateur for u in utilisateurs]

    @staticmethod
    @log
    def afficher_tous() -> str:
        """Afficher tous les utilisateurs.

        Parameters
        ----------
        None

        Returns
        -------
        str
            Chaîne de caractères mise sous forme de tableau.
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
