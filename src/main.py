import logging

from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse

from utils.log_init import initialiser_logs

from api.routers import recherche

app = FastAPI(title="Cocktailopedia")

app.include_router(recherche.router)
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
