from typing import Annotated

from fastapi import APIRouter, Depends, Query

from api.securite import get_current_user
from business_object.filtre_cocktail import FiltreCocktail
from business_object.filtre_ingredient import FiltreIngredient
from business_object.utilisateur import Utilisateur
from service.cocktail_service import CocktailService
from service.recherche_service import RechercheService

router = APIRouter()

recherche_service = RechercheService()


@router.get("/cocktails/recherche", tags=["Cocktails"], summary="Rechercher des cocktails")
async def recherche_cocktail(nom_cocktail: Annotated[str, Query()]):
    """Recherche de cocktail"""
    filtre = FiltreCocktail(nom=nom_cocktail)
    cocktails = recherche_service.recherche_cocktail(filtre)
    return cocktails


@router.get(
    "/cocktails/recherche_filtre",
    tags=["Cocktails"],
    summary="Rechercher des cocktails (avec filtre)",
)
def recherche_filtre_cocktail(
    filtre: Annotated[FiltreCocktail, Query()],
):
    cocktails = recherche_service.recherche_cocktail(filtre)
    return cocktails


@router.get(
    "/cocktails/faisables",
    tags=["Cocktails"],
    summary="Lister les cocktails (quasi-)faisables",
    description=(
        "Le nombre d'ingrédients supplémentaires fait référence au nombre d'ingrédients"
        " intervenants dans la conception du cocktail qui ne sont pas dans l'inventaire."
        " S'il vaut 0 alors le cocktail est faisable avec l'inventaire uniquement"
    ),
)
def liste_cocktail_quasifaisables(
    current_user: Annotated[Utilisateur, Depends(get_current_user)],
    nb_manquants: Annotated[
        int, Query(ge=0, description="Nombre d'ingrédients supplémentaires")
    ] = 0,
):
    return recherche_service.liste_cocktails_faisables(current_user, nb_manquants)


@router.get(
    "/cocktails/liste_ingredients",
    tags=["Cocktails"],
    summary="Lister les ingrédients d'un cocktail",
)
def liste_ingredients_cocktail(id_cocktail: Annotated[int, Query(ge=0)]):
    return CocktailService().ingredient_cocktail(id_cocktail)


@router.get(
    "/ingredients/recherche_filtre",
    tags=["Ingrédients"],
    summary="Rechercher des ingrédients (avec filtre)",
)
def recherche_ingredient(filtre: Annotated[FiltreIngredient, Query()]):
    return recherche_service.recherche_ingredient(filtre)


@router.get(
    "/ingredients/liste_course_optimale", tags=["Ingrédients"], summary="Liste de course optimale"
)
def liste_course_optimale(
    current_user: Annotated[Utilisateur, Depends(get_current_user)],
    nb_ing_achetes: Annotated[int, Query(description="Nombre d'ingrédient à acheter", le=20, ge=1)],
):
    return recherche_service.recherche_ingredients_optimaux(current_user, nb_ing_achetes)
