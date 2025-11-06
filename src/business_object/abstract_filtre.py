from abc import ABC, abstractmethod

class AbstractFiltre(ABC):
    def __init__(self, nom: str = None, alcoolise: bool = None):
        self.nom = nom
        self.alcoolise = alcoolise

    @abstractmethod
    def voir_filtre(self):
        """Méthode à définir dans les classes enfants"""
        pass
