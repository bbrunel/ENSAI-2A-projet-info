from utilisateur import Utilisateur
from ingredient import Ingredient

class IngredientUtilisateurService(metaclass=Singleton):
    """Fait le lien entre les ingrédients et les utilisateurs.
    """

    def ajout_ingredient_utilisateur(self, utilisateur: Utilisateur, ingredient: Ingredient) -> Ingredient: # ajouter une quantité ?
        """Ajoute un ingrédient au bar personnel de l'utilisateur.

        Parameters
        ----------
        utilisateur: Utilisateur
            L'utilisateur qui ajoute un ingrédient dans son bar personnel.
        ingredient: Ingredient
            L'ingredient à ajouter dans le bar personnel de l'utilisateur.

        Return
        ------
        ingredient: Ingredient
        """

    def supprimer_ingredient_utilisateur(self, ingredient: Ingredient) -> bool: # ajouter un paramètre quantité ?
        """Supprime un ingrédient du bar personnel de l'utilisateur.

        Parameters
        ----------
        ingredient: Ingredient
            L'ingrédient à supprimer du bar personnel.
        
        Return
        ------
        bool
            True si l'ingrédient a bien été supprimé.
        """
        IngredientUtilisateurDao().supprimer(ingredient)

    def liste_tous_ingredients_utilisateur(self, utilisateur: Utilisateur) -> list[Ingredient]:
        """Liste les ingrédients du bar personnel de l'utilisateur.

        Parameters
        ----------
        utilisateur: Utilisateur
            L'utilisateur dont on veut connaître les ingrédients du bar personnel.
        
        Return
        ------
        liste_ingredients_utilisateur: list[Ingredient]
            La liste des ingrédients du bar personnel.
        """
        liste_ingredients_utilisateur = IngredientUtilisateurDao().lister_tous()
        return liste_ingredients_utilisateur