from src.business_object.cocktail import Cocktail

##############################################################
##############################################################
from src.dao.favoris_dao import FavorisDAO
from src.service.recherche_service import RechercheService


##########################################################################
#######################################################################
class FavorisService:
    """
    Classe service pour les fonctions liées aux cocktails favoris

    """

    def __init__(self, favorite_dao: FavoriteDAO):
        """
        Initialise la classe FavoriteService avec le résultat d'une base de données issue d'un curseur

        """
        self.fav_dao = FavoriteDAO

    def aj_fav_cocktail(self, id_utilisateur : int, id_cocktail : int) -> Cocktail:
        """
        Ajoute un cocktail aux favoris de l'utilisateur

        Paramètres
        ----------
        id _utilisateur : int
            id de l'utilisateur voulant ajouter un favori
        id_cocktail : int
            id du cocktail à ajouter en tant que favori

        Retour
        ----------
        Renvoie le cocktail mis en favoris
        """
        if id_cocktail is not int:
            raise TypeError("id indiquée non conforme au format.")
        id_validation = RechercheService().recherche_cocktail(id=id_cocktail)
        if id_validation is None:
            raise ValueError("Aucun cocktail ne possède cet id.")
        ajout = FavorisDAO().aj_fav(id_utilisateur, id_cocktail)
        if ajout is False:
            raise ValueError("Ce cocktail est déjà en favori pour vous.")
        return id_validation

    def suppr_fav_cocktail(self, id_utilisateur: int, id_cocktail: int):
        """
        retire un cocktail des favoris de l'utilisateur

        Paramètres
        ----------
        id_utilisateur : int
            id de l'utilisateur qui demande à supprimer un de ses favoris
        id_cocktail : int
            id du cocktail que l'utilisateur veut supprimer

        Retour
        ----------
        Renvoie le cocktail supprimé
        """
        if id_cocktail is not int:
            raise TypeError("id indiquée non conforme au format")
        suppression = FavorisDAO().suppr_fav(id_utilisateur, id_cocktail)
        if suppression is False:
            raise ValueError("Pas de cocktail correspondant parmi les favoris")
        return suppression

    def list_all_fav_cocktails(self, id_utilisateur: int) -> list[Cocktail]:
        """
        Liste l'ensemble des cocktails mis en favoris par l'utilisateur

        Paramètres
        ----------
        id_utilisateur : int
            id de l'utilisateur qui veut consulter ses favoris

        Retour
        ----------
        Renvoie la liste des cocktails msi en favoris par l'utilisateur
        """
        favoris = FavorisDAO().lister_ts_fav(id_utilisateur)
        if favoris is None:
            raise ValueError("Pas de cocktail parmi les favoris")
        return favoris
