from unittest.mock import MagicMock
from service.recherche_service import RechercheService

from business_object.cocktail import Cocktail
from business_object.ingredient import Ingredient
from business_object.filtre_cocktail import FiltreCocktail
from business_object.filtre_ingredient import FiltreIngredient

from business_object.utilisateur import Utilisateur
from dao.utilisateur_dao import UtilisateurDao

from service.ingredient_utilisateur_service import IngredientUtilisateurService

def test_recherche_cocktail_filtre_id():
    """
    Teste si la fonction renvoie bien les cocktails dont l'id correspond à 11000.
    """
    
    #GIVEN
    filtre = FiltreCocktail(id = 11000)

    #WHEN
    recherche = RechercheService().recherche_cocktail(filtre)

    #THEN
    assert "Mojito" in [cocktail.nom for cocktail in recherche]


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


def test_recherche_ingredient_filtre_id():
    """
    Teste si la fonction renvoie bien les cocktails dont le nom correspond à 'Mauresque'.
    """
    
    #GIVEN
    filtre = FiltreIngredient(id = 305)

    #WHEN
    recherche = RechercheService().recherche_ingredient(filtre)

    #THEN
    assert "Light Rum" in [ing.nom for ing in recherche]


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
    utilisateur = UtilisateurDao().trouver_par_id(1)

    #WHEN
    recherche = RechercheService().liste_cocktails_faisables(utilisateur)

    #THEN
    assert 'Mojito' in [cocktail.nom for cocktail in recherche]



def test_liste_cocktails_quasi_faisables():
    """
    Teste si la fonction renvoie bien les cocktails presque faisables à partir des ingrédients de
    l'utilisateur.
    """

    #GIVEN
    utilisateur = UtilisateurDao().trouver_par_id(2)

    #WHEN
    recherche = RechercheService().liste_cocktails_faisables(utilisateur, 3)

    #THEN
    assert 'Mojito' in [cocktail.nom for cocktail in recherche]