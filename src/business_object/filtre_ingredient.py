from business_object.abstract_filtre import AbstractFiltre

class FiltreIngredient(AbstractFiltre):
    def __init__(self, nom: str = None, alcoolise: bool = None, type_ing: str = None):
        super().__init__(nom, alcoolise)
        self.type_ing = type_ing

    def voir_filtre(self):
        """Permet de voir les filtres appliqués sur les ingrédients"""
        return f'{self.nom}, {self.alcoolise}, {self.type_ing}'
