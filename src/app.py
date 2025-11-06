import logging

from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

from business_object.filtre_cocktail import FiltreCocktail
from business_object.filtre_ingredient import FiltreIngredient

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

# Run the FastAPI application
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=9876)

    logging.info("Arret du Webservice")
