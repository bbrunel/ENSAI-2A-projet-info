from ingredient import Ingredient


class IngredientService(metaclass=Singleton):
    """
    """

    def ajout_ingredient(str:str) -> Ingredient: # vérifier le type de l'entrée
        """Ajoute un ingrédient.

        Parameters
        ----------
        str: str
            Nom de l'ingrédient à ajouter.
        
        Return
        ------
        Ingredient
            Ingrédient ajouté.
        """
        IngredientDao.ajouter_ingredient(str)

    def supprimer_ingredient(ingredient:Ingredient) -> bool:
        """Supprimer un ingrédient.
        
        Parameters
        ----------
        ingredient: Ingredient
            L'ingrédient à supprimer

        Return
        ------
        bool
            True si l'ingrédient a bien été supprimé.
        """
        pass

    def verifier_ingredient(id:int) -> Ingredient:
        """Vérifier qu'un ingrédient existe.

        Parameters
        ----------
        id: int
            Identifiant de l'ingrédient. ???

        Return
        ------
        """
        