from unittest.mock import MagicMock
from service.recherche_service import RechercheService

from business_object.cocktail import Cocktail
from business_object.ingredient import Ingredient
from business_object.filtre_cocktail import FiltreCocktail
from business_object.filtre_ingredient import FiltreIngredient

from dao.cocktail_dao import Cocktail


def test_recherche_cocktail_filtre_nom():
    """
    Teste si la fonction renvoie bien les cocktails dont le nom correspond à 'Mauresque'.
    """
    
    #GIVEN
    filtre = FiltreIngredient(nom = "Mauresque")

    #WHEN
    recherche = recherche_cocktail(filtre)

    #THEN
    assert recherche[0].nom == "Mauresque"


def test_recherche_ingredient_filtre_nom():
    """
    Teste si la fonction renvoie bien les ingrédients dont le nom correspond à 'Kahlua'.
    """

    #GIVEN
    filtre = FiltreIngredient(nom = "Kahlua")

    #WHEN
    recherche = recherche_ingredient(filtre)

    #THEN
    assert recherche[0].nom == "Kahlua"


def test_liste_cocktails_faisables():
    """
    Teste si la fonction renvoie bien les cocktails faisables à partir des ingrédients de
    l'utilisateur.
    """

    #GIVEN
    id_ingredients_utilisateurs = [513, 427, 362]
    #CREER UN UTILISATEUR MOCK

    #WHEN
    cocktails = liste_cocktails_faisables()

    #THEN
    assert cocktails[0].nom == "Mauresque"