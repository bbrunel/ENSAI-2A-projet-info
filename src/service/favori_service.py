from cocktail import Cocktail
from user import User
##############################################################
##############################################################
from src.dao.favorite import FavoriteDAO
from src.models import Favorite, FavoriteCreate, FavoriteRegister, FavoriteUpdate
from src.utils.exceptions import (
    ItemNotFoundError,
    WrongUserItemError,
)
##########################################################################
#######################################################################
class FavorisService(Cocktail):
    """
    Classe service pour les fonctions liées aux cocktails favoris
    
    """
    def __init__(self, favorite_dao : FavoriteDAO):
        """
        Initialise la classe FavoriteService avec le résultat d'une base de données issue d'un curseur 
        
        """
        self.favdao = FavoriteDAO

    def add_fav_cocktail(self, id_user : int, id_cocktail : int ): 
        """
        Ajoute un favori
        """
        self.append(id_user, id_cocktail)

    def remove_fav_cocktail(self,id_user : int, id_cocktail : int):
        """
        retire un cocktail des favoris de l'utilisateur 
        pass #besoin de la DAO favorite
    
    def list_all_fav_cocktails(self, id_user : ) -> list[Cocktail]