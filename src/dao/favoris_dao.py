import logging

from business_object.favori import Favori
from dao.db_connection import DBConnection


class FavorisDAO:
    """
    Classe DAO regroupant les méthodes utiles à la gestion des favoris
    """

    def aj_fav(self, id_utilisateur: int, id_cocktail: int, note_perso: str = None) -> bool:
        """
        Creation d'un favori dans la base de données

        Paramètres
        ----------
        id_utilisateur : int
            id de l'utilisateur voulant ajouter un favori
        id_cocktail : int
            id du cocktail à mettre en favori

        Retour
        -------
        fav_ajoute: bool
            True si le cocktail a bien été ajouté aux fav
            False sinon
        """

        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO favorites(id_user, id_recipe, note) VALUES "
                        "(%(id_user)s, %(id_recipe)s, %(note)s) RETURNING id_recipe;",
                        {
                            "id_user": id_utilisateur,
                            "id_recipe": id_cocktail,
                            "note": note_perso,
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)

        fav_ajoute = False
        if res:
            fav_ajoute = True

        return fav_ajoute

    def suppr_fav(self, id_utilisateur: int, id_cocktail: int) -> bool:
        """
        Méthode servant à supprimer un cocktail des favoris d'un utilisateur

        Paramètres
        ----------
        id_utilisateur : int
            id de l'utilisateur souhaitant supprimer un de ses favoris
        id_cocktail : int
            id du cocktail à supprimer des favoris

        Retour
        -------
            True si le favori a bien été supprimé pour l'utilisateur
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "DELETE FROM favorites                  "
                        " WHERE id_user = %(id_user)s           "
                        "   AND id_recipe = %(id_recipe)s;      ",
                        {"id_user": id_utilisateur, "id_recipe": id_cocktail},
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)

        return res > 0

    def supprimer_tous(self, id_utilisateur: int) -> bool:
        """
        Méthode servant à supprimer tous les cocktails des favoris d'un utilisateur

        Paramètres
        ----------
        id_utilisateur : int
            id de l'utilisateur souhaitant supprimer un de ses favoris
        Retour
        -------
            True si les favori ont bien été supprimés pour l'utilisateur
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "DELETE FROM favorites                  "
                        " WHERE id_user = %(id_user)s           ",
                        {"id_user": id_utilisateur},
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)

        return res > 0

    def lister_ts_fav(self, id_utilisateur: int) -> list[Favori]:
        """
        Méthode servant à lister l'intégralité des favoris d'un utilisateur

        Paramètres
        ----------
        id_utilisateur : int
            id de l'utilisateur voulant consulter ses favoris

        Retour
        -------
        list_fav : list[Cocktail]
            La liste de tous les cocktails dans les favoris de l'utilisateur
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT * FROM cocktails c JOIN favorites f ON c.id_recipe = f.id_recipe "
                        "WHERE id_user = %(id_user)s;",
                        {"id_user": id_utilisateur},
                    )
                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise

        list_fav = []

        if res:
            for ligne in res:
                cocktail = Favori(
                    id=ligne["id_recipe"],
                    nom=ligne["recipe_name"],
                    nom_alt=None,
                    tags=None,
                    categorie=ligne["category"],
                    iba=ligne["iba_category"],
                    alcolise=ligne["alcoholic"],
                    verre=ligne["glass_type"],
                    instructions=ligne["instruction"],
                    url_image=ligne["cocktail_pic_url"],
                    note_perso=ligne["note"],
                )

                list_fav.append(cocktail)

        return list_fav
