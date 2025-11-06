from typing import Annotated
from fastapi import APIRouter, Query


from business_object.filtre_cocktail import FiltreCocktail
from business_object.filtre_ingredient import FiltreIngredient
from service.recherche_service import RechercheService

router = APIRouter()

recherche_service = RechercheService()

@router.get("/recherche_cocktail/{nom_cocktail}", tags=["Cocktails","Recherche"])
async def recherche_cocktail(nom_cocktail: str):
    """Recherche de cocktail"""
    filtre = FiltreCocktail(nom = nom_cocktail)
    cocktails = recherche_service.recherche_cocktail(filtre)
    print(cocktails)
    liste_noms = []
    for c in cocktails:
        liste_noms.append(c.nom)
    return liste_noms

@router.get("/recherche_filtre_cocktail", tags=["Cocktails", "Recherche"])
def recherche_filtre_cocktail(filtre: Annotated[FiltreCocktail, Query()]):
    cocktails = recherche_service.recherche_cocktail(filtre)
    return cocktails


