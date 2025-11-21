from typing import Annotated

from fastapi import APIRouter, Depends, Query

from api.securite import get_current_user
from business_object.utilisateur import Utilisateur
from service.ingredient_service import IngredientService
from service.ingredient_utilisateur_service import IngredientUtilisateurService

router = APIRouter()


@router.get(
    "/inventaire/liste", tags=["Inventaire"], summary="Lister les ingrédients de l'inventaire"
)
def liste_ingredients_inventaire(current_user: Annotated[Utilisateur, Depends(get_current_user)]):
    return IngredientUtilisateurService().liste_tous_ingredients_utilisateur(current_user)


@router.put(
    "/inventaire/ajouter",
    tags=["Inventaire"],
    summary="Ajouter un ingrédient dans l'inventaire",
)
def ajout_ing_inventaire(
    current_user: Annotated[Utilisateur, Depends(get_current_user)], id_ing: Annotated[int, Query()]
):
    ingredient = IngredientService().verifier_ingredient(id_ing)
    return IngredientUtilisateurService().ajout_ingredient_utilisateur(current_user, ingredient)


@router.delete(
    "/inventaire/supprimer", tags=["Inventaire"], summary="Supprimer un ingrédient de l'inventaire"
)
def supprime_ing_inventaire(
    current_user: Annotated[Utilisateur, Depends(get_current_user)], id_ing: Annotated[int, Query]
):
    ingredient = IngredientService().verifier_ingredient(id_ing)
    return IngredientUtilisateurService().supprimer_ingredient_utilisateur(current_user, ingredient)
