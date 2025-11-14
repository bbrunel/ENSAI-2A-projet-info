# importer le mock

import logging

from utils.singleton import Singleton
from utils.log_decorator import log

from dao.db_connection import DBConnection

from business_object.ingredient import Ingredient


class IngredientUtilisateurDao(metaclass=Singleton):

    @log
    def ajouter(self, id_utilisateur, id_ingredient) -> Ingredient:
        """Creation d'un ingredient dans le bar personnel.

        Parameters
        ----------
        id_utilisateur : int
        id_ingredient : int

        Returns
        -------
        Ingredient
        """

        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        """
                        INSERT INTO have (id_user, id_ingredient) VALUES
                            (%(id_utilisateur)s, %(id_ingredient)s)
                          RETURNING id_ingredient ;
                        """,
                        {
                            "id_utilisateur": id_utilisateur,
                            "id_ingredient": id_ingredient
                        },
                    )
                    res = cursor.fetchone()
                    res = res["id_ingredient"]
        except Exception as e:
            logging.info(e)

        return res

    @log
    def supprimer(self, id_utilisateur, id_ingredient) -> bool:
        """Suppression d'un ingrédient dans le bar personnel.

        Parameters
        ----------
        id_utilisateur : int
            Identifiant de l'utilisateur qui supprime un ingrédient de son
            bar personnel.
        id_ingredient : int
            Identifiant de l'ingredient à supprimer du bar personnel de
            l'utilisateur.

        Returns
        -------
            True si l'ingredient a bien été supprimé.
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    # Supprimer le compte d'un ingredient
                    cursor.execute(
                        """
                        DELETE
                            FROM have
                            WHERE id_ingredient=%(id_ingredient)s
                              AND id_user=%(id_utilisateur)s
                        """,
                        {
                            "id_ingredient": id_ingredient,
                            "id_utilisateur": id_utilisateur
                        },
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)
            raise

        return res > 0

    @log
    def lister_tous(self, id_utilisateur) -> list[Ingredient]:  # SQL vérifié
        """Lister tous les ingredients du bar personnel de l'utilisateur.

        Parameters
        ----------
        id_utilisateur: int
            L'identifiant de l'utilisateur dont on veut lister le
            bar personnel.

        Returns
        -------
        liste_ingredients : list[Ingredient]
            renvoie la liste de tous les ingredients du bar personnel de
            l'utilisateur
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        """
                        SELECT *
                            FROM have h
                            LEFT JOIN ingredients i
                                ON h.id_ingredient = i.id_ingredient
                            WHERE h.id_user=%(id_utilisateur)s;
                        """,
                        {
                            "id_utilisateur": id_utilisateur
                        }
                    )
                    res = cursor.fetchall()

        except Exception as e:
            logging.info(e)
            raise

        liste_ingredients = []

        if res:
            for row in res:
                ingredient = Ingredient(
                    id=row["id_ingredient"],
                    nom=row["ingredient_name"],
                    desc=row["description"],
                    type_ing=row["ingredient_type"],
                    alcoolise=row["alcoholic"],
                    abv=row["abv"],
                )

                liste_ingredients.append(ingredient)

        return liste_ingredients
