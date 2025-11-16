from business_object.ingredient import Ingredient
from business_object.filtre_ingredient import FiltreIngredient
from dao.ingredient_dao import IngredientDao
from service.recherche_service import RechercheService

from utils.log_decorator import log
from utils.singleton import Singleton


class IngredientService(metaclass=Singleton):
    """Gère les ingrédients de la base de données.

    Methods
    -------
    ajout_ingredient
    supprimer_ingredient
    verifier_ingredient
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
        nom : str
            Nom de l'ingrédient à ajouter.
        desc : str
            Description de l'ingrédient à ajouter.
        type_ing : str
            Type de l'ingrédient à ajouter.
        alcoolise : bool
            Si l'ingrédient à ajouter est alcoolisé.
        abv : int
            Degré d'alcool de l'ingrédient à ajouter si alcoolisé.

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
        if IngredientDao().ajouter(nouvel_ingredient):
            return nouvel_ingredient
        else:
            return None

    def supprimer_ingredient(self, ingredient: Ingredient) -> bool:
        """Supprimer un ingrédient.

        Parameters
        ----------
        ingredient : Ingredient
            L'ingrédient à supprimer.

        Return
        ------
        bool
            True si l'ingrédient a bien été supprimé.
        """
        id_ingredient = ingredient.id
        return IngredientDao().supprimer(id_ingredient)

    def verifier_ingredient(self, id_ingredient: int) -> Ingredient:
        """Vérifie qu'un ingrédient existe déjà dans la base de données.

        Permet de connaître les autres informations de l'ingrédient à
        partir de son id.

        Parameters
        ----------
        id_ingredient : int
            id de l'ingrédient à vérifier.

        Return
        ------
        Ingredient
        """
        
        if not isinstance(id_ingredient, int):
            raise TypeError("L'id indiquée n'est pas conforme au format.")

        filtre = FiltreIngredient(id=id_ingredient)
        ingredient_liste = RechercheService().recherche_ingredient(filtre)
    
        if ingredient_liste == []:
            ingredient = None
            raise ValueError("Pas d'ingrédient correspondant à cet id.")
    
        print("Ce que retourne ingredient_liste :", ingredient_liste)
        ingredient = ingredient_liste[0]

        return ingredient
