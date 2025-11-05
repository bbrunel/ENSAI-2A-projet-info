import logging

from utils.singleton import Singleton
from utils.log_decorator import log

from dao.db_connection import DBConnection

from business_object.ingredient import Ingredient


class IngredientUtilisateurDao(metaclass=Singleton):


    @log
    def ajouter(self, ingredient):
        """Creation d'un ingredient dans la base de données

        Parameters
        ----------
        ingredient : Ingredient

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
                        """
                        INSERT INTO have (id_ingredient, id_utilisateur) VALUES
                            (%(id_ingredient)s, %(id_utilisateur)s) 
                            RETURNING id_ingredient;                                                
                        """,
                        {
                            "id_ingredient": ingredient.id_ingredient,
                            "id_utilisateur": utilisateur.id_utilisateur
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
    def supprimer(self, ingredient):
        """Suppression d'un ingrédient dans le bar personnel.

        Parameters
        ----------
        ingredient : Ingredient
            ingredient à supprimer de la base de données

        Returns
        -------
            True si le ingredient a bien été supprimé
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    # Supprimer le compte d'un ingredient
                    cursor.execute(
                        """
                        DELETE FROM have
                            WHERE id_ingredient=%(id_ingredient)s
                              AND id_utilisateur=%(id_utilisateur)s
                        """,
                        {
                            "id_ingredient": ingredient.id_ingredient,
                            "id_utilisateur": utilisateur.id_utilisateur
                        },
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)
            raise

        return res > 0


    @log
    def lister_tous(self):
        """Lister tous les ingredients.

        Parameters
        ----------
        None

        Returns
        -------
        liste_ingredients : list[Ingredient]
            renvoie la liste de tous les ingredients dans la base de données
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        """
                        SELECT h.id_ingredient, i.nom, i.desc, i.type, i.alcoolise, i.abv
                          FROM have h
                          LEFT JOIN ingredient i ON h.id_ingredient = i.id_ingredient ;
                        """
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
                    nom=row["nom"],
                    desc=row["desc"],
                    type=row["type"],
                    alcoolise=row["alcoolise"],
                    abv=row["abv"],
                )

                liste_ingredients.append(ingredient)

        return liste_ingredients
