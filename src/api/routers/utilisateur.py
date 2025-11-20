from typing import Annotated

from fastapi import APIRouter, Depends, Form

from api.securite import get_current_user, get_password_hash
from business_object.utilisateur import Utilisateur
from service.favoris_service import FavorisService
from service.ingredient_utilisateur_service import IngredientUtilisateurService
from service.utilisateur_service import UtilisateurService

router = APIRouter()


@router.post("/creer_compte", tags=["Utilisateur"])
def creer_compte(
    username: Annotated[str, Form(description="Nom d'utilisateur", min_length=1)],
    password: Annotated[str, Form(description="Mot de passe", min_length=7)],
):
    return UtilisateurService.creer(username, get_password_hash(password))


@router.put("/modifier_mdp", tags=["Utilisateur"])
def modifier_mdp(
    current_user: Annotated[Utilisateur, Depends(get_current_user)],
    password: Annotated[str, Form(description="Nouveau mot de passe", min_length=7)],
):
    current_user.mdp = get_password_hash(password)
    return UtilisateurService.modifier(current_user)


@router.put("/modifier_nom_utilisateur", tags=["Utilisateur"])
def modifier_nom(
    current_user: Annotated[Utilisateur, Depends(get_current_user)],
    username: Annotated[str, Form(description="Nouveau nom d'utilisateur", min_length=1)],
):
    current_user.nom_utilisateur = username
    return UtilisateurService.modifier(current_user)


@router.delete("/supprimer_mon_compte", tags=["Utilisateur"])
def supprimer_mon_compte(current_user: Annotated[Utilisateur, Depends(get_current_user)]):
    FavorisService().supprimer_tous(current_user.id)
    IngredientUtilisateurService().supprimer_tous(current_user)
    return UtilisateurService.supprimer(current_user)
