import logging

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import RedirectResponse

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
    cocktails = RechercheService().recherche_cocktail(filtre)
    print(cocktails)
    liste_noms = []
    for c in cocktails:
        liste_noms.append(c.nom)
    return liste_noms

@app.get("/recherche_filtre_cocktail", tags=["Cocktails", "Recherche"])
def recherche_filtre_cocktail(filtre: Annotated[FiltreCocktail, Query()]):
    cocktails = RechercheService().recherche_cocktail(filtre)
    return cocktails

# Run the FastAPI application
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=9876)

    logging.info("Arret du Webservice")
