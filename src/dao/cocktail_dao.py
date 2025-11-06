import logging

from dao.db_connection import DBConnection
from src.business_object.cocktail import Cocktail
from src.business_object.ingredient import Ingredient
from src.service.recherche_service import RechercheService


class CocktailDAO:
    """
    Classe DAO regroupant les méthodes utiles à la gestion des cocktails
    """

    def ingredients_ckt(id_cocktail) -> list[Ingredient]:
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
                        "  WHERE id_recipe = %(id_recipe)s;                ",
                        {"id_user": id_cocktail},
                    )
                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise

        list_ingr = []

        if res:
            for ligne in res:
                ingredient_sorti = RechercheService().recherche_ingredient(id=ligne)
                ingr = Ingredient(
                    id=ingredient_sorti["id"],
                    nom=ingredient_sorti["nom"],
                    desc=ingredient_sorti["desc"],
                    type_ing=ingredient_sorti["type_ing"],
                    alcoolise=ingredient_sorti["alcoolise"],
                    abv=ingredient_sorti["abv"],
                )

                list_ingr.append(ingr)

        return list_ingr

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
        return RechercheService().recherche_cocktail()
