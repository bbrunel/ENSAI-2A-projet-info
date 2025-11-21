from business_object.filtre_cocktail import FiltreCocktail
from business_object.filtre_ingredient import FiltreIngredient
from business_object.utilisateur import Utilisateur
from dao.recherche_dao import RechercheDao
from service.ingredient_service import IngredientService
from service.ingredient_utilisateur_service import IngredientUtilisateurService


class RechercheService:
    """Permet de rechercher des cocktails et des ingrédients en appliquant un filte de recherche."""

    def __init__(self):
        pass

    def recherche_cocktail(self, filtre: FiltreCocktail = None):
        """Renvoie les cocktails correspondant aux filtres.
        Lève une erreur si aucun cocktail de la base de donnée ne correspond au filtre.

        Parameter
        -------
            filtre: Filtrecocktail
                Les filtres appliqués à la recherche.

        Return
        -------
            list[Cocktail]
                La liste des cocktails correspondant aux filtres.
        """

        if not (isinstance(filtre, FiltreCocktail) or filtre is None):
            raise TypeError("Filtre pas adapté à la recherche de cocktails.")

        cocktails = RechercheDao().recherche_cocktail(filtre)
        if cocktails is None:
            raise ValueError("Pas de cocktail correspondant au filtre.")
        return cocktails

    def recherche_ingredient(self, filtre):
        """Renvoie les ingrédients correspondant aux filtres.
        Lève une erreur si aucun igrédient de la base de donnée ne correspond au filtre.

        Parameter
        -------
            filtre: Filtreingredient
                Les filtres appliqués à la recherche.

        Return
        -------
            list[Ingredient]
                La liste des ingrédients correspondant aux filtres.
        """

        if not isinstance(filtre, FiltreIngredient):
            raise TypeError("Filtre pas adapté à la recherche d'ingrédients")

        ingredients = RechercheDao().recherche_ingredient(filtre)

        if ingredients is None:
            raise ValueError("Pas d'ingrédient correspondant au filtre.")

        return ingredients

    def liste_cocktails_faisables(self, utilisateur: Utilisateur, nb_ing_manquants: int = 0):
        """Renvoie la liste des cocktails faisables ou presque en fonction des ingrédients de
        l'utilisateur.
        Utilise l'utilisateur en argument pour en extraire son inventaire, puis les id des
        ingrédients de son inventaire, pour les donner en argument de la fonction DAO
        correspondante.
        Utilise la fonction de la classe DAO correspondant à la recherche de cocktails faisables.

        Parameter
        -------
            utilisateur: Utilisateur
                L'utilisateur dont l'inventaire est utilisé pour chercher les cocktails faisables.
            nb_ing_manquants: int = 0
                Le nombre d'ingrédient manquant pour réaliser un cocktail proposé.

        Return
        -------
            list[Cocktail]
                La liste des cocktails faisables selon les ingrédients de l'utilisateur et le
                nombre d'ingrédients manquants.
        """

        inventaire = IngredientUtilisateurService().liste_tous_ingredients_utilisateur(utilisateur)
        id_ing_inventaire = [ingredient.id for ingredient in inventaire]

        return RechercheDao().cocktails_faisables(id_ing_inventaire, nb_ing_manquants)

    def recherche_ingredients_optimaux(self, utilisateur: Utilisateur, nb_ing_supp: int = 1):
        """Méthode permettants de trouver une liste d'ingrédients à ajouter à l'inventaire d'un
        utilisateur apportant un grand nombre de cocktails faisables supplémentaires.
        PS:
        Il ne s'agit pas réellement de la liste optimale, on utilise en effet un algorithme glouton,
        le nombre de combinaisons d'ingrédients à tester étant vite beaucoup trop grands
        (environ 10000 pour nb_ing_supp = 2)
        """

        def meilleur_ingredient(a_choisir: list[int], deja_choisis: list[int]):
            meilleur = -1  # Le meilleur ingredient jusqu'à présent
            max_contribution = 0  # Le nombre de coktails ajoutés par le meilleur ingrédient
            for ing in a_choisir:
                contribution = RechercheDao().nb_cocktail_faisables(deja_choisis + [ing])
                if contribution > max_contribution:
                    meilleur = ing
                    max_contribution = contribution
            return meilleur, max_contribution

        if nb_ing_supp < 1 or nb_ing_supp > 5:
            raise ValueError("Le nombre d'ingredient supplémentaire doit être entre 1 et 5.")
        ing_possedes = [
            ing.id
            for ing in IngredientUtilisateurService().liste_tous_ingredients_utilisateur(
                utilisateur
            )
        ]
        ing_possibles = RechercheDao().ingredients_cocktails_quasifaisables(
            ing_possedes, nb_ing_supp
        )
        ing_choisis = []
        nb_cocktails = 0
        while len(ing_choisis) < nb_ing_supp:
            meilleur, nb_cocktails = meilleur_ingredient(ing_possibles, ing_possedes + ing_choisis)
            ing_possibles.remove(meilleur)
            ing_choisis.append(meilleur)

        return {
            "Nombre de cocktails supplémentaires": (
                nb_cocktails,
                RechercheDao().nb_cocktail_faisables(ing_possedes),
            ),
            "Liste de course": [IngredientService().verifier_ingredient(id) for id in ing_choisis],
        }
