from pydantic import BaseModel


class Cocktail(BaseModel):
    """
    Liste de cocktails

    Paramètres
    ----------
    id : int
        id d'un cocktail
    nom : str
        nom usuel d'un cocktail
    nom_alt : str
        potentiel autre nom donné à un cocktail
    tags : str
        Les tags attribués au cocktail
    categorie : str
        catégorie du cocktail
    iba : str
        type de cocktail considéré par l'IBA
        (the International Bartender Association)
    alcolise : bool
        booléen indiquant si le cocktail contient de l'alcool
    verre : str
        type de verre utilisé pour faire le cocktail
    instructions : str
        instructions pour réaliser le cocktail
    url_image : str
        potentielle image d'illustration du cocktail
    """

    id: int
    nom: str
    nom_alt: str | None = None
    tags: str | None = None
    categorie: str | None = None
    iba: str | None = None
    alcoolise: bool | None = True
    verre: str | None = None
    instructions: str | None = None
    url_image: str | None = None
