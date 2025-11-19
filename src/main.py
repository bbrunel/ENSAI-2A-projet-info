import logging

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from api.routers import administration, auth, favoris, ingredients, recherche, utilisateur
from utils.log_init import initialiser_logs

app = FastAPI(title="Cocktailopedia", docs_url="/docs", root_path="/proxy/9876")

app.include_router(recherche.router)
app.include_router(auth.router)
app.include_router(favoris.router)
app.include_router(utilisateur.router)
app.include_router(ingredients.router)
app.include_router(administration.router)
initialiser_logs("Webservice")


@app.get("/", include_in_schema=False)
async def redirect_to_docs():
    """Redirect to the API documentation"""
    return RedirectResponse(url="/docs")


# Run the FastAPI application
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=9876)

    logging.info("Arret du Webservice")
