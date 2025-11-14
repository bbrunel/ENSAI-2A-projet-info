from pydantic import BaseModel

class FiltreCocktail(BaseModel):
    id: int = None
    nom: str = None
    alcoolise: bool = None
    tags: list[str] = None
    iba: str = None
    categorie: str = None
    verre: str = None

    def voir_filtre(self):
        """Permet de voir les filtres appliqués sur les cocktails"""
        return f"{self.id}, {self.nom}, {self.alcoolise}, {self.tags}, {self.iba}, \
{self.categorie}, {self.verre}"
