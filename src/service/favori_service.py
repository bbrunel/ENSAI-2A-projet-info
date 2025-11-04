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
    Service class for the favorite business logic

    
    """
    def __init__(self, favorite_dao : FavoriteDAO):
        """
        Initialize FavoriteService with the result of a database about a cursor 
        """
        self.favdao = FavoriteDAO

    def add_fav_cocktail(self, id_user : int, id_cocktail : int ): 
        self.append(id_user, id_cocktail)

    def remove_fav_cocktail(self,id_user : int, id_cocktail : int):
        pass #besoin de la DAO favorite
    
    def list_all_fav_cocktails(self, id_user : ) -> list[Cocktail]