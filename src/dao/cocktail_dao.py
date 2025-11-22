import logging

from business_object.cocktail import Cocktail
from business_object.filtre_ingredient import FiltreIngredient
from business_object.ingredient import Ingredient
from dao.db_connection import DBConnection
from service.recherche_service import RechercheService
from utils.log_decorator import log


class CocktailDAO:
    """
    Classe DAO regroupant les méthodes utiles à la gestion des cocktails

    Methodes
    ----------
        ingredients_ckt
        nb_cocktails
        verifier_cocktail
        list_ts_cocktails
    """

    @log
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
                filtre = FiltreIngredient(id=ligne["id_ingredient"])
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

    @log
    def nb_cocktails(self) -> int:
        res = None

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

        if res:
            res = res["count"]

        return res

    @log
    def verifier_cocktail(self, id_cocktail: int) -> Cocktail:
        res = None
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT * FROM cocktails WHERE id_recipe = %(id)s;", {"id": id_cocktail}
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)

        cocktail = None
        if res:
            cocktail = Cocktail(
                id=res["id_recipe"],
                nom=res["recipe_name"],
                categorie=res["category"],
                iba=res["iba_category"],
                alcoolise=res["alcoholic"],
                verre=res["glass_type"],
                instructions=res["instruction"],
                url_image=res["cocktail_pic_url"],
            )
        return cocktail

    @log
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
        # return RechercheService().recherche_cocktail()
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
                    id=row["id_recipe"],
                    nom=row["recipe_name"],
                    categorie=row["category"],
                    iba=row["iba_category"],
                    alcoolise=row["alcoholic"],
                    verre=row["glass_type"],
                    instructions=row["instruction"],
                    url_image=row["cocktail_pic_url"],
                )
                liste_cocktails.append(cocktail)
        return liste_cocktails
