import logging

from utils.singleton import Singleton
from utils.log_decorator import log

from dao.db_connection import DBConnection

from business_object.ingredient import Ingredient


class IngredientUtilisateurDao(metaclass=Singleton):
    def ajouter(self, ingredient):
        """Creation d'un joueur dans la base de données

        Parameters
        ----------
        joueur : Joueur

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
                        INSERT INTO ingredient(nom, desc, type, alcoolise, abv) VALUES
                            (%(nom)s, %(desc)s, %(type)s, %(alcoolise)s, %(abv)s) 
                            RETURNING id;                                                
                        """,
                        {
                            "nom": joueur.pseudo,
                            "desc": joueur.mdp,
                            "type": joueur.age,
                            "alcoolise": joueur.mail,
                            "abv": joueur.fan_pokemon,
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)

        created = False
        if res:
            joueur.id = res["id"]
            created = True

        return created
