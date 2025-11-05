import logging

from utils.singleton import Singleton
from utils.log_decorator import log

from dao.db_connection import DBConnection

from business_object.ingredient import Ingredient


class IngredientUtilisateurDao(metaclass=Singleton):


    @log
    def ajouter(self, id_utilisateur, id_ingredient): # SQL vérifié
        """Creation d'un ingredient dans le bar personnel.

        Parameters
        ----------
        id_utilisateur : int
        id_ingredient : int

        Returns
        -------
        created : bool
            True si la création est un succès.
            False sinon.
        """

        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        """
                        INSERT INTO have (id_ingredient, id_user) VALUES
                            (%(id_ingredient)s, %(id_utilisateur)s) 
                            RETURNING id_ingredient;                                                
                        """,
                        {
                            "id_ingredient": id_ingredient,
                            "id_utilisateur": id_utilisateur
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)

        created = False
        if res:
            ingredient.id_ingredient = res["id_ingredient"]
            created = True

        return created


    @log
    def supprimer(self, id_utilisateur, id_ingredient):
        """Suppression d'un ingrédient dans le bar personnel.

        Parameters
        ----------
        id_utilisateur : int
            Identifiant de l'utilisateur qui supprime un ingrédient de son bar personnel.
        id_ingredient : int
            Identifiant de l'ingredient à supprimer du bar personnel de l'utilisateur.

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
    def lister_tous(self, id_utilisateur): # SQL vérifié
        """Lister tous les ingredients du bar personnel de l'utilisateur.

        Parameters
        ----------
        id_utilisateur: int
            L'identifiant de l'utilisateur dont on veut lister le bar personnel.

        Returns
        -------
        liste_ingredients : list[Ingredient]
            renvoie la liste de tous les ingredients du bar personnel de l'utilisateur
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        """
                        SELECT *
                            FROM have h
                            LEFT JOIN ingredients i ON h.id_ingredient = i.id_ingredient 
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
                    id_ingredient=row["id_ingredient"],
                    nom=row["ingredient_name"],
                    desc=row["description"],
                    type=row["ingredient_type"],
                    alcoolise=row["alcoholic"],
                    abv=row["abv"],
                )

                liste_ingredients.append(ingredient)

        return liste_ingredients
