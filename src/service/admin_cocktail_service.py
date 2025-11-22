from business_object.cocktail import Cocktail
from dao.admin_cocktail_dao import AdminCocktailDAO
from service.cocktail_service import CocktailService
from service.recherche_service import FiltreCocktail, RechercheService


class AdminCocktailService:
    """
    Classe service des actions  destinées réservées aux administrateurs

    Methodes
    ----------
        ajout_cocktail
        supprimer_cocktail
    """

    def ajout_cocktail(
        self,
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
        if not isinstance(nom, str):
            raise TypeError("Le nom doit être un string.")
        if not isinstance(tags, list) and tags is not None:
            raise TypeError("Les tags doivent être une liste de strings.")
        if tags is not None and not all(isinstance(t, str) for t in tags):
            raise TypeError("Les tags doivent être des strings.")
        if not isinstance(categorie, str):
            raise TypeError("La catégorie doit être un string.")
        if not isinstance(iba, str):
            raise TypeError("Iba doit être un string.")
        if not isinstance(alcolise, bool):
            raise TypeError("Alcolisé doit être un booléen.")
        if not isinstance(verre, str):
            raise TypeError("Le verre doit être un string.")
        if not isinstance(instructions, str):
            raise TypeError("Les instructions doivent être sous forme de string.")
        if url_image is not None:
            if not isinstance(url_image, str):
                raise TypeError("Le lien URL doit être un string.")

        verif_pas_deja_existant = RechercheService().recherche_cocktail(
            FiltreCocktail(
                nom=nom, alcoolise=alcolise, categorie=categorie, iba=iba, verre=verre, tags=tags
            )
        )
        if verif_pas_deja_existant != []:
            raise ValueError("Ce cocktail existe déjà.")

        ajout_reussi = AdminCocktailDAO().ajouter_ckt(
            nom, tags, categorie, iba, alcolise, verre, instructions, url_image
        )
        if not isinstance(ajout_reussi, int):
            raise ValueError("Il y a eu un problème dans la création de ce nouvau cocktail.")

        return ajout_reussi

    def supprimer_cocktail(self, id_cocktail) -> Cocktail:
        """
        Supprime un cocktail pour un ADMINISTRATEUR

        Paramètres
        ----------
        id_cocktail : l'id du cocktail à supprimer


        Retour
        ----------
        Renvoie le cocktail supprimé
        """
        if not isinstance(id_cocktail, int):
            raise TypeError("id indiquée non conforme au format")
        item = CocktailService().verifier_cocktail(id_cocktail)
        if item is None:
            raise ValueError("Aucun cocktail ne possède cette id")
        suppression = AdminCocktailDAO().suppr_ckt(id_cocktail)
        if not suppression:
            raise ValueError("Aucun cocktail possédant cette id n'a été supprimé")
        return suppression
