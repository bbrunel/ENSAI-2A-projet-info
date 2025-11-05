from abc import ABC, abstractmethod

class AbstractFiltre(ABC):
    def __init__(self, id: int, nom: str = None, alcoolise: bool = None):
        self.id = id
        self.nom = nom
        self.alcoolise = alcoolise

    @abstractmethod
    def voir_filtre(self):
        """Méthode à définir dans les classes enfants"""
        pass