from business_object.cocktail import Cocktail
from business_object.ingredient import Ingredient
from dao.cocktail_dao import CocktailDAO
from service.recherche_service import RechercheService
from business_object.filtre_cocktail import FiltreCocktail


class CocktailService:
    """
    Classe service pour les cocktails

    """

    def __init__(self) -> None:
        pass

    def verifier_cocktail(self, id_cocktail: int) -> Cocktail:
        """Vérifie si un cocktail existe bel et bien déjà.

        Paramètres
        ----------
        id_cocktail : l'id du cocktail à vérifier/lire


        Retour
        ----------
        renvoie ErreurCocktailPasTrouvé: si le cocktail n'a pas été trouvé
        retourne le cocktail dont on vérifie la présence
        """
        if not isinstance(id_cocktail, int):
            raise TypeError("id indiquée non conforme au format")

        filtre = FiltreCocktail(id=id_cocktail)
        cocktail = RechercheService().recherche_cocktail(filtre)
        if cocktail is None:
            raise ValueError("Pas de cocktail correspondant à cet id.")
            
        return cocktail

    def ingredient_cocktail(self, id_cocktail: int) -> list[Ingredient]:
        """
        liste des ingrédients composant un cocktail demandé

        Paramètres
        ----------
        id_cocktail : int
            l'id du cocktail dont on veut connaitre les ingrédients

        Retour
        ----------
        Affiche ErreurCocktailPasTrouvé: si le cocktail n'a pas été trouvé
        Renvoie la liste des ingrédients composant le cocktail en question
        """
        if not isinstance(id_cocktail, int):
            raise TypeError("id indiquée non conforme au format")

        ingredients = CocktailDAO().ingredients_ckt(id_cocktail)
        if ingredients is None:
            raise ValueError("Pas de cocktail correspondant à cet id.")

        return ingredients

    def lister_tous_cocktail(self) -> list[Cocktail]:
        """Lister l'ensemble des cocktails

        Paramètres
        ----------


        Retour
        ----------
        Renvoie le cocktail dont on vérifie la présence
        """
        list_cocktails = CocktailDAO().list_ts_cocktails()
        if list_cocktails is None:
            raise ValueError("Pas de cocktail.")
            
        return list_cocktails

    def nb_cocktails(self) -> int:
        """
        
        """
        return CocktailDAO().nb_cocktails()