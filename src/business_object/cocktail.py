class Cocktail():
    """
    List of cocktails

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
        type de cocktail considéré par l'IBA (the International Bartender Association)
    alcolise : bool
        booléen indiquant si le cocktail contient de l'alcool 
    verre : str 
        type de verre utilisé pour faire le cocktail
    instructions : str
        instructions pour réaliser le cocktail
    url_image : str 
        potentielle image d'illustration du cocktail
    """


    def __init__(
        self,
        id : int,
        nom : str,
        nom_alt : str = None,
        tags : str = None,
        categorie : str = None,
        iba : str = None,
        alcolise : bool = True,
        verre : str = None,
        instructions : str = None,
        url_image : str = None,
    ):
        self.id = id
        self.nom = nom
        self.nom_alt = nom_alt
        self.tags = tags
        self.categorie = categorie
        self.iba = iba
        self.alcolise = alcolise
        self.verre = verre 
        self.instructions = instructions
        self.url_image = url_image