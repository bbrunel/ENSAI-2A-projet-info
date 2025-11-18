from typing import Annotated

from fastapi import APIRouter, Depends

from api.securite import get_current_user
from business_object.utilisateur import Utilisateur
from service.ingredient_utilisateur_service import IngredientUtilisateurService

router = APIRouter()


@router.get("/liste_ingredients", tags=["Ingrédients"])
def liste_ingredient(current_user: Annotated[Utilisateur, Depends(get_current_user)]):
    return IngredientUtilisateurService().liste_tous_ingredients_utilisateur(current_user)
