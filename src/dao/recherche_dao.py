import logging

from business_object.cocktail import Cocktail
from business_object.filtre_cocktail import FiltreCocktail
from business_object.filtre_ingredient import FiltreIngredient
from business_object.ingredient import Ingredient
from dao.db_connection import DBConnection
from utils.singleton import Singleton


class RechercheDao(metaclass=Singleton):
    """
    Classe DAO regroupant les méthodes permettant de chercher ingrédients et cocktails dans la
    base de données
    """

    def recherche_cocktail(self, filtre: FiltreCocktail = None) -> list[Cocktail]:
        """Récupère dans la base de données la liste des cocktails satisfaisant un filtre

        Parameters
        ----------
            filtre : FiltreCocktail = None

        Returns
        -------
            cocktails : list[Cocktail]
        """

        res = None
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    query = "SELECT * FROM cocktails WHERE 1=1"
                    params = []

                    if filtre.id is not None:
                        query += " AND id_recipe = %s"
                        params.append(filtre.id)

                    if filtre.nom is not None:
                        query += " AND similarity(LOWER(recipe_name), LOWER(%s)) > 0.5"
                        params.append(filtre.nom)

                    if filtre.alcoolise is not None:
                        query += " AND alcoholic = %s"
                        params.append(filtre.alcoolise)

                    if filtre.iba is not None:
                        query += " AND iba_category = %s"
                        params.append(filtre.iba)

                    if filtre.categorie is not None:
                        query += " AND category = %s"
                        params.append(filtre.categorie)

                    if filtre.verre is not None:
                        query += "AND glass_type = %s"
                        params.append(filtre.verre)

                    cursor.execute(query, params)
                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)

        liste_cocktails = []
        if res:
            for row in res:
                cocktail = Cocktail(
                    row["id_recipe"],
                    row["recipe_name"],
                    None,
                    None,
                    row["category"],
                    row["iba_category"],
                    row["alcoholic"],
                    row["glass_type"],
                    row["instruction"],
                    row["cocktail_pic_url"],
                )
                liste_cocktails.append(cocktail)
        return liste_cocktails

    def cocktails_faisables(self, id_ingredients: list[int], nb_manquants: int = 0) -> list[Cocktail]:
        """Cette fonction récupère dans la base de données la liste des cocktails
        faisables (ou quasi-faisable si nb_manquants > 0) avec une liste d'ingrédients donnés.

        Parameters
        ----------
            id_ingredients: list[int]
                liste des identifiants des ingrédients possédés
            nb_manquants: int
                nombre maximum d'ingrédients supplémentaires
                entrant dans la composition du cocktail
        Returns
        -------
            liste_cocktails: list[Cocktail]
                Liste des Cocktail faisables
        """
        res = None
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    # La requete cherche dans la table composition les couple cocktail/ingredient
                    # dont l'ingredient n'est PAS dans la liste des ingredients possédés, ensuite
                    # on garde uniquement les cocktails dont le nombre d'occurence (donc le nombre
                    # d'ingredient supplementaire à utiliser) est inférieur à nb_manquants.
                    if nb_manquants > 0:
                        query = (
                            "SELECT c1.*, count(*) as nb_missing FROM cocktails c1"
                            " JOIN composition c2 ON c1.id_recipe = c2.id_recipe"
                            " WHERE NOT c2.id_ingredient IN %(liste_ing)s"
                            " GROUP BY c1.id_recipe HAVING count(*) <= %(nb_max)s"
                            " ORDER BY nb_missing;"
                        )
                        params = {
                                    "liste_ing": tuple(id_ingredients),
                                    "nb_max": nb_manquants
                                 }

                    else:
                        query = (
                            "SELECT c1.*, count(*) as n FROM cocktails c1"
                            " JOIN composition c2 ON c1.id_recipe = c2.id_recipe"
                            " WHERE c2.id_ingredient IN %(liste_ing)s"
                            " GROUP BY c1.id_recipe HAVING c1.id_recipe NOT IN"
                            " (SELECT c1.id_recipe FROM cocktails c1"
                            " JOIN composition c2 ON c1.id_recipe = c2.id_recipe "
                            " WHERE NOT c2.id_ingredient IN %(liste_ing)s "
                            " GROUP BY c1.id_recipe);"
                        )
                        params = {"liste_ing" : tuple(id_ingredients)}
                    cursor.execute(query, params)
                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)

        liste_cocktails = []
        if res:
            for row in res:
                cocktail = Cocktail(
                    row["id_recipe"],
                    row["recipe_name"],
                    None,
                    None,
                    row["category"],
                    row["iba_category"],
                    row["alcoholic"],
                    row["glass_type"],
                    row["instruction"],
                    row["cocktail_pic_url"],
                )
                liste_cocktails.append(cocktail)
        return liste_cocktails

    def recherche_ingredient(self, filtre: FiltreIngredient = None) -> list[Ingredient]:
        """Cette fonction cherche dans la base de données les ingrédients correspondants au filtre

        Parameters
        ----------
            filtre: FiltreIngredient = None

        Returns
        -------
            liste_ingredients: list[Ingredient]
        """
        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    query = "SELECT * FROM ingredients WHERE 1=1"
                    params = {}

                    if filtre.id is not None:
                        query += " AND id_ingredient = %s"
                        params["id"] = filtre.id

                    if filtre.nom is not None:
                        query += " AND similarity(LOWER(ingredient_name), LOWER(%(name)s)) > 0.5"
                        params["name"] = filtre.nom

                    if filtre.alcoolise is not None:
                        query += " AND alcoholic = %(alcoolise)s"
                        params["alcoolise"] = filtre.alcoolise

                    if filtre.type_ing is not None:
                        query += " AND ingredient_type = %(type)s"
                        params["type"] = filtre.type_ing
                    cursor.execute(query, params)
                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)

        liste_ingredients = []
        if res:
            for row in res:
                ingredient = Ingredient(
                    row["id_ingredient"],
                    row["ingredient_name"],
                    row["description"],
                    row["ingredient_type"],
                    row["alcoholic"],
                    row["abv"],
                )
                liste_ingredients.append(ingredient)
        return liste_ingredients

