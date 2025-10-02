from utilisateur import Utilisateur
from ingredient import Ingredient

class IngredientUtilisateurService(metaclass=Singleton):
    """Fait le lien entre les ingrédients et les utilisateurs.
    """

    def ajout_ingredient_utilisateur(self, utilisateur: Utilisateur, ingredient: Ingredient) -> Ingredient:
        pass

    def supprimer_ingredient_utilisateur(self, ingredient: Ingredient) -> bool:
        pass

    def liste_tous_ingredients_utilisateur(self, utilisateur: Utilisateur) -> list[Ingredient]:
        pass