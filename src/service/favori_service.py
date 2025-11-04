from src.business_object.cocktail import Cocktail
from src.business_object.utilisateur import 
##############################################################
##############################################################
from src.dao.favorite import FavoriteDAO
from src.utils.exceptions import (
    ItemNotFoundError,
    WrongUserItemError,
)
##########################################################################
#######################################################################
class FavorisService:
    """
    Classe service pour les fonctions liées aux cocktails favoris
    
    """
    def __init__(self, favorite_dao : FavoriteDAO):
        """
        Initialise la classe FavoriteService avec le résultat d'une base de données issue d'un curseur 
        
        """
        self.fav_dao = FavoriteDAO

    def aj_fav_cocktail(self, id_utilisateur : int, id_cocktail : int ) -> Cocktail: 
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
        Affiche DejaFait : si le cocktail en question est déja en favoris pour cet utilisateur

        Renvoie le cocktail mis en favoris
        """
        self.append(id_utilisateur, id_cocktail)

    def suppr_fav_cocktail(self,id_utilisateur : int, id_cocktail : int):
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
        Affiche ErreurCocktailPasTrouvé: si le cocktail n'a pas été trouvé  
        Renvoie le cocktail supprimé
        """
        pass #besoin de la DAO favorite
    
    def list_all_fav_cocktails(self, id_utilisateur : int) -> list[Cocktail]:
        """
        Liste l'ensemble des cocktails mis en favoris par l'utilisateur 

        Paramètres
        ----------
        id_utilisateur : int 
            id de l'utilisateur qui veut consulter ses favoris
        
        Retour
        ----------
        Affiche ErreurCocktailPasTrouvé: si aucun cocktail n'a été trouvé
        Renvoie la liste des cocktails msi en favoris par l'utilisateur 
        """
