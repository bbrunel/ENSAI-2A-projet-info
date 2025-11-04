from abstractFiltre import AbstractFiltre

class FiltreCocktail(AbstractFiltre):
    def __init__(self, nom: str = None, alcoolise: bool = None,
                 tags=None,
                 iba: str = None,
                 categorie: str = None,
                 verre: str = None):
        super().__init__(nom, alcoolise)
        self.tags = tags if tags is not None else []
        self.iba = iba
        self.categorie = categorie
        self.verre = verre

    def voir_filtre(self):
        """Permet de voir les filtres appliqués sur les cocktails"""
        return f'{self.nom}, {self.alcoolise}, {self.tags}, {self.iba}, \
{self.categorie}, {self.verre}'