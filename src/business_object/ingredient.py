class Ingredient:
    """Objets représentant des ingrédients.
    """

    def __init__(self, id: int, nom: str, desc: str, type: str, alcoolise: bool, abv: int):
        self.id = id
        self.nom = nom
        self.desc = desc
        self.type = type
        self.alcoolise = alcoolise
        self.abv = abv

    def __str__(self):
        return f"Ingredient({self.id}, {self.nom})"