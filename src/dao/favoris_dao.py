import logging

from utils.singleton import Singleton
from dao.db_connection import DBConnection
from utils.log_decorator import log

from business_object.cocktail import Cocktail
from src.service.recherche_service import RechercheService

class FavorisDAO:
    """
    Classe DAO regroupant les méthodes utiles à la gestion des favoris
    """

    def aj_fav(self, id_utilisateur : int, id_cocktail : int) -> bool:
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
                        "INSERT INTO favorites(id_user, id_recipe) VALUES        "
                        "(%(id_user)s, %(id_recipe)s);                           ",
                        {
                            "id_user": id_utilisateur,
                            "id_recipe": id_cocktail,
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)

        fav_ajoute = False
        if res:
            fav_ajoute = True

        return fav_ajoute

    def suppr_fav(self, id_utilisateur : int, id_cocktail : int) -> bool:
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
                        {
                            "id_user": id_utilisateur,
                            "id_recipe": id_cocktail},
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e) 

        return res > 0
        
    def lister_ts_fav(self, id_utilisateur : int ) -> list[Cocktail]:
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
                        "SELECT id_recipe                              "
                        "  FROM favorites                              "
                        "  WHERE id_user = %(id_user)s;                ",
                        {
                            "id_user": id_utilisateur},
                    )
                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise

        list_fav = []

        if res:
            for ligne in res:
                cocktail_sorti = RechercheService().recherche_cocktail(id=ligne)
                cocktail = Cocktail(
                    id=cocktail_sorti["id"],
                    nom=cocktail_sorti["nom"],
                    nom_alt=cocktail_sorti["nom_alt"],
                    tags=cocktail_sorti["tags"],
                    categorie=cocktail_sorti["categorie"],
                    iba=cocktail_sorti["iba"],
                    alcolise=cocktail_sorti["alcolise"],
                    verre=cocktail_sorti["verre"],
                    instructions=cocktail_sorti["instructions"],
                    url_image=cocktail_sorti["url_image"],
                )

                list_fav.append(cocktail)

        return list_fav