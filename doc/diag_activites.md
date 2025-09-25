# Diagramme d'activité

> Un diagramme UML d'activité modélise le flux de travail d'un processus, montrant la séquence d'activités et de décisions dans un système. Il illustre comment les actions s'enchaînent et comment les choix sont faits.

Ce diagramme est codé avec [mermaid](https://mermaid.js.org/syntax/stateDiagram.html) :

- avantage : facile à coder
- inconvénient : on ne maîtrise pas bien l'affichagev

Pour afficher ce diagramme dans VScode :

- à gauche aller dans **Extensions** (ou CTRL + SHIFT + X)
- rechercher `mermaid`
  - installer l'extension **Markdown Preview Mermaid Support**
- revenir sur ce fichier
  - faire **CTRL + K**, puis **V**


```mermaid
stateDiagram
    login : Se connecter
    menu_joueur : Menu Joueur
    menu_ingr : Gestion des ingrédients
    logon : Créer un compte
    gerer_ingr : Gérer les ingrédients
    Consulter_les_ingrédients : Consulter les ingrédients
    Ajouter_un_ingrédient : Ajouter un ingrédient
    Supprimer_un_ingrédient : Supprimer un ingrédient
    recettes : Propositions de recettes
    rec_ingr_manquant : Recettes pour lesquelles il manque peu d'ingrédients
    logout : Se déconnecter
    admin : Accès administrateur
    list_joueurs : Lister les joueurs
    
    [*] --> Accueil
    
    Accueil --> Rechercher
    
    Accueil --> logon

    Accueil --> admin

    Accueil --> login
    login --> menu_joueur
    
    Accueil --> Quitter
    Quitter --> [*]

    admin --> list_joueurs
    
    state menu_joueur {
    	[*] --> gerer_ingr
      [*] --> recettes
      [*] --> rec_ingr_manquant
    	[*] --> logout
      logout --> [*]:retour accueil
    }

  gerer_ingr --> menu_ingr

    state menu_ingr {
      [*] --> Consulter_les_ingrédients
      [*] --> Ajouter_un_ingrédient
      [*] --> Supprimer_un_ingrédient
        
    }
```