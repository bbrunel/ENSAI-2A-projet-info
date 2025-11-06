from unittest.mock import MagicMock
from service.recherche_service import RechercheService

from business_object.cocktail import Cocktail
from business_object.ingredient import Ingredient
from business_object.filtre_cocktail import FiltreCocktail
from business_object.filtre_ingredient import FiltreIngredient


def test_recherche_cocktail_filtre_nom():
    """
    Teste si la fonction renvoie bien les cocktails dont le nom correspond à 'Mauresque'.
    """
    
    #GIVEN
    filtre = FiltreCocktail(nom = "Mauresque")

    #WHEN
    recherche = RechercheService().recherche_cocktail(filtre)

    #THEN
    assert "Mauresque" in [cocktail.nom for cocktail in recherche]


def test_recherche_ingredient_filtre_nom():
    """
    Teste si la fonction renvoie bien les ingrédients dont le nom correspond à 'Kahlua'.
    """

    #GIVEN
    filtre = FiltreIngredient(nom = "Kahlua")

    #WHEN
    recherche = RechercheService().recherche_ingredient(filtre)

    #THEN
    assert "Kahlua" in [ing.nom for ing in recherche]


def test_liste_cocktails_faisables():
    """
    Teste si la fonction renvoie bien les cocktails faisables à partir des ingrédients de
    l'utilisateur.
    """

    #GIVEN
    id_ingredients_utilisateurs = [513, 427, 362]
    #CREER UN UTILISATEUR MOCK AVEC DB LOCALE

    #WHEN
    cocktails = RechercheService().liste_cocktails_faisables()

    #THEN
    assert cocktails[0].nom == "Mauresque"


def test_liste_cocktails_quasi_faisables():
    """
    Teste si la fonction renvoie bien les cocktails presque faisables à partir des ingrédients de
    l'utilisateur.
    """

    #GIVEN
    id_ingredients_utilisateurs = [513, 427]
    #CREER UN UTILISATEUR MOCK AVEC DB LOCALE

    #WHEN
    cocktails = RechercheService().liste_cocktails_faisables()

    #THEN
    assert cocktails[0].nom == "Mauresque"