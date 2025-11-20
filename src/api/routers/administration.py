from typing import Annotated

from fastapi import APIRouter, Depends, Query

from api.securite import get_current_admin
from business_object.utilisateur import Utilisateur
from service.favoris_service import FavorisService
from service.ingredient_utilisateur_service import IngredientUtilisateurService
from service.utilisateur_service import UtilisateurService

router = APIRouter()


@router.get("/admin/liste_utilisateurs", tags=["Administration"], summary="Lister les utilisateurs")
def liste_utilisateurs(current_admin: Annotated[Utilisateur, Depends(get_current_admin)]):
    return UtilisateurService.lister_tous(True)


@router.delete("/admin/banir", tags=["Administration"], summary="Supprimer un utilisateur")
def supprimer_utilisateur(
    current_admin: Annotated[Utilisateur, Depends(get_current_admin)],
    id_utilisateur: Annotated[int, Query(ge=0)],
):
    utilisateur = UtilisateurService.trouver_par_id(id_utilisateur)
    if utilisateur:
        FavorisService().supprimer_tous(utilisateur.id)
        IngredientUtilisateurService().supprimer_tous(utilisateur)
        return UtilisateurService.supprimer(utilisateur)
    return False


@router.put(
    "/admin/ajouter",
    tags=["Administration"],
    summary="Accorder les droits d'administrateur à un utilisateur",
)
def ajout_admin(
    current_admin: Annotated[Utilisateur, Depends(get_current_admin)],
    id_utilisateur: Annotated[int, Query(ge=0)],
):
    utilisateur = UtilisateurService.trouver_par_id(id_utilisateur)
    if utilisateur:
        utilisateur.admin = True
        return UtilisateurService.modifier(utilisateur)
    return utilisateur


@router.put(
    "/admin/supprimer",
    tags=["Administration"],
    summary="Enlever les droits d'administrateur à un utilisateur",
)
def supprimer_admin(
    current_admin: Annotated[Utilisateur, Depends(get_current_admin)],
    id_utilisateur: Annotated[int, Query(ge=0)],
):
    utilisateur = UtilisateurService.trouver_par_id(id_utilisateur)
    if utilisateur:
        utilisateur.admin = False
        return UtilisateurService.modifier(utilisateur)
    return utilisateur
