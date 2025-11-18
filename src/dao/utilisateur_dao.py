import logging

from business_object.utilisateur import Utilisateur
from dao.db_connection import DBConnection
from utils.log_decorator import log
from utils.singleton import Singleton


class UtilisateurDao(metaclass=Singleton):
    """Classe contenant les méthodes pour accéder aux Utilisateurs de la base de données"""

    @log
    def creer(self, utilisateur) -> bool:
        """Création d'un utilisateur dans la base de données

        Parameters
        ----------
        utilisateur : Utilisateur

        Returns
        -------
        created : bool
            True si la création est un succès
            False sinon
        """

        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO users(username, hashed_password) VALUES "
                        "(%(username)s, %(hashed_password)s)                 "
                        "RETURNING id_user;                                  ",
                        {
                            "username": utilisateur.nom_utilisateur,
                            "hashed_password": utilisateur.mdp,
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)

        if res:
            utilisateur.id = res["id_user"]
            return utilisateur
        return None

    @log
    def trouver_par_id(self, id_utilisateur) -> Utilisateur:
        """Trouver un utilisateur grâce à son id

        Parameters
        ----------
        id_utilisateur : int
            numéro id de l'utilisateur que l'on souhaite trouver

        Returns
        -------
        utilisateur : Utilisateur
            renvoie l'utilisateur que l'on cherche par id
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT id_user, username, hashed_password "
                        "FROM users                               "
                        "WHERE id_user = %(id_utilisateur)s;      ",
                        {"id_utilisateur": id_utilisateur},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)
            raise

        utilisateur = None
        if res:
            utilisateur = Utilisateur(
                id=res["id_user"], nom_utilisateur=res["username"], mdp=res["hashed_password"]
            )

        return utilisateur

    @log
    def trouver_par_nom(self, nom_utilisateur) -> Utilisateur:
        """Trouver un utilisateur grâce à son nom d'utilisateur

        Parameters
        ----------
        nom_utilisateur : str
            nom d'utilisateur que l'on souhaite trouver

        Returns
        -------
        utilisateur : Utilisateur
            renvoie l'utilisateur que l'on cherche par nom
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT id_user, username, hashed_password "
                        "FROM users                               "
                        "WHERE username = %(nom_utilisateur)s;    ",
                        {"nom_utilisateur": nom_utilisateur},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)
            raise

        utilisateur = None
        if res:
            utilisateur = Utilisateur(
                id=res["id_user"], nom_utilisateur=res["username"], mdp=res["hashed_password"]
            )

        return utilisateur

    @log
    def lister_tous(self) -> list[Utilisateur]:
        """Lister tous les utilisateurs

        Returns
        -------
        liste_utilisateurs : list[Utilisateur]
            renvoie la liste de tous les utilisateurs dans la base de données
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT id_user, username, hashed_password "
                        "FROM users;                              "
                    )
                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise

        liste_utilisateurs = []

        if res:
            for row in res:
                utilisateur = Utilisateur(
                    id=row["id_user"], nom_utilisateur=row["username"], mdp=row["hashed_password"]
                )
                liste_utilisateurs.append(utilisateur)

        return liste_utilisateurs

    @log
    def modifier(self, utilisateur) -> bool:
        """Modification d'un utilisateur dans la base de données

        Parameters
        ----------
        utilisateur : Utilisateur

        Returns
        -------
        modified : bool
            True si la modification est un succès
            False sinon
        """

        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE users                          "
                        "SET username = %(username)s,          "
                        "    hashed_password = %(hashed_password)s "
                        "WHERE id_user = %(id_user)s;          ",
                        {
                            "username": utilisateur.nom_utilisateur,
                            "hashed_password": utilisateur.mdp,
                            "id_user": utilisateur.id,
                        },
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)

        return res == 1

    @log
    def supprimer(self, utilisateur) -> bool:
        """Suppression d'un utilisateur dans la base de données

        Parameters
        ----------
        utilisateur : Utilisateur
            utilisateur à supprimer de la base de données

        Returns
        -------
            True si l'utilisateur a bien été supprimé
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    # Supprimer d'abord les dépendances (table have et favorites)
                    cursor.execute(
                        "DELETE FROM have                      "
                        "WHERE id_user = %(id_user)s;          ",
                        {"id_user": utilisateur.id},
                    )

                    cursor.execute(
                        "DELETE FROM favorites                 "
                        "WHERE id_user = %(id_user)s;          ",
                        {"id_user": utilisateur.id},
                    )

                    # Puis supprimer l'utilisateur
                    cursor.execute(
                        "DELETE FROM users                     "
                        "WHERE id_user = %(id_user)s;          ",
                        {"id_user": utilisateur.id},
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)
            raise

        return res > 0

    @log
    def se_connecter(self, nom_utilisateur, mdp_hash) -> Utilisateur:
        """Se connecter grâce à son nom d'utilisateur et son mot de passe hashé

        Parameters
        ----------
        nom_utilisateur : str
            nom d'utilisateur de l'utilisateur que l'on souhaite trouver
        mdp_hash : str
            mot de passe hashé de l'utilisateur

        Returns
        -------
        utilisateur : Utilisateur
            renvoie l'utilisateur que l'on cherche
        """
        res = None
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT id_user, username, hashed_password "
                        "FROM users                               "
                        "WHERE username = %(username)s            "
                        "  AND hashed_password = %(mdp_hash)s;    ",
                        {"username": nom_utilisateur, "mdp_hash": mdp_hash},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)

        utilisateur = None

        if res:
            utilisateur = Utilisateur(
                id=res["id_user"], nom_utilisateur=res["username"], mdp=res["hashed_password"]
            )

        return utilisateur
