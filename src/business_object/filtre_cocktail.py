from typing import Literal

from pydantic import BaseModel


class FiltreCocktail(BaseModel):
    id: int = None
    nom: str = None
    alcoolise: bool = None
    tags: list[str] = None
    iba: Literal["new era drinks", "unforgettables", "contemporary classics"] | None = None
    categorie: (
        Literal[
            "beer",
            "soft drink",
            "coffee  tea",
            "punch  party drink",
            "cocktail",
            "ordinary drink",
            "shake",
            "shot",
            "homemade liqueur",
            "other  unknown",
            "cocoa",
        ]
        | None
    ) = None
    verre: (
        Literal[
            "highball glass",
            "cordial glass",
            "pitcher",
            "punch bowl",
            "beer pilsner",
            "mason jar",
            "balloon glass",
            "cocktail glass",
            "champagne flute",
            "collins glass",
            "beer mug",
            "whiskey sour glass",
            "coffee mug",
            "oldfashioned glass",
            "copper mug",
            "white wine glass",
            "hurricane glass",
            "whiskey glass",
            "martini glass",
            "brandy snifter",
            "shot glass",
            "margarita glass",
            "irish coffee cup",
            "coupe glass",
            "pousse cafe glass",
            "jar",
            "beer glass",
            "nick and nora glass",
            "wine glass",
            "margaritacoupette glass",
            "pint glass",
        ]
        | None
    ) = None

    def voir_filtre(self):
        """Permet de voir les filtres appliqués sur les cocktails"""
        return f"{self.id}, {self.nom}, {self.alcoolise}, {self.tags}, {self.iba}, \
{self.categorie}, {self.verre}"
