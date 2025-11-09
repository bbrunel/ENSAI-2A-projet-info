from typing import Annotated

from fastapi import APIRouter, Query

from api.securite import *
from business_object.filtre_cocktail import FiltreCocktail
from business_object.utilisateur import Utilisateur
from service.recherche_service import RechercheService

router = APIRouter()

recherche_service = RechercheService()


@router.get("/recherche_cocktail/{nom_cocktail}", tags=["Cocktails", "Recherche"])
async def recherche_cocktail(nom_cocktail: str):
    """Recherche de cocktail"""
    filtre = FiltreCocktail(nom=nom_cocktail)
    cocktails = recherche_service.recherche_cocktail(filtre)
    return cocktails


@router.get("/recherche_filtre_cocktail", tags=["Cocktails", "Recherche"])
def recherche_filtre_cocktail(filtre: Annotated[FiltreCocktail, Query()]):
    cocktails = recherche_service.recherche_cocktail(filtre)
    return cocktails


@router.get("/liste_faisables/{nb_manquants}", tags=["Cocktails"])
def liste_cocktail_quasifaisables(
    current_user: Annotated[Utilisateur, Depends(get_current_user)], nb_manquants: int
):
    return recherche_service.liste_cocktails_faisables(current_user, nb_manquants)
