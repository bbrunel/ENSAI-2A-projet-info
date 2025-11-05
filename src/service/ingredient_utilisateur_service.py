from business_object.utilisateur import Utilisateur

from business_object.ingredient import Ingredient

from utils.singleton import Singleton

class IngredientUtilisateurService(metaclass=Singleton):
    """Fait le lien entre les ingrédients et les utilisateurs.
    """

    def ajout_ingredient_utilisateur(self, utilisateur: Utilisateur, ingredient: Ingredient) -> Ingredient:
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
        id_utilisateur = utilisateur["id"]
        id_ingredient = ingredient["id"]
        return ingredient if IngredientUtilisateurDao().ajouter(id_utilisateur, id_ingredient) else None


    def supprimer_ingredient_utilisateur(self, utilisateur: Utilisateur, ingredient: Ingredient) -> bool: 
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
        id_utilisateur = utilisateur["id"]
        id_ingredient = ingredient["id"]
        return IngredientUtilisateurDao().supprimer(id_utilisateur, id_ingredient)

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
        id_utilisateur = utilisateur["id"]
        return IngredientUtilisateurDao().lister_tous(id_utilisateur)