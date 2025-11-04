from src.business_object.filtre_ingredient import FiltreIngredient
from src.business_object.filtre_cocktail import FiltreCocktail
#from src.dao import RechercheDAO

class RechercheService:
    """Permet de rechercher des cocktails et des ingrédients en appliquant un filte de recherche.
    """
    def __init__(self, recherche_dao : RechercheDAO):
        self.dao = recherche_dao

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
        if type(filtre)!= FiltreCocktail:
            raise TypeError(f'Filtre pas adapté à la recherche de cocktails.')
        
        cocktails = self.dao.recherche_cocktail(filtre)
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
        if type(filtre)!= FiltreIngredient:
            raise TypeError(f"Filtre pas adapté à la recherche d'ingrédients")

        ingredients = self.dao.recherche_ingredient(filtre)
        if ingredients is None:
            raise ValueError(f"Pas d'ingrédient correspondant au filtre.")
        return ingredients 
    
    def liste_cocktails_faisables(self, utilisateur):
        """Renvoie la liste des cocktails faisables en fonction des ingrédients de l'utilisateur.

        Parameter
        -------
            utilisateur: Utilisateur
                L'utilisateur dont l'inventaire est utilisé pour chercher les cocktails faisables.
        
        Return
        -------
            list[Cocktail]
                La liste des cocktails faisables selon les ingrédients de l'utilisateur.
        """
        inventaire = IngredientUtilisateurService.lister_tous_ingredients_utilisateur(utilisateur)
        tous_cocktails = CocktailService.lister_tous_cocktail()
        cocktails_faisables = []
        
        for cocktail in tous_cocktails:
            ingredients = CocktailService.ingredient_cocktail(cocktail)
            faisable = True
            
            for ingredient in ingredients:
                if ingredient not in inventaire:
                    faisable = False
                    break
            
            if faisable:
                cocktails_faisables.append(cocktail)
        return cocktails_faisables
    
    def liste_cocktails_quasi_faisables(self, utilisateur, nb_ing_manquants):
        """Renvoie la liste des cocktails faisables ou presque faisables en fonction des ingrédients
         de l'utilisateur.

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
        inventaire = IngredientUtilisateurService.lister_tous_ingredients_utilisateur(utilisateur)
        tous_cocktails = CocktailService.lister_tous_cocktail()
        cocktails_faisables = []
        
        for cocktail in tous_cocktails:
            ingredients = CocktailService.ingredient_cocktail(cocktail)
            faisable = True
            compt_ing_manquants = nb_ing_manquant
            
            for ingredient in ingredients:
                if ingredient not in inventaire:
                    compt_ing_manquants -=1
                    if compt_ing_manquants == 0:
                        faisable = False
                        break
            
            if faisable:
                cocktails_faisables.append(cocktail)
        
        return cocktails_faisables