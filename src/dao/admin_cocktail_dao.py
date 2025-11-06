import logging

from dao.db_connection import DBConnection


class AdminCocktailDAO:
    """
    Classe DAO regroupant les méthodes uniquement disponible pour les admins
    """

    def ajouter_ckt(
        self,
        nom: str,
        tags: list[str],
        categorie: str,
        iba: str,
        alcolise: bool,
        verre: str,
        instructions: str,
        url_image: str = None,
    ) -> int:
        """
        Creation d'un cocktail dans la base de données

        Paramètres
        ----------
        nom : str
            nom usuel d'un cocktail
        tags : str
            Les tags attribués au cocktail
        categorie : str
            catégorie du cocktail
        iba : str
            type de cocktail considéré par l'IBA (the International Bartender Association)
        alcolise : bool
            booléen indiquant si le cocktail contient de l'alcool
        verre : str
            type de verre utilisé pour faire le cocktail
        instructions : str
            instructions pour réaliser le cocktail
        url_image : str
            potentielle image d'illustration du cocktail

        Retour
        -------
        id_cocktail : int
            l'id du cocktail créé
        """

        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO cocktails(recipe_name, category, alcoholic,    "
                        "glass_type, instruction,                                   "
                        "iba_category,cocktail_pic_url) VALUES                      "
                        "(%(recipe_name)s, %(category)s, %(alcoholic)s,             "
                        " %(glass_type)s,%(instruction)s,                           "
                        " %(iba_category)s, %(cocktail_pic_url)s)                   "
                        "RETURNING id_recipe;                                       ",
                        {
                            "recipe_name": nom,
                            "category": categorie,
                            "alcoholic": alcolise,
                            "glass_type": verre,
                            "instruction": instructions,
                            "iba_category": verre,
                            "cocktail_pic_url": url_image,
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)

        if res:
            return res["id_recipe"]






    def suppr_ckt(self, id_cocktail) -> bool:
        """
        Méthode servant à supprimer un cocktail de Cocktail

        Paramètres
        ----------
        id_cocktail : int 
            id du cocktail à supprimer des cocktails

        Retour
        -------
        True si le cocktail a bien été supprimé de la base de données 
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "DELETE FROM cocktail                   "
                        " WHERE id_recipe = %(id_recipe)s;      ",
                        {
                            "id_recipe": id_cocktail},
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e) 

        return res > 0