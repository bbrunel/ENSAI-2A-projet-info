from typing import Annotated

from fastapi import APIRouter, Depends, Query

from api.securite import get_current_user
from business_object.filtre_cocktail import FiltreCocktail
from business_object.utilisateur import Utilisateur
from service.recherche_service import RechercheService

router = APIRouter()

recherche_service = RechercheService()


@router.get("/recherche_cocktail", tags=["Cocktails"])
async def recherche_cocktail(nom_cocktail: Annotated[str, Query()]):
    """Recherche de cocktail"""
    filtre = FiltreCocktail(nom=nom_cocktail)
    cocktails = recherche_service.recherche_cocktail(filtre)
    return cocktails


@router.get("/recherche_filtre_cocktail", tags=["Cocktails"])
def recherche_filtre_cocktail(
    filtre: Annotated[FiltreCocktail, Query()],
):
    cocktails = recherche_service.recherche_cocktail(filtre)
    return cocktails


@router.get("/liste_faisables", tags=["Cocktails"])
def liste_cocktail_quasifaisables(
    current_user: Annotated[Utilisateur, Depends(get_current_user)],
    nb_manquants: Annotated[int, Query(ge=0)],
):
    return recherche_service.liste_cocktails_faisables(current_user, nb_manquants)
