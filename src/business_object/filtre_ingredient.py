from pydantic import BaseModel


class FiltreIngredient(BaseModel):
    id: int = None
    nom: str = None
    alcoolise: bool = None
    type_ing: str = None
    
    def voir_filtre(self):
        """Permet de voir les filtres appliqués sur les ingrédients"""
        return f"{self.id}, {self.nom}, {self.alcoolise}, {self.type_ing}"
