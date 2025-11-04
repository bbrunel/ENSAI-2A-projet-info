from cocktail import Cocktail

from src.dao.admin_cocktail import AdminCocktailDAO

class AdminCocktailService:
    """
    Classe service pour les cocktails

    
    """
    def __init__(self, cocktail_dao : CocktailDAO) -> None:
        self.dao.cocktail = cocktail_dao
        
    def ajout_cocktail(self, 
        id_utilisateur : int, 
        nom : str,
        nom_alt : str = None,
        tags : str,
        categorie : str ,
        iba : str ,
        alcolise : bool,
        abv : int,
        verre : str ,
        instructions : str,
        url_image : str = None) -> Cocktail:
        """
        Ajoute un cocktail par un ADMINISTRATEUR.

        Paramètres 
        ----------
        id_utilisateur : l'id de l'utilisateur qui fait la requete 
        
        
        Retour
        ----------
        renvoie PasLesDroits : si l'utilisateur qui fait appel au service n'est pas un administrateur 
        retourne le cocktail ajouté
        """
        if id_utilisateur not in id_admins:
            raise
    
    def supprimer_cocktail(self, id_utilisateur, id_cocktail) -> Cocktail:
        """
        Supprime un cocktail pour un ADMINISTRATEUR

        Paramètres 
        ----------
        id_utilisateur : l'id de l'utilisateur qui fait la requete 
        id_cocktail : l'id du cocktail à supprimer
        
        
        Retour
        ----------
        renvoie ErreurCocktailPasTrouvé: si le cocktail n'a pas été trouvé
        renvoie PasLesDroits : si l'utilisateur qui fait appel au service n'est pas un administrateur 
        retourne le cocktail supprimé
        """
        item = self.dao.read(item_id)
        if item is None:
            raise ErreurCocktailPasTrouvé(item_id)
        if item.user_id not in  id_admins:
            raise PasLesDroits
        cocktail_a_suppr = self.dao.delete(item_id)
        if cocktail_a_suppr is None:
            raise ErreurCocktailPasTrouvé(item_id)
        return cocktail_a_suppr
    
    
    def verifier_cocktail(self,, id_cocktail : int ) -> Cocktail:
        """Vérifie si un cocktail existe bel et bien déjà.

        Paramètres 
        ----------
        id_cocktail : l'id du cocktail à vérifier
        
        
        Retour
        ----------
        renvoie ErreurCocktailPasTrouvé: si le cocktail n'a pas été trouvé
        retourne le cocktail dont on vérifie la présence 
        """       
        cocktail = self.dao.cocktail.lecture(id_cocktail)
        if cocktail is None:
            raise ErreurCocktailPasTrouvé(id_cocktail)
        return cocktail

    
    def ingredient_cocktail ():


    def lister_tous_cocktail() -> list[Cocktail]:
        """Lister l'ensemble des cocktails

        Paramètres 
        ----------
        
        
        Retour
        ----------
        renvoie ErreurCocktailPasTrouvé: si aucun cocktail n'a été trouvé
        retourne le cocktail dont on vérifie la présence 
        """
        return 
