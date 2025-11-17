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
    def ajouter(
        self,
        nom: str,
        desc: str,
        type_ing: str,
        alcoolise: bool,
        abv: int
    ) -> Ingredient | None:

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
                            "nom": nom,
                            "desc": desc,
                            "type": type_ing,
                            "alcoolise": alcoolise,
                            "abv": abv
                        },
                    )
                    res = cursor.fetchone()
                    res = res["id_ingredient"]
        except Exception as e:
            logging.info(e)

        return res

    def supprimer(self, id_ingredient: int) -> bool:

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    # Supprimer le compte d'un ingredient
                    cursor.execute(
                        """
                        DELETE
                            FROM ingredients
                            WHERE id_ingredient=%(id_ingredient)s
                        """,
                        {
                            "id_ingredient": id_ingredient
                        },
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)
            raise

        return res > 0
