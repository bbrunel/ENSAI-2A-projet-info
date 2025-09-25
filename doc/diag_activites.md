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

## 1er diagramme : global

```mermaid
stateDiagram
    login : Se connecter
    menu_utilisateur : Menu utilisateur
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
    admin_out : Se déconnecter
    list_utilisateurs : Consulter la liste des utilisateurs
    menu_admin : Menu administrateur
    Saisie_a : Saisie
    Saisie_u : Saisie
    
    [*] --> Accueil
    
    Accueil --> Rechercher

    Accueil --> login
    login --> Saisie_u
    Saisie_u --> menu_utilisateur: Saisie valide
    Saisie_u --> login: Saisie invalide
    
    Accueil --> logon

    Accueil --> admin
    admin --> Saisie_a
    Saisie_a --> menu_admin: Saisie valide
    Saisie_a --> admin: Saisie invalide
    
    Accueil --> Quitter
    Quitter --> [*]

    state menu_admin {
      [*] --> list_utilisateurs
      [*] --> admin_out
      admin_out --> [*]: Retour accueil
    }
    
    state menu_utilisateur {
    	[*] --> gerer_ingr
      [*] --> recettes
      [*] --> rec_ingr_manquant
    	[*] --> logout
      logout --> [*]:Retour accueil
    }

    gerer_ingr --> menu_ingr

    state menu_ingr {
      [*] --> Consulter_les_ingrédients
      [*] --> Ajouter_un_ingrédient
      [*] --> Supprimer_un_ingrédient
      [*] --> Retour
      Retour --> [*]: Retour menu utilisateur
        
    }
```

## 2e diagramme : centré sur la connexion

```mermaid
stateDiagram
    login : Se connecter
    menu_utilisateur : Menu utilisateur
    menu_ingr : Gestion des ingrédients
    gerer_ingr : Gérer les ingrédients
    Consulter_les_ingrédients : Consulter les ingrédients
    Ajouter_un_ingrédient : Ajouter un ingrédient
    Supprimer_un_ingrédient : Supprimer un ingrédient
    recettes : Propositions de recettes
    rec_ingr_manquant : Recettes pour lesquelles il manque peu d'ingrédients
    logout : Se déconnecter
    
    [*] --> Accueil

    Accueil --> login

    login --> Saisie
    Saisie --> menu_utilisateur: Saisie valide
    Saisie --> login: Saisie invalide

    state menu_utilisateur {
    	[*] --> gerer_ingr
      [*] --> recettes
      [*] --> rec_ingr_manquant
    	[*] --> logout
      logout --> [*]:Retour accueil
    }

  gerer_ingr --> menu_ingr

    state menu_ingr {
      [*] --> Consulter_les_ingrédients
      [*] --> Ajouter_un_ingrédient
      [*] --> Supprimer_un_ingrédient
      [*] --> Retour
      Retour --> [*]: Retour menu utilisateur
        
    }
```

## 3e diagramme : menu utilisateurs

```mermaid
stateDiagram
    login : Se connecter
    menu_utilisateur : Menu utilisateur
    menu_ingr : Gestion des ingrédients
    gerer_ingr : Gérer les ingrédients
    recettes : Propositions de recettes
    rec_ingr_manquant : Recettes pour lesquelles il manque peu d'ingrédients
    logout : Se déconnecter
    
    [*] --> Accueil

    Accueil --> login

    login --> Saisie
    Saisie --> menu_utilisateur: Saisie valide
    Saisie --> login: Saisie invalide

    state menu_utilisateur {
    	[*] --> gerer_ingr
      [*] --> recettes
      [*] --> rec_ingr_manquant
    	[*] --> logout
      logout --> [*]:Retour accueil
    }

    gerer_ingr --> menu_ingr

```

## 4e diagramme : menu ingrédients

```mermaid
stateDiagram
    login : Se connecter
    menu_utilisateur : Menu utilisateur
    menu_ingr : Gestion des ingrédients
    gerer_ingr : Gérer les ingrédients
    Consulter_les_ingrédients : Consulter les ingrédients
    Ajouter_un_ingrédient : Ajouter un ingrédient
    Supprimer_un_ingrédient : Supprimer un ingrédient
    
    [*] --> Accueil

    Accueil --> login

    login --> Saisie
    Saisie --> menu_utilisateur: Saisie valide
    Saisie --> login: Saisie invalide

    state menu_utilisateur {
    	[*] --> gerer_ingr
    }

  gerer_ingr --> menu_ingr

    state menu_ingr {
      [*] --> Consulter_les_ingrédients
      [*] --> Ajouter_un_ingrédient
      [*] --> Supprimer_un_ingrédient
      [*] --> Retour
      Retour --> [*]: Retour menu utilisateur
        
    }
```

## 5e diagramme : menu administrateur


```mermaid
stateDiagram
    login : Se connecter
    menu_utilisateur : Menu utilisateur
    logon : Créer un compte
    logout : Se déconnecter
    admin : Accès administrateur
    admin_out : Se déconnecter
    list_utilisateurs : Consulter la liste des utilisateurs
    menu_admin : Menu administrateur
    Saisie_u : Saisie
    Saisie_a : Saisie
    
    [*] --> Accueil
    
    Accueil --> Rechercher

    Accueil --> login
    login --> Saisie
    Saisie_u --> menu_utilisateur: Saisie valide
    Saisie_u --> login: Saisie invalide
    
    Accueil --> logon

    Accueil --> admin
    admin --> Saisie
    Saisie_a --> menu_admin: Saisie valide
    Saisie_a --> admin: Saisie invalide
    
    Accueil --> Quitter
    Quitter --> [*]

    state menu_admin {
      [*] --> list_utilisateurs
      [*] --> admin_out
      admin_out --> [*]: Retour accueil
    }

```