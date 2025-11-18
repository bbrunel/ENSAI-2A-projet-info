from typing import Annotated

from fastapi import APIRouter, Depends, Form

from api.securite import get_current_user, get_password_hash
from service.utilisateur_service import UtilisateurService

router = APIRouter()


@router.post("/creer_compte", tags=["Utilisateur"])
def creer_compte(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return UtilisateurService.creer(username, get_password_hash(password))


@router.delete("/supprimer_compte", tags=["Utilisateur"])
def supprimer_compte(current_user: Annotated[str, Depends(get_current_user)]):
    return UtilisateurService.supprimer(current_user)
