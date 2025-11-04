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
        cocktail = self.dao.cocktail.lecture(id_cocktail)
        if cocktail is None:
            raise ErreurCocktailPasTrouvé(id_cocktail)
        return cocktail

    def ingredient_cocktail(self, id_cocktail) -> list[Ingrédient]:
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
        return

    def lister_tous_cocktail() -> list[Cocktail]:
        """Lister l'ensemble des cocktails

        Paramètres
        ----------


        Retour
        ----------
        Affiche ErreurCocktailPasTrouvé: si aucun cocktail n'a été trouvé
        Renvoie le cocktail dont on vérifie la présence
        """
        return
