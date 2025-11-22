from business_object.utilisateur import Utilisateur
from business_object.ingredient import Ingredient

from dao.ingredient_utilisateur_dao import IngredientUtilisateurDao

from utils.singleton import Singleton


class IngredientUtilisateurService(metaclass=Singleton):
    """Gère le bar personnel des utilisateurs en faisant le lien entre les
    ingrédients et les utilisateurs.

    Methods
    -------
        ajout_ingredient_utilisateur
        supprimer_ingredient_utilisateur
        supprimer_tous
        liste_tous_ingredient_utilisateur
    """

    def ajout_ingredient_utilisateur(
        self,
        utilisateur: Utilisateur,
        ingredient: Ingredient
    ) -> int:
        """Ajoute un ingrédient au bar personnel de l'utilisateur.

        Parameters
        ----------
        utilisateur : Utilisateur
            L'utilisateur qui ajoute un ingrédient dans son bar personnel.
        ingredient : Ingredient
            L'ingredient à ajouter dans le bar personnel de l'utilisateur.

        Return
        ------
        Int
            L'id de l'ingrédient ajouté.
        None
            Si l'ingrédient n'est pas ajouté.
        """
        if not isinstance(utilisateur, Utilisateur):
            raise TypeError("utilisateur de type inadéquate")
        id_utilisateur = utilisateur.id

        if not isinstance(ingredient, Ingredient):
            raise TypeError("ingredient de type inadéquate")
        id_ingredient = ingredient.id

        if IngredientUtilisateurDao().ajouter(
            id_utilisateur,
            id_ingredient
        ) == ingredient.id:
            return ingredient

        else:
            raise ValueError("id non existant")

    def supprimer_ingredient_utilisateur(
        self,
        utilisateur: Utilisateur,
        ingredient: Ingredient
    ) -> bool:
        """Supprime un ingrédient du bar personnel de l'utilisateur.

        Parameters
        ----------
        utilisateur : Utilisateur
            L'utilisateur dont on supprime l'ingrédient du bar personnel.
        ingredient : Ingredient
            L'ingrédient à supprimer du bar personnel.

        Return
        ------
        bool
            True si l'ingrédient a bien été supprimé.
        """
        if not isinstance(utilisateur, Utilisateur):
            raise TypeError("utilisateur de type inadéquate")
        id_utilisateur = utilisateur.id

        if not isinstance(ingredient, Ingredient):
            raise TypeError("ingredient de type inadéquate")
        id_ingredient = ingredient.id
        return IngredientUtilisateurDao().supprimer(
            id_utilisateur,
            id_ingredient
        )

    def supprimer_tous(self, utilisateur: Utilisateur):
        """Supprime de tous les ingrédients dans le bar personnel.

        Parameters
        ----------
        Utilisateur : int
            Utilisateur qui supprime un ingrédient de son bar personnel.

        Returns
        -------
            True si l'ingredient a bien été supprimé.
        """
        if not isinstance(utilisateur, Utilisateur):
            raise TypeError("utilisateur doit être de type Utilisateur")
            
        return IngredientUtilisateurDao().supprimer_tous(utilisateur.id)

    def liste_tous_ingredients_utilisateur(
        self,
        utilisateur: Utilisateur
    ) -> list[Ingredient]:
        """Liste les ingrédients du bar personnel de l'utilisateur.

        Parameters
        ----------
        utilisateur: Utilisateur
            L'utilisateur dont on veut connaître les ingrédients du bar
            personnel.

        Return
        ------
        liste_ingredients_utilisateur: list[Ingredient]
            La liste des ingrédients du bar personnel.
        """
        if not isinstance(utilisateur, Utilisateur):
            raise TypeError("L'utilisateur doit être de type Utilisateur")

        id_utilisateur = utilisateur.id
        return IngredientUtilisateurDao().lister_tous(id_utilisateur)
