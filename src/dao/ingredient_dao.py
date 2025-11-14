import logging

from utils.singleton import Singleton
from utils.log_decorator import log

from dao.db_connection import DBConnection

from business_object.ingredient import Ingredient

class IngredientDao(metaclass=Singleton):
    """Classe contenant les méthodes pour accéder aux ingrédients de la
    base de données.

    """

    @log
    def ajouter(self, ingredient: Ingredient) -> Ingredient | None:

        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        """
                        INSERT INTO ingredients(
                            ingredient_name,
                            ingredient_type,
                            description,
                            alcoholic,
                            abv
                        )
                        VALUES (
                            %(nom)s,
                            %(desc)s,
                            %(type)s,
                            %(alcoolise)s,
                            %(abv)s
                        )
                          RETURNING id_ingredient ;
                        """,
                        {
                            "nom": ingredient.nom,
                            "desc": ingredient.desc,
                            "type": ingredient.type_ing,
                            "alcoolise": ingredient.alcoolise,
                            "abv": ingredient.abv
                        },
                    )
                    res = cursor.fetchone()
                    res = res["id_ingredient"]
        except Exception as e:
            logging.info(e)

        return res


    def supprimer(self, ingredient: Ingredient) -> bool:

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
