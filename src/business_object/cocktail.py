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

    categorie : str 
        catégorie de cocktail
    iba : str 
        type de cocktail considéré par l'IBA (the International Bartender Association)
    alcolise : bool
        booléen indiquant si le cocktail contient de l'alcool 
    abv : int
        unité internationale de taux d'alcool par volume 
    verre : str 
        type de verre utilisé pour faire le cocktail
    instructions : str
        instructions pour réaliser le cocktail
    url_image : str 
        potentielle image d'illustration du cocktail
    """


    def __init__(
        self,
        id : int ,
        nom : str,
        nom_alt : str = None,
        tags : str,
        categorie : str ,
        iba : str ,
        alcolise : bool,
        abv : int,
        verre : str ,
        instructions : str,
        url_image : str = None,
    ):
        self.__id = id
        self.__nom = nom
        self.__nom_alt = nom_alt
        self.__tags = tags
        self.__categorie = categorie
        self.__iba = iba
        self.__alcolise = alcolise
        self.__abv = abv
        self.__verre = verre 
        self.__instructions = instructions
        self.__ = url_image