from business_object.ingredient import Ingredient

from dao.ingredient_dao import IngredientDao

from utils.singleton import Singleton

class IngredientService(metaclass=Singleton):
    """
    """

    @log
    def ajout_ingredient(self, nom: str, desc: str, type_ing: str, alcoolise: bool, abv: int) -> Ingredient: # vérifier le type de l'entrée
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
        nouvel_ingredient = Ingredient(
            id=id,
            nom=nom,
            desc=desc,
            type_ing=type_ing,
            alcoolise=alcoolise,
            abv=abv
        )

        return nouvel_ingredient if IngredientDao().ajouter(nouvel_ingredient) else None

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
            id de l'ingrédient à vérifier.

        Return
        ------
        """
        pass