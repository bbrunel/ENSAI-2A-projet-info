from unittest.mock import MagicMock
from service.recherche_service import RechercheService
from business_object.ingredient import Ingredient
from business_object.filtre_cocktail import FiltreCocktail
from business_object.filtre_ingredient import FiltreIngredient


def test_recherche_cocktail_filtre_nom():
    """
    Teste si la fonction renvoie bien les cocktails dont le nom correspond à 'mauresque'.
    """
    
    #GIVEN
    filtre = FiltreIngredient(nom = "mauresque")
    recherche_cocktail_mauresque = pass #A COMPLETER

    #WHEN
    recherche = recherche_cocktail(filtre)

    #THEN
    assert recherche == recherche_cocktail_mauresque


def test_recherche_ingredient_filtre_nom():
    """
    Teste si la fonction renvoie bien les ingrédients dont le nom correspond à 'kahlua'.
    """

    #GIVEN
    filtre = FiltreIngredient(nom = "kahlua")
    recherche_ingredient_kahlua = pass #A COMPLETER

    #WHEN
    recherche = recherche_ingredient(filtre)

    #THEN
    assert recherche == recherche_ingredient_kahlua


def test_liste_cocktails_faisables():
    """
    Teste si la fonction renvoie bien les cocktails faisables à partir des ingrédients de
    l'utilisateur.
    """

    #GIVEN
    ingredients_utilisateurs = inventaire_utilisateur
    liste_test = pass #A COMPLETER

    #WHEN
    cocktails = liste_cocktails_faisables()

    #THEN
    assert cocktails == liste_test