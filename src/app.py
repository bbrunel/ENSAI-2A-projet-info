import logging

from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

from service.recherche_service import RechercheService
from utils.log_init import initialiser_logs

app = FastAPI(title="Cocktailopedia")

recherche_service = RechercheService()

initialiser_logs("Webservice")

@app.get("/", include_in_schema=False)
async def redirect_to_docs():
    """Redirect to the API documentation"""
    return RedirectResponse(url="/docs")


@app.get("/recherche_cocktail/{nom_cocktail}", tags=["Cocktails","Recherche"])
async def recherche_cocktail(nom_cocktail: str):
    """Recherche de cocktail"""
    filtre = FiltreCocktail(nom = nom_cocktail)
    return RechercheService.recherche_cocktail(filtre)

