from business_object.filtre_ingredient import FiltreIngredient
from business_object.filtre_cocktail import FiltreCocktail
from dao.recherche_dao import RechercheDao


class RechercheService:
    """Permet de rechercher des cocktails et des ingrédients en appliquant un filte de recherche.
    """

    def __init__(self):
        pass

    def recherche_cocktail(self, filtre):
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
        if not isinstance(filtre, FiltreCocktail):
            raise TypeError(f'Filtre pas adapté à la recherche de cocktails.')

        cocktails = RechercheDao().recherche_cocktail(filtre)
        if cocktails is None:
            raise ValueError(f'Pas de cocktail correspondant au filtre.')
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
            raise TypeError(f"Filtre pas adapté à la recherche d'ingrédients")

        ingredients = RechercheDao().recherche_ingredient(filtre)

        if ingredients is None:
            raise ValueError(f"Pas d'ingrédient correspondant au filtre.")

        return ingredients


    def liste_cocktails_faisables(self, utilisateur):
        """Renvoie la liste des cocktails faisables en fonction des ingrédients de l'utilisateur.
        Utilise l'utilisateur en argument pour en extraire son inventaire, puis les id des
        ingrédients de son inventaire, pour les donner en argument de la fonction DAO
        correspondante.
        Utilise la fonction de la classe DAO correspondant à la recherche de cocktails presque
        faisables, avec 0 ingrédients manquants.

        Parameter
        -------
            utilisateur: Utilisateur
                L'utilisateur dont l'inventaire est utilisé pour chercher les cocktails faisables.

        Return
        -------
            list[Cocktail]
                La liste des cocktails faisables selon les ingrédients de l'utilisateur.
        """

        inventaire = IngredientUtilisateurService().lister_tous_ingredients_utilisateur(utilisateur)
        id_ing_inventaire = [ingredient.id for ingredient in inventaire]

        return RechercheDao().liste_cocktails_faisables(id_ing_inventaire, 0)


    def liste_cocktails_quasi_faisables(self, utilisateur, nb_ing_manquants):
        """Renvoie la liste des cocktails faisables ou presque faisables en fonction des
        ingrédients de l'utilisateur.
        Utilise l'utilisateur en argument pour en extraire son inventaire, puis les id des
        ingrédients de son inventaire, pour les donner en argument de la fonction DAO
        correspondante.

        Parameter
        -------
            utilisateur: Utilisateur
                L'utilisateur dont l'inventaire est utilisé pour chercher les cocktails faisables.

            nb_ing_manquants: int
                Le nombre d'ingrédients manquants qu'il n'est pas nécessaire d'avoir pour qu'un
                cocktail soit renvoyé.

        Return
        -------
            list[Cocktail]
                La liste des cocktails faisables ou presque selon les ingrédients de l'utilisateur.
        """

        inventaire = IngredientUtilisateurService().lister_tous_ingredients_utilisateur(utilisateur)
        id_ing_inventaire = [ingredient.id for ingredient in inventaire]

        return RechercheDao().liste_cocktails_faisables(id_ing_inventaire, nb_ing_manquants)
