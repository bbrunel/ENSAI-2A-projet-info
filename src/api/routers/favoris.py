from typing import Annotated

from fastapi import APIRouter, Depends, Query

from api.securite import get_current_user
from business_object.utilisateur import Utilisateur
from service.favoris_service import FavorisService

router = APIRouter()
favoris_service = FavorisService()


@router.put("/favoris/ajouter", tags=["Favoris"], summary="Ajouter un cocktail aux favoris")
def ajout_favori(
    current_user: Annotated[Utilisateur, Depends(get_current_user)],
    id_cocktail: Annotated[int, Query(title="ID du Cocktail")],
    note_perso: Annotated[str, Query(title="Notes personelles")] = None,
):
    cocktail = favoris_service.aj_fav_cocktail(current_user.id, id_cocktail, note_perso)
    return cocktail


@router.get("/favoris/liste", tags=["Favoris"], summary="Lister les favoris")
def liste_favoris(current_user: Annotated[Utilisateur, Depends(get_current_user)]):
    favs = favoris_service.list_all_fav_cocktails(current_user.id)
    return favs


@router.delete("/favoris/supprimer", tags=["Favoris"], summary="Supprimer un cocktail des favoris")
def supprimer_favori(
    current_user: Annotated[Utilisateur, Depends(get_current_user)],
    id_cocktail: Annotated[int, Query()],
):
    favoris_service.suppr_fav_cocktail(current_user.id, id_cocktail)
