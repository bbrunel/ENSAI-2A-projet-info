import logging

from business_object.cocktail import Cocktail
from business_object.filtre_cocktail import FiltreCocktail
from business_object.ingredient import Ingredient

from utils.singleton import Singleton
from dao.db_connection import DBConnection
from utils.log_decorator import log

class RechercheDao(metaclass=Singleton):
    """
        Classe DAO regroupant les méthodes permettant de chercher ingrédients et cocktails dans la
        base de données
    """

    def recherche_cocktail(self,filtre: FiltreCocktail) -> list[Cocktail]:
        """Récupère dans la base de données la liste des cocktails satisfaisant un filtre

        Parameters
        ----------
            filtre : FiltreCocktail
        
        Returns
        -------
            cocktails : list[Cocktail]
        """

        res = None
        try:
            with DBConnection.connection() as connection:
                with connection.cursor() as cursor:
                    query = "SELECT * FROM cocktail WHERE 1=1"
                    params = []
                    if filtre.nom is not None:
                        query += " AND recipe_name = %s"
                        params.append(filtre.nom)
                    if filtre.alcoolise is not None:
                        query += " AND alcoholic = %s"
                        params.append(filtre.alcoolise)
                    if filtre.iba is not None:
                        query += " AND iba_category = %s"
                        params.append(filtre.iba)
                    if filtre.categorie is not None:
                        query += " AND category = %s"
                        params.append(category)
                    if filtre.verre is not None:
                        query += "AND glass_type = %s"
                        params.append(verre)
                    cursor.execute(query, params)
                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)

        liste_cocktails = []
        if res:
            for row in res:
                cocktail = Cocktail(row['id_recipe'],
                                    row['recipe_name'],
                                    None,None,
                                    row['category'],
                                    row['iba_category'],
                                    row['alcoholic'],
                                    row['glass_type'],
                                    row['instruction'],
                                    row['cocktail_pic_url'])
                liste_cocktails.append(cocktail)
        return liste_cocktails

    def cocktails_faisables(id_ingredients: list[int], nb_manquants: int = 0) -> list[Cocktail]:
        res = None
        try:
            with DBConnection.connection() as connection:
                with connection.cursor() as cursor:
                    query  = "SELECT c1.* as nb_missing FROM cocktails c1"
                    query += " JOIN composition c2 ON c1.id_recipe = c2.id_recipe"
                    query += " WHERE NOT c2.id_ingredient IN %(liste_ing)s"
                    query += " GROUP BY c1.id_recipe HAVING count(*) <= %(nb_max)s ORDER BY nb_missing;"
                    cursor.execute(query,
                                   {
                                    "liste_ing": tuple(id_ingredients),
                                    "nb_max": nb_manquants
                                   })
                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)
        
        liste_cocktails = []
        if res:
            for row in res:
                cocktail = Cocktail(row['id_recipe'],
                                    row['recipe_name'],
                                    None,None,
                                    row['category'],
                                    row['iba_category'],
                                    row['alcoholic'],
                                    row['glass_type'],
                                    row['instruction'],
                                    row['cocktail_pic_url'])
                liste_cocktails.append(cocktail)
        return liste_cocktails
