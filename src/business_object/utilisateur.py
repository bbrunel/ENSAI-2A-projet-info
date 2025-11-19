class Utilisateur:
    """
    Classe métier représentant un utilisateur de l'application "À Portée de Verre".

    Attributs:
        id : int
            Identifiant unique de l'utilisateur (clé primaire)
        nom_utilisateur : str
            Nom d'utilisateur unique pour la connexion
        mdp : str
            Mot de passe hashé de l'utilisateur
    """

    def __init__(
        self, id: int = None, nom_utilisateur: str = None, mdp: str = None, admin: bool = False
    ):
        """
        Constructeur de la classe Utilisateur.

        Args:
            id: Identifiant unique (généré par la base de données)
            nom_utilisateur: Nom d'utilisateur pour l'authentification
            mdp: Mot de passe hashé
        """
        self.id = id
        self.nom_utilisateur = nom_utilisateur
        self.mdp = mdp
        self.admin = admin

    def __str__(self):
        """
        Représentation lisible de l'utilisateur.
        """
        return f"Utilisateur(id={self.id}, nom_utilisateur='{self.nom_utilisateur}')"

    def as_list(self):
        """
        Retourne les attributs sous forme de liste pour l'affichage tabulaire.

        Returns:
            list: [id, nom_utilisateur] pour l'affichage
        """
        return [self.id, self.nom_utilisateur]
