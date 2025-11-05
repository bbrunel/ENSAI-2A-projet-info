from unittest.mock import MagicMock
from dao.recherche_dao import RechercheDao

from business_object.cocktail import Cocktail
from business_object.ingredient import Ingredient
from business_object.filtre_cocktail import FiltreCocktail
from business_object.filtre_ingredient import FiltreIngredient

def test_recherche_cocktail_mauresque():
    """
    Teste si la methode recherche_cocktail renvoie bien le cocktail 'Mauresque' correspondant au 
    filtre, contenant le nom 'Mauresque'.
    """

    #GIVEN
    filtre = FiltreCocktail(nom = "Mauresque")

    #WHEN
    recherche = recherche_cocktail(filtre)

    #THEN
    assert recherche[0].nom == "Mauresque"


def test_cocktails_faisables_mauresque():
    """
    Teste si la liste des cocktails faisables contient le cocktail 'Mauresque' avec la liste des id 
    des ingrédients du cocktail.
    """

    #GIVEN
    id_ingredients_utilisateurs = [513, 427, 362]

    #WHEN
    cocktails = cocktails_faisables(id_ingredients_utilisateurs)

    #THEN
    assert cocktails[0].nom == "Mauresque"


def test_recherche_ingredient():
    """
    Teste si la methode renvoie bien l'ingrédient 'Water' pour un filtre dont le nom filtré est 
    'Water'.
    """

    #GIVEN
    filtre = FiltreIngredient(nom = "Water")

    #WHEN
    resultat = recherche_ingredient(filtre)

    #THEN
    assert resultat[0].nom == "Water"