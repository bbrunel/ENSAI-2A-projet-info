from typing import Annotated

from fastapi import APIRouter, Depends, Query

from api.securite import get_current_user
from business_object.utilisateur import Utilisateur
from service.favoris_service import FavorisService

router = APIRouter()
favoris_service = FavorisService()


@router.post("/ajout_favori", tags=["Favoris"])
def ajout_favori(
    current_user: Annotated[Utilisateur, Depends(get_current_user)],
    id_cocktail: Annotated[int, Query()],
):
    cocktail = favoris_service.aj_fav_cocktail(current_user.id, id_cocktail)
    return cocktail


@router.get("/liste_favoris", tags=["Favoris"])
def liste_favoris(current_user: Annotated[Utilisateur, Depends(get_current_user)]):
    favs = favoris_service.list_all_fav_cocktails(current_user.id)
    return favs


@router.delete("/supprimer_favori", tags=["Favoris"])
def supprimer_favori(
    current_user: Annotated[Utilisateur, Depends(get_current_user)],
    id_cocktail: Annotated[int, Query()],
):
    favoris_service.suppr_fav_cocktail(current_user.id, id_cocktail)
