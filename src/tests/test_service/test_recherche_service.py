import os
import sys

# Ajouter le chemin src au PYTHONPATH
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from unittest.mock import patch

import pytest

from business_object.cocktail import Cocktail
from business_object.filtre_cocktail import FiltreCocktail
from business_object.filtre_ingredient import FiltreIngredient
from business_object.ingredient import Ingredient
from business_object.utilisateur import Utilisateur
from service.recherche_service import RechercheService
from service.utilisateur_service import UtilisateurService

# Tests unitaires


class Test_recherche_service_unitaire:
    """
    Teste la classe RechercheService à travers des tests unitaires.

    Methodes testées
    ----------
        recherche_cocktail
        recherche_ingredient
        liste_cocktails_faisables
        recherche_ingredients_optimaux
    """

    ## recherche_cocktail

    def test_recherche_cocktail_ok(self):
        """
        Teste si la méthode renvoie bien les cocktails correspondant aux filtres.
        """
        # GIVEN
        filtre = FiltreCocktail(id=11000)
        cocktails_attendus = [Cocktail(id=11000, nom="Mojito", alcoolise=True)]

        with patch(
            "dao.recherche_dao.RechercheDao.recherche_cocktail", return_value=cocktails_attendus
        ):
            # WHEN
            resultat = RechercheService().recherche_cocktail(filtre)

        # THEN
        assert resultat == cocktails_attendus
        assert len(resultat) == 1
        assert resultat[0].nom == "Mojito"

    def test_recherche_cocktail_erreur_type_filtre(self):
        """
        Teste si la méthode lève bien une erreur quand le filtre n'est pas du bon type.
        """
        # GIVEN
        filtre_incorrect = "pas_un_filtre"

        # WHEN & THEN
        with pytest.raises(TypeError):
            RechercheService().recherche_cocktail(filtre_incorrect)

    def test_recherche_cocktail_erreur_aucun_resultat(self):
        """
        Teste si la méthode lève bien une erreur quand aucun cocktail n'est trouvé.
        """
        # GIVEN
        filtre = FiltreCocktail(id=999999)

        with patch("dao.recherche_dao.RechercheDao.recherche_cocktail", return_value=None):
            # WHEN & THEN
            with pytest.raises(ValueError):
                RechercheService().recherche_cocktail(filtre)

    def test_recherche_cocktail_filtre_none(self):
        """
        Teste si la méthode accepte un filtre None.
        """
        # GIVEN
        cocktails_attendus = [
            Cocktail(id=1, nom="cocktail 1", alcoolise=True),
            Cocktail(id=2, nom="cocktail 2", alcoolise=True),
            Cocktail(id=3, nom="cocktail 3", alcoolise=True),
            Cocktail(id=4, nom="cocktail 4", alcoolise=True),
        ]
        with patch(
            "dao.recherche_dao.RechercheDao.recherche_cocktail",
            return_value=[
                Cocktail(id=1, nom="cocktail 1", alcoolise=True),
                Cocktail(id=2, nom="cocktail 2", alcoolise=True),
                Cocktail(id=3, nom="cocktail 3", alcoolise=True),
                Cocktail(id=4, nom="cocktail 4", alcoolise=True),
            ],
        ):
            # WHEN
            resultat = RechercheService().recherche_cocktail(None)

        # THEN
        assert resultat == cocktails_attendus

    ## recherche_ingredient

    def test_recherche_ingredient_ok(self):
        """
        Teste si la méthode renvoie bien les ingrédients correspondant aux filtres.
        """
        # GIVEN
        filtre = FiltreIngredient(nom="Vodka")
        ingredients_attendus = [Ingredient(1, "Vodka", "", "", True, 40.0)]

        with patch(
            "dao.recherche_dao.RechercheDao.recherche_ingredient", return_value=ingredients_attendus
        ):
            # WHEN
            resultat = RechercheService().recherche_ingredient(filtre)

        # THEN
        assert resultat == ingredients_attendus
        assert len(resultat) == 1
        assert resultat[0].nom == "Vodka"

    def test_recherche_ingredient_erreur_type_filtre(self):
        """
        Teste si la méthode lève bien une erreur quand le filtre n'est pas du bon type.
        """
        # GIVEN
        filtre_incorrect = "pas_un_filtre"

        # WHEN & THEN
        with pytest.raises(TypeError):
            RechercheService().recherche_ingredient(filtre_incorrect)

    def test_recherche_ingredient_erreur_aucun_resultat(self):
        """
        Teste si la méthode lève bien une erreur quand aucun ingrédient n'est trouvé.
        """
        # GIVEN
        filtre = FiltreIngredient(nom="IngredientInexistant")

        with patch("dao.recherche_dao.RechercheDao.recherche_ingredient", return_value=None):
            # WHEN & THEN
            with pytest.raises(ValueError):
                RechercheService().recherche_ingredient(filtre)

    ## liste_cocktails_faisables

    def test_liste_cocktails_faisables_ok(self):
        """
        Teste si la méthode renvoie bien les cocktails faisables.
        """
        # GIVEN
        utilisateur = Utilisateur(id=1, nom_utilisateur="Test")
        inventaire = [Ingredient(1, "Vodka", "", "", True, 40.0)]
        cocktails_attendus = [Cocktail(id=1, nom="Vodka Martini", alcoolise=True)]

        with (
            patch(
                "service.ingredient_utilisateur_service.IngredientUtilisateurService.liste_tous_ingredients_utilisateur",
                return_value=inventaire,
            ),
            patch(
                "dao.recherche_dao.RechercheDao.cocktails_faisables",
                return_value=cocktails_attendus,
            ),
        ):
            # WHEN
            resultat = RechercheService().liste_cocktails_faisables(utilisateur, 0)

        # THEN
        assert resultat == cocktails_attendus

    def test_liste_cocktails_quasi_faisables_ok(self):
        """
        Teste si la méthode renvoie bien les cocktails quasi-faisables.
        """
        # GIVEN
        utilisateur = Utilisateur(id=1, nom_utilisateur="Test")
        inventaire = [Ingredient(1, "Vodka", "", "", True, 40.0)]
        cocktails_attendus = [Cocktail(id=2, nom="Mojito", alcoolise=True)]

        with (
            patch(
                "service.ingredient_utilisateur_service.IngredientUtilisateurService.liste_tous_ingredients_utilisateur",
                return_value=inventaire,
            ),
            patch(
                "dao.recherche_dao.RechercheDao.cocktails_faisables",
                return_value=cocktails_attendus,
            ),
        ):
            # WHEN
            resultat = RechercheService().liste_cocktails_faisables(utilisateur, 1)

        # THEN
        assert resultat == cocktails_attendus

    ## recherche_ingredients_optimaux
    def test_recherche_ingredients_optimaux_ok(self):
        """
        Teste la méthode avec un cas simple.
        """
        # GIVEN
        utilisateur = Utilisateur(id=1, nom_utilisateur="Test")

        with (
            patch("service.recherche_service.IngredientUtilisateurService") as mock_ius,
            patch("service.recherche_service.RechercheDao") as mock_dao,
            patch("service.recherche_service.IngredientService") as mock_is,
        ):
            mock_ius.return_value.liste_tous_ingredients_utilisateur.return_value = [
                Ingredient(
                    id=1,
                    nom="Ing1",
                    desc="Description 1",
                    type_ing="liqueur",
                    alcoolise=True,
                    abv=40,
                ),
                Ingredient(
                    id=2,
                    nom="Ing2",
                    desc="Description 2",
                    type_ing="liqueur",
                    alcoolise=True,
                    abv=40,
                ),
            ]

            mock_dao.return_value.ingredients_cocktails_quasifaisables.return_value = [3, 4, 5]
            mock_dao.return_value.nb_cocktail_faisables.return_value = 5

            mock_is.return_value.nb_cocktails.return_value = 10
            mock_is.return_value.verifier_ingredient.side_effect = lambda id: Ingredient(
                id=id,
                nom=f"Ing{id}",
                desc=f"Description {id}",
                type_ing="liqueur",
                alcoolise=True,
                abv=40,
            )

            # WHEN
            resultat = RechercheService().recherche_ingredients_optimaux(utilisateur, 1)

        # THEN
        assert "Nombre de cocktails supplémentaires" in resultat
        assert "Liste de course" in resultat
        assert len(resultat["Liste de course"]) == 1

    def test_recherche_ingredients_optimaux_erreur_nb_ing_supp_trop_bas(self):
        """
        Teste si la méthode lève bien une erreur quand nb_ing_supp < 1.
        """
        # GIVEN
        utilisateur = Utilisateur(id=1, nom_utilisateur="Test")

        # WHEN & THEN
        with pytest.raises(ValueError):
            RechercheService().recherche_ingredients_optimaux(utilisateur, 0)

    def test_recherche_ingredients_optimaux_erreur_nb_ing_supp_trop_haut(self):
        """
        Teste si la méthode lève bien une erreur quand nb_ing_supp > 20.
        """
        # GIVEN
        utilisateur = Utilisateur(id=1, nom_utilisateur="Test")

        # WHEN & THEN
        with pytest.raises(ValueError):
            RechercheService().recherche_ingredients_optimaux(utilisateur, 21)


# Tests d'intégration


class Test_recherche_service_integration:
    """
    Teste la classe RechercheService à travers des tests d'intégration.

    Methodes testées
    ----------
        recherche_cocktail
        recherche_ingredient
        liste_cocktails_faisables
        recherche_ingredients_optimaux
    """

    ## recherche_cocktail

    def test_recherche_cocktail_filtre_id(self):
        """
        Teste si la fonction renvoie bien les cocktails dont l'id correspond à 17222.
        """
        # GIVEN
        filtre = FiltreCocktail(id=17222)

        # WHEN
        recherche = RechercheService().recherche_cocktail(filtre)

        # THEN
        assert "A1" in [cocktail.nom for cocktail in recherche]

    def test_recherche_cocktail_filtre_nom(self):
        """
        Teste si la fonction renvoie bien les cocktails dont le nom correspond à 'ABC'.
        """
        # GIVEN
        filtre = FiltreCocktail(nom="ABC")

        # WHEN
        recherche = RechercheService().recherche_cocktail(filtre)

        # THEN
        assert "ABC" in [cocktail.nom for cocktail in recherche]

    def test_recherche_cocktail_filtre_alcoolise(self):
        """
        Teste si la fonction filtre correctement par caractère alcoolisé.
        """
        # GIVEN
        filtre = FiltreCocktail(alcoolise=True)

        # WHEN
        recherche = RechercheService().recherche_cocktail(filtre)

        # THEN
        assert len(recherche) > 0
        assert all(cocktail.alcoolise for cocktail in recherche)
        assert "A1" in [ing.nom for ing in recherche]

    def test_recherche_cocktail_filtre_non_alcoolise(self):
        """
        Teste si la fonction filtre correctement les cocktails non alcoolisés.
        """
        # GIVEN
        filtre = FiltreCocktail(alcoolise=False)

        # WHEN
        recherche = RechercheService().recherche_cocktail(filtre)

        # THEN
        if len(recherche) > 0:  # S'il y a des cocktails non alcoolisés
            assert all(not cocktail.alcoolise for cocktail in recherche)
            assert "Apello" in [ing.nom for ing in recherche]

    def test_recherche_cocktail_filtre_categorie(self):
        """
        Teste si la fonction filtre correctement par catégorie.
        """
        # GIVEN
        filtre = FiltreCocktail(categorie="ordinary drink")

        # WHEN
        recherche = RechercheService().recherche_cocktail(filtre)

        # THEN
        assert len(recherche) > 0
        assert all(cocktail.categorie == "ordinary drink" for cocktail in recherche)
        assert "Adam" in [ing.nom for ing in recherche]

    def test_recherche_cocktail_erreur_filtre_incorrect(self):
        """
        Teste que la fonction lève une erreur quand le filtre n'est pas du bon type.
        """
        # GIVEN
        filtre_incorrect = "pas_un_filtre"

        # WHEN & THEN
        with pytest.raises(TypeError):
            RechercheService().recherche_cocktail(filtre_incorrect)

    ## recherche_ingredient

    def test_recherche_ingredient_filtre_id(self):
        """
        Teste si la fonction renvoie bien les ingrédients dont l'id correspond à 1.
        """
        # GIVEN
        filtre = FiltreIngredient(id=3)

        # WHEN
        recherche = RechercheService().recherche_ingredient(filtre)

        # THEN
        assert "Rum" in [ing.nom for ing in recherche]

    def test_recherche_ingredient_filtre_nom(self):
        """
        Teste si la fonction renvoie bien les ingrédients dont le nom correspond à 'Gin'.
        """
        # GIVEN
        filtre = FiltreIngredient(nom="Gin")

        # WHEN
        recherche = RechercheService().recherche_ingredient(filtre)

        # THEN
        assert "Gin" in [ing.nom for ing in recherche]

    def test_recherche_ingredient_filtre_alcoolise(self):
        """
        Teste si la fonction filtre correctement les ingrédients alcoolisés.
        """
        # GIVEN
        filtre = FiltreIngredient(alcoolise=True)

        # WHEN
        recherche = RechercheService().recherche_ingredient(filtre)

        # THEN
        assert len(recherche) > 0
        assert all(ing.alcoolise for ing in recherche)
        assert "Gin" in [ing.nom for ing in recherche]

    def test_recherche_ingredient_erreur_filtre_incorrect(self):
        """
        Teste que la fonction lève une erreur quand le filtre n'est pas du bon type.
        """
        # GIVEN
        filtre_incorrect = "pas_un_filtre"

        # WHEN & THEN
        with pytest.raises(TypeError):
            RechercheService().recherche_ingredient(filtre_incorrect)

    ## liste_cocktails_faisables

    def test_liste_cocktails_faisables_complet(self):
        """
        Teste la fonction qui trouve les cocktails faisables avec les ingrédients d'un utilisateur.
        """
        # GIVEN
        utilisateur = UtilisateurService().trouver_par_nom("Gerald")

        # WHEN
        cocktails_faisables = RechercheService().liste_cocktails_faisables(
            utilisateur, nb_ing_manquants=0
        )

        # THEN
        assert isinstance(cocktails_faisables, list)
        if len(cocktails_faisables) > 0:
            assert all(isinstance(cocktail, Cocktail) for cocktail in cocktails_faisables)

    def test_liste_cocktails_quasi_faisables(self):
        """
        Teste la fonction qui trouve les cocktails presque faisables (1 ingrédient manquant).
        """
        # GIVEN
        utilisateur = UtilisateurService().trouver_par_nom("Gerald")

        # WHEN
        cocktails_quasi_faisables = RechercheService().liste_cocktails_faisables(
            utilisateur, nb_ing_manquants=1
        )

        # THEN
        assert isinstance(cocktails_quasi_faisables, list)

    ## recherche_ingredients_optimaux

    def test_recherche_ingredients_optimaux_basique(self):
        """
        Teste la fonction de recherche d'ingrédients optimaux avec un cas simple.
        """
        # GIVEN
        from service.utilisateur_service import UtilisateurService

        utilisateur = UtilisateurService().trouver_par_nom("Gerald")

        # WHEN
        resultat = RechercheService().recherche_ingredients_optimaux(utilisateur, 1)

        # THEN
        assert "Nombre de cocktails supplémentaires" in resultat
        assert "Liste de course" in resultat
        assert isinstance(resultat["Nombre de cocktails supplémentaires"], int)
        assert isinstance(resultat["Liste de course"], list)
        if len(resultat["Liste de course"]) > 0:
            assert all(isinstance(ing, Ingredient) for ing in resultat["Liste de course"])


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
