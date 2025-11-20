from business_object.cocktail import Cocktail
from business_object.filtre_cocktail import FiltreCocktail
from business_object.filtre_ingredient import FiltreIngredient
from service.recherche_service import RechercheService
from service.utilisateur_service import UtilisateurService


def test_recherche_cocktail_filtre_id():
    """
    Teste si la fonction renvoie bien les cocktails dont l'id correspond à 11000.
    """

    # GIVEN
    filtre = FiltreCocktail(id=17222)

    # WHEN
    recherche = RechercheService().recherche_cocktail(filtre)

    # THEN
    assert "A1" in [cocktail.nom for cocktail in recherche]


def test_recherche_cocktail_filtre_nom():
    """
    Teste si la fonction renvoie bien les cocktails dont le nom correspond à 'Mauresque'.
    """

    # GIVEN
    filtre = FiltreCocktail(nom="ABC")

    # WHEN
    recherche = RechercheService().recherche_cocktail(filtre)

    # THEN
    assert "ABC" in [cocktail.nom for cocktail in recherche]


def test_recherche_ingredient_filtre_id():
    """
    Teste si la fonction renvoie bien les cocktails dont le nom correspond à 'Mauresque'.
    """

    # GIVEN
    filtre = FiltreIngredient(id=1)

    # WHEN
    recherche = RechercheService().recherche_ingredient(filtre)

    # THEN
    assert "Vodka" in [ing.nom for ing in recherche]


def test_recherche_ingredient_filtre_nom():
    """
    Teste si la fonction renvoie bien les ingrédients dont le nom correspond à 'Kahlua'.
    """

    # GIVEN
    filtre = FiltreIngredient(nom="Gin")

    # WHEN
    recherche = RechercheService().recherche_ingredient(filtre)

    # THEN
    assert "Gin" in [ing.nom for ing in recherche]


def test_recherche_cocktail_filtre_alcoolise():
    """
    Teste si la fonction filtre correctement par caractère alcoolisé.
    """

    # GIVEN
    filtre = FiltreCocktail(alcoolise=True)

    # WHEN
    recherche = RechercheService().recherche_cocktail(filtre)

    # THEN
    assert len(recherche) > 0
    assert all(cocktail.alcolise for cocktail in recherche)
    assert "A1" in [ing.nom for ing in recherche]


def test_recherche_cocktail_filtre_non_alcoolise():
    """
    Teste si la fonction filtre correctement les cocktails non alcoolisés.
    """

    # GIVEN
    filtre = FiltreCocktail(alcoolise=False)

    # WHEN
    recherche = RechercheService().recherche_cocktail(filtre)

    # THEN
    if len(recherche) > 0:  # S'il y a des cocktails non alcoolisés
        assert all(not cocktail.alcolise for cocktail in recherche)
        assert "Apello" in [ing.nom for ing in recherche]


def test_recherche_cocktail_filtre_categorie():
    """
    Teste si la fonction filtre correctement par catégorie.
    """

    # GIVEN - Utilise une catégorie qui existe dans ta base
    filtre = FiltreCocktail(categorie="ordinary drink")

    # WHEN
    recherche = RechercheService().recherche_cocktail(filtre)

    # THEN
    assert len(recherche) > 0
    assert all(cocktail.categorie == "ordinary drink" for cocktail in recherche)
    assert "Adam" in [ing.nom for ing in recherche]


def test_recherche_ingredient_filtre_alcoolise():
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


def test_liste_cocktails_faisables_complet():
    """
    Teste la fonction qui trouve les cocktails faisables avec les ingrédients d'un utilisateur.
    """

    # GIVEN
    # Créer ou récupérer un utilisateur existant avec des ingrédients
    utilisateur = UtilisateurService().trouver_par_nom("Gerald")  # Utilisateur existant

    # WHEN
    cocktails_faisables = RechercheService().liste_cocktails_faisables(
        utilisateur, nb_ing_manquants=0
    )

    # THEN
    assert isinstance(cocktails_faisables, list)  # may be revoir recherche_dao
    # Vérifie que ce sont bien des objets Cocktail
    if len(cocktails_faisables) > 0:
        assert all(isinstance(cocktail, Cocktail) for cocktail in cocktails_faisables)


def test_liste_cocktails_quasi_faisables():
    """
    Teste la fonction qui trouve les cocktails presque faisables (1 ingrédient manquant).
    """

    # GIVEN
    utilisateur = UtilisateurService().trouver_par_nom("Gerald")  # Utilisateur existant

    # WHEN
    cocktails_quasi_faisables = RechercheService().liste_cocktails_faisables(
        utilisateur, nb_ing_manquants=1
    )

    # THEN
    assert isinstance(cocktails_quasi_faisables, list)


def test_recherche_cocktail_erreur_filtre_incorrect():
    """
    Teste que la fonction lève une erreur quand le filtre n'est pas du bon type.
    """

    # GIVEN
    filtre_incorrect = "pas_un_filtre"

    # WHEN & THEN
    try:
        RechercheService().recherche_cocktail(filtre_incorrect)
        assert False, "L'erreur devrait être levée"
    except TypeError:
        assert True  # L'erreur est bien levée


def test_recherche_ingredient_erreur_filtre_incorrect():
    """
    Teste que la fonction lève une erreur quand le filtre n'est pas du bon type.
    """

    # GIVEN
    filtre_incorrect = "pas_un_filtre"  # Mauvais type

    # WHEN & THEN
    try:
        RechercheService().recherche_ingredient(filtre_incorrect)
        assert False, "L'erreur devrait être levée"
    except TypeError:
        assert True  # L'erreur est bien levée


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
