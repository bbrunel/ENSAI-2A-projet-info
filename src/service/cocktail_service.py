from src.business_object.cocktail import Cocktail
from src.business_object.ingredient import Ingredient
from src.dao.cocktail import CocktailDAO


class CocktailService:
    """
    Classe service pour les cocktails

    """

    def __init__(self, cocktail_dao: CocktailDAO) -> None:
        self.dao.cocktail = cocktail_dao

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
        if id_cocktail is not int:
            raise TypeError("id indiquée non conforme au format")
        cocktail = CocktailDAO().lecture(id_cocktail)
        if cocktail is None:
            raise ValueError("Pas de cocktail correspondant à cet id.")
        return cocktail

    def ingredient_cocktail(self, id_cocktail) -> list[Ingredient]:
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
        if id_cocktail is not int:
            raise TypeError("id indiquée non conforme au format")
        ingredients = CocktailDAO().ingredients_ckt(id_cocktail)
        if ingredients is None:
            raise ValueError("Pas de cocktail correspondant à cet id.")
        return ingredients

    def lister_tous_cocktail() -> list[Cocktail]:
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
