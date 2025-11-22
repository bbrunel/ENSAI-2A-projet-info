from business_object.ingredient import Ingredient
from dao.ingredient_dao import IngredientDao
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
        self, nom: str, desc: str, type_ing: str, alcoolise: bool, abv: int
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
        nouvel_ing = Ingredient(
            id=id, nom=nom, desc=desc, type_ing=type_ing, alcoolise=alcoolise, abv=abv
        )
        id_nouvel_ing = IngredientDao().ajouter(
            nouvel_ing.nom,
            nouvel_ing.desc,
            nouvel_ing.type_ing,
            nouvel_ing.alcoolise,
            nouvel_ing.abv,
        )
        if id_nouvel_ing:
            return IngredientDao.verifier_ingredient(id_nouvel_ing)

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
        ingredient = IngredientDao().verifier_ingredient(id_ingredient)
        if ingredient is None:
            raise ValueError("ingredient inexistant")
        return ingredient

    def nb_cocktails(self, id_ingredient: int) -> int:
        """Cette méthode renvoit le nombre de cocktails nécessitant un ingrédient.

        Params
        ------
            id_ingredient: int
                L'id d'un ingrédient

        Returns
        -------
            int
                Le nombre de cocktail nécessitant cet ingrédient.
        """
        return IngredientDao().nb_cocktails(id_ingredient)
