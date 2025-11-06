from src.business_object.cocktail import Cocktail
from src.dao.admin_cocktail_dao import AdminCocktailDAO
from src.service.cocktail_service import CocktailService
from src.service.recherche_service import RechercheService


class AdminCocktailService:
    """
    Classe service des actions résservées aux administrateurs

    """

    def __init__(self, admcocktail_dao: AdminCocktailDAO) -> None:
        self.dao.admin_cocktail = admcocktail_dao

    def ajout_cocktail(
        self,
        id_utilisateur: int,
        nom: str,
        tags: list[str],
        categorie: str,
        iba: str,
        alcolise: bool,
        verre: str,
        instructions: str,
        url_image: str = None,
    ) -> int:
        """
        Ajoute un cocktail par un ADMINISTRATEUR.

        Paramètres
        ----------
        id_utilisateur :
            l'id de l'utilisateur qui fait la requete
            (afin de regarder s'il s'agit d'un administrateur )
        nom : str 
            nom usuel d'un cocktail
        tags : str
            Les tags attribués au cocktail
        categorie : str 
            catégorie du cocktail
        iba : str 
            type de cocktail considéré par l'IBA(the International Bartender Association)
        alcolise : bool
            booléen indiquant si le cocktail contient de l'alcool 
        verre : str 
            type de verre utilisé pour faire le cocktail
        instructions : str
            instructions pour réaliser le cocktail
        url_image : str 
            potentielle image d'illustration du cocktail

        Retour
        ----------
        ajout_reussi : int
            l'id du cocktail ajouté
        """
        if id_utilisateur not in id_admins:
            raise ValueError("vos droits ne vous permettent pas de modifier la base de données.")
        if nom is not str:
            raise TypeError("Le nom doit être un string.")
        if tags is not list[str]:
            raise TypeError("Les tags doivent être des strings.")
        if categorie is not str:
            raise TypeError("La catégorie doit être un string.")
        if iba is not str:
            raise TypeError("Iba doit être un string.")
        if alcolise is not bool:
            raise TypeError("Alcolisé doit être un booléen.")
        if verre is not str:
            raise TypeError("Le verre doit être un string.")
        if instructions is not str:
            raise TypeError("Les instructions doivent être sous forme de string.")
        if url_image is not None:
            if url_image is not str:
                raise TypeError("Le lien URL doit être un string.")
        verif_pas_deja_existant = RechercheService().recherche_cocktail(
            nom=nom, alcoolise=alcolise, categorie=categorie, iba=iba, verre=verre, tags=tags
        )
        if verif_pas_deja_existant is not None:
            raise ValueError("Ce cocktail existe déjà.")
        ajout_reussi = AdminCocktailDAO().ajouter_ckt(
            nom, tags, categorie, iba, alcolise, verre, instructions, url_image
        )
        if ajout_reussi is not int:
            raise ValueError("Il y a eu un problème dans la création de ce nouvau cocktail.")
        return ajout_reussi
    def supprimer_cocktail(self, id_utilisateur, id_cocktail) -> Cocktail:
        """
        Supprime un cocktail pour un ADMINISTRATEUR

        Paramètres
        ----------
        id_utilisateur : l'id de l'utilisateur qui fait la requete
        id_cocktail : l'id du cocktail à supprimer


        Retour
        ----------
        Renvoie le cocktail supprimé
        """
        if id_utilisateur not in id_admins:
            raise ValueError("vos droits ne vous permettent pas de modifier la base de données")
        if id_cocktail is not int:
            raise TypeError("id indiquée non conforme au format")

        item = CocktailService().verifier_cocktail(id_cocktail)
        if item is None:
            raise ValueError("Aucun cocktail ne possèède cette id")
        return AdminCocktailDAO().suppr_ckt(id_cocktail)
