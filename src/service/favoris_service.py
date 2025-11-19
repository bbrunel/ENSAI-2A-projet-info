from business_object.cocktail import Cocktail

##############################################################
from dao.favoris_dao import FavorisDAO
from service.cocktail_service import CocktailService


#######################################################################
class FavorisService:
    """
    Classe service pour les fonctions liées aux cocktails favoris

    """

    def aj_fav_cocktail(self, id_utilisateur: int, id_cocktail: int) -> Cocktail:
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
        cocktail = CocktailService().verifier_cocktail(id_cocktail)
        ajout = FavorisDAO().aj_fav(id_utilisateur, id_cocktail)
        if not ajout:
            raise ValueError("Ce cocktail est déjà en favori pour vous.")
        return cocktail

    def suppr_fav_cocktail(self, id_utilisateur: int, id_cocktail: int) -> bool:
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
        True si le cocktail a été supprimé
        """
        suppression = FavorisDAO().suppr_fav(id_utilisateur, id_cocktail)
        if suppression is False:
            raise ValueError("Pas de cocktail correspondant parmi les favoris")
        return suppression

    def supprimer_tous(self, id_utilisateur: int) -> bool:
        """
        retire tous les cocktails des favoris de l'utilisateur

        Paramètres
        ----------
        id_utilisateur : int
            id de l'utilisateur qui demande à supprimer un de ses favoris

        Retour
        ------
        True si les cocktails ont été supprimés
        """
        suppression = FavorisDAO().supprimer_tous(id_utilisateur)
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
