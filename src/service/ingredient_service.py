from business_object.ingredient import Ingredient
from dao.ingredient_dao import IngredientDao
from src.service.recherche_service import RechercheService

from utils.log_decorator import log
from utils.singleton import Singleton


class IngredientService(metaclass=Singleton):
    """
    """

    @log
    def ajout_ingredient(
        self,
        nom: str,
        desc: str,
        type_ing: str,
        alcoolise: bool,
        abv: int
    ) -> Ingredient:
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

    def supprimer_ingredient(ingredient: Ingredient) -> bool:
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
        return IngredientDao().supprimer(ingredient)

    def verifier_ingredient(id_ingredient: int) -> Ingredient:
        """Vérifier qu'un ingrédient existe.

        Parameters
        ----------
        id: int
            id de l'ingrédient à vérifier.

        Return
        ------
        """
        if id_ingredient is not int:
            raise TypeError("L'id indiquée n'est pas conforme au format.")
        ingredient = RechercheService().recherche_ingredient(id=id_ingredient)
        if ingredient is None:
            raise ValueError("Pas d'ingrédient correspondant à cet id.")
