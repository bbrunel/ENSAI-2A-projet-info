from src.business_object.cocktail import Cocktail
from src.dao.admin_cocktail import AdminCocktailDAO
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
        tags: str,
        categorie: str,
        iba: str,
        alcolise: bool,
        verre: str,
        instructions: str,
        nom_alt: str = None,
        url_image: str = None,
    ) -> Cocktail:
        """
        Ajoute un cocktail par un ADMINISTRATEUR.

        Paramètres
        ----------
        id_utilisateur :
            l'id de l'utilisateur qui fait la requete
            (afin de regarder s'il s'agit d'un administrateur )


        Retour
        ----------
        Renvoie le cocktail ajouté
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
        if nom_alt is not None:
            if nom_alt is not str:
                raise TypeError("Le(s) nom(s) doi(ven)t être un string.")
        if url_image is not None:
            if url_image is not str:
                raise TypeError("Le lien URL doit être un string.")
        verif_pas_deja_existant = RechercheService().recherche_cocktail(
            nom=nom, alcoolise=alcolise, categorie=categorie, iba=iba, verre=verre, tags=tags
        )
        if verif_pas_deja_existant is not None:
            raise ValueError("Ce cocktail existe déjà.")
        return AdminCocktailDAO().ajouter_ckt(
            nom, tags, categorie, iba, alcolise, verre, instructions, nom_alt, url_image
        )

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
