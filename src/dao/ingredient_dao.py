import logging

from business_object.ingredient import Ingredient
from dao.db_connection import DBConnection
from utils.log_decorator import log
from utils.singleton import Singleton


class IngredientDao(metaclass=Singleton):
    """Classe contenant les méthodes pour accéder aux ingrédients de la
    base de données.

    """

    @log
    def verifier_ingredient(self, id_ingredient: int) -> Ingredient:
        res = None
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT * FROM ingredients WHERE id_ingredient = %(id_ing)s",
                        {"id_ing": id_ingredient},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)
        if res:
            return Ingredient(
                id=res["id_ingredient"],
                nom=res["ingredient_name"],
                desc=res["description"],
                type_ing=res["ingredient_type"],
                alcoolise=res["alcoholic"],
                abv=res["abv"],
            )
        return None

    @log
    def ajouter(
        self, nom: str, desc: str, type_ing: str, alcoolise: bool, abv: int
    ) -> Ingredient | None:
        """Création d'un ingrédient dans la base de données.

        Parameters
        ----------
        nom : str
            Nom de l'ingrédient à créer.
        desc: str
            Description de l'ingrédient à créer.
        type_ing: str
            Type de l'ingrédient à créer.
        alcoolise: bool
            Si l'ingrédient à créer est alcoolisé.
        abv: int
            Degré d'alcool de l'ingrédient à créer.

        Returns
        -------
        id_ingredient: int
            L'id de l'ingrédient créé.
        """

        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    query = """
                        INSERT INTO ingredients(
                            id_ingredient,
                            ingredient_name,
                            ingredient_type,
                            description,
                            alcoholic,
                            abv
                        )
                        VALUES (
                            (SELECT MAX(id_ingredient) + 1 FROM ingredients),
                            %(nom)s,
                            %(desc)s,
                            %(type)s,
                            %(alcoolise)s,
                            %(abv)s
                        )
                          RETURNING id_ingredient ;
                        """
                    params = {
                        "nom": nom,
                        "desc": desc,
                        "type": type_ing,
                        "alcoolise": alcoolise,
                        "abv": abv,
                    }
                    cursor.execute(query, params)

                    res = cursor.fetchone()

        except Exception as e:
            logging.info(e)

        if res:
            res = res["id_ingredient"]
            print("res:", res)

        return res

    def supprimer(self, id_ingredient: int) -> bool:
        """Supprime un ingrédient de la base de données.

        Parameters
        ----------
        id_ingredient : int
            id de l'ingrédient que l'on souhaite supprimer.

        Returns
        -------
        bool
            Si l'ingrédient a bien été supprimé.
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    # Supprimer le compte d'un ingredient
                    cursor.execute(
                        """
                        DELETE
                            FROM composition
                            WHERE id_ingredient=%(id_ingredient)s;
                        DELETE
                            FROM ingredients
                            WHERE id_ingredient=%(id_ingredient)s;
                        
                        """,
                        {"id_ingredient": id_ingredient},
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)
            raise

        return res > 0

    def id_ing_max(self):
        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    query = """SELECT MAX(id_ingredient) FROM ingredients"""
                    cursor.execute(query)

                    res = cursor.fetchone()

        except Exception as e:
            logging.info(e)
        return res["max"]
