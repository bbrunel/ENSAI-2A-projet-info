from typing import Literal

from pydantic import BaseModel


class FiltreIngredient(BaseModel):
    id: int = None
    nom: str = None
    alcoolise: bool = None
    type_ing: (
        Literal[
            "ricewine",
            "whiskey",
            "stout",
            "beverage",
            "syrup",
            "sambuca",
            "spirit",
            "confectionery",
            "tea",
            "whisky",
            "sugar",
            "liquor",
            "beer",
            "vermouth",
            "soda",
            "port",
            "cordial",
            "garnish",
            "vinegar",
            "cola",
            "alcopop",
            "mix",
            "juice",
            "seasoning",
            "milk",
            "bitters",
            "coffee",
            "rum",
            "softdrink",
            "cider",
            "fruit",
            "brandy",
            "spice",
            "cream",
            "sherry",
            "fruitjuice",
            "sauce",
            "water",
            "liqueur",
            "gin",
            "mixer",
            "confectionery",
            "fortifiedwine",
            "sweet",
            "bitter",
            "mineral",
            "candy",
            "schnapps",
            "liquer",
            "aperitif",
            "flower",
            "tequila",
            "vodka",
            "wine",
            "herb",
        ]
        | None
    ) = None

    def voir_filtre(self):
        """Permet de voir les filtres appliqués sur les ingrédients"""
        return f"{self.id}, {self.nom}, {self.alcoolise}, {self.type_ing}"
