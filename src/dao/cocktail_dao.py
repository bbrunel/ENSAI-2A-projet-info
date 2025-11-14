import logging

from dao.db_connection import DBConnection
from business_object.cocktail import Cocktail
from business_object.ingredient import Ingredient
from business_object.filtre_ingredient import FiltreIngredient
from service.recherche_service import RechercheService


class CocktailDAO:
    """
    Classe DAO regroupant les méthodes utiles à la gestion des cocktails
    """

    def ingredients_ckt(self, id_cocktail) -> list[Ingredient]:
        """
        Méthode servant à regarder les ingrédients dans un cocktail


        Paramètres
        ----------
        id_cocktail : int
            id du cocktail dont on veut connaitre les ingrédients

        Retour
        -------
        list_ingr : list[Ingredient]
            La liste des ingrédients du cocktail
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT id_ingredient                              "
                        "  FROM composition                              "
                        "  WHERE id_recipe = %(id_user)s;                ",
                        {"id_user": id_cocktail},
                    )
                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise

        list_ingr = []

        if res:
            for ligne in res:
                filtre = FiltreIngredient(id=ligne['id_ingredient'])
                print(filtre)
                ingredient_sorti = RechercheService().recherche_ingredient(filtre)[0]
                ingr = Ingredient(
                    id=ingredient_sorti.id,
                    nom=ingredient_sorti.nom,
                    desc=ingredient_sorti.desc,
                    type_ing=ingredient_sorti.type_ing,
                    alcoolise=ingredient_sorti.alcoolise,
                    abv=ingredient_sorti.abv,
                )

                list_ingr.append(ingr)

        return list_ingr
    

    def nb_cocktails(self) -> int:
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT count(*)                              "
                        "  FROM cocktails                              "
                    )
                    res = cursor.fetchone()

        except Exception as e:
            logging.info(e)
            raise
        return res['count']

    def list_ts_cocktails(self) -> list[Cocktail]:
        """
        Méthode servant à obtenir la liste complète des cocktails


        Paramètres
        ----------


        Retour
        -------
        list_tt_ckt : list[Cocktail]
            La liste de tous les cocktails
        """
        #return RechercheService().recherche_cocktail()
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                             "
                        "  FROM cocktails                              "
                    )
                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise

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