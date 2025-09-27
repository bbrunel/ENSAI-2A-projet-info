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


## 1er diagramme : global bis

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
    Rechercher_a : Rechercher une recette
    Rechercher_u : Rechercher une recette
    Supp : Supprimer un compte
    
    [*] --> Accueil

    state Accueil {
      [*] --> Rechercher_a
      [*] --> login
      [*] --> logon
      [*] --> admin
      [*] --> Quitter
    }

    login --> Saisie_u
    Saisie_u --> menu_utilisateur: Saisie valide
    Saisie_u --> login: Saisie invalide

    admin --> Saisie_a
    Saisie_a --> menu_admin: Saisie valide
    Saisie_a --> admin: Saisie invalide

    Quitter --> [*]

    state menu_admin {
      [*] --> list_utilisateurs
      [*] --> Supp
      [*] --> admin_out
      admin_out --> [*]: Retour accueil
    }
    
    state menu_utilisateur {
    	[*] --> gerer_ingr
      [*] --> recettes
      [*] --> rec_ingr_manquant
      [*] --> Rechercher_u
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

## 2e diagramme : accueil

```mermaid
stateDiagram
    login : Se connecter
    logon : Créer un compte
    admin : Accès administrateur
    
    [*] --> Accueil

    state Accueil {
      [*] --> Rechercher
      [*] --> login
      [*] --> logon
      [*] --> admin
      [*] --> Quitter
      Quitter --> [*]
    }

```


## 2e diagramme : accueil sans menu

```mermaid
stateDiagram
    login : Se connecter
    logon : Créer un compte
    admin : Accès administrateur
    
    [*] --> Accueil
    
    Accueil --> Rechercher

    Accueil --> login
    
    Accueil --> logon

    Accueil --> admin
    
    Accueil --> Quitter
    Quitter --> [*]

```


## 3e diagramme : centré sur la connexion

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
    Rechercher : Rechercher une recette
    gerer_fav : Favoris
    menu_fav : Gestions des favoris
    add_fav : Mettre en favori
    supp_fav : Supprimer des favoris
    list_fav : Consulter les favoris
    Retour_f : Retour
    modif_compte : Modifier les informations de connexion

    
    [*] --> Accueil

    Accueil --> login

    login --> Saisie
    Saisie --> menu_utilisateur: Saisie valide
    Saisie --> login: Saisie invalide

    state menu_utilisateur {
    	[*] --> gerer_ingr
      [*] --> gerer_fav
      [*] --> recettes
      [*] --> rec_ingr_manquant
      [*] --> Rechercher
      [*] --> modif_compte
    	[*] --> logout
      logout --> [*]:Retour accueil
    }

  gerer_ingr --> menu_ingr

  gerer_fav --> menu_fav

  state menu_ingr {
    [*] --> Consulter_les_ingrédients
    [*] --> Ajouter_un_ingrédient
    [*] --> Supprimer_un_ingrédient
    [*] --> Retour
    Retour --> [*]: Retour menu utilisateur
      
  }
    state menu_fav {
      [*] --> list_fav
      [*] --> add_fav
      [*] --> supp_fav
      [*] --> Retour_f
      Retour_f --> [*]: Retour menu utilisateur
    }


```


## 3e diagramme : ingrédients et favoris

```mermaid
stateDiagram
    login : Se connecter
    menu_utilisateur : Menu utilisateur
    menu_ingr : Gestion des ingrédients
    gerer_ingr : Gérer les ingrédients
    Consulter_les_ingrédients : Consulter les ingrédients
    Ajouter_un_ingrédient : Ajouter un ingrédient
    Supprimer_un_ingrédient : Supprimer un ingrédient
    gerer_fav : Favoris
    menu_fav : Gestions des favoris
    add_fav : Mettre en favori
    supp_fav : Supprimer des favoris
    list_fav : Consulter les favoris
    Retour_f : Retour

    
    [*] --> Accueil

    Accueil --> login

    login --> Saisie
    Saisie --> menu_utilisateur: Saisie valide
    Saisie --> login: Saisie invalide

    menu_utilisateur --> gerer_ingr
    menu_utilisateur --> gerer_fav


  gerer_ingr --> menu_ingr

  gerer_fav --> menu_fav

  state menu_ingr {
    [*] --> Consulter_les_ingrédients
    [*] --> Ajouter_un_ingrédient
    [*] --> Supprimer_un_ingrédient
    [*] --> Retour
    Retour --> [*]: Retour menu utilisateur
      
  }
    state menu_fav {
      [*] --> list_fav
      [*] --> add_fav
      [*] --> supp_fav
      [*] --> Retour_f
      Retour_f --> [*]: Retour menu utilisateur
    }


```

## 4e diagramme : menu utilisateurs

```mermaid
stateDiagram
    login : Se connecter
    menu_utilisateur : Menu utilisateur
    menu_ingr : Gestion des ingrédients
    gerer_ingr : Gérer les ingrédients
    recettes : Propositions de recettes
    rec_ingr_manquant : Recettes pour lesquelles il manque peu d'ingrédients
    logout : Se déconnecter
    Rechercher : Rechercher une recette
    
    [*] --> Accueil

    Accueil --> login

    login --> Saisie
    Saisie --> menu_utilisateur: Saisie valide
    Saisie --> login: Saisie invalide

    state menu_utilisateur {
    	[*] --> gerer_ingr
      [*] --> gerer_fav
      [*] --> recettes
      [*] --> rec_ingr_manquant
      [*] --> Rechercher
    	[*] --> logout
      logout --> [*]:Retour accueil
    }

    gerer_ingr --> menu_ingr

    gerer_fav --> menu_fav

    state menu_ingr {
      [*] --> Consulter_les_ingrédients
      [*] --> Ajouter_un_ingrédient
      [*] --> Supprimer_un_ingrédient
      [*] --> Retour
      Retour --> [*]: Retour menu utilisateur
        
    }


```

## 5e diagramme : menu ingrédients

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
      [*] --> gerer_fav
    }

  gerer_ingr --> menu_ingr

  gerer_fav --> menu_fav

    state menu_ingr {
      [*] --> Consulter_les_ingrédients
      [*] --> Ajouter_un_ingrédient
      [*] --> Supprimer_un_ingrédient
      [*] --> Retour
      Retour --> [*]: Retour menu utilisateur
        
    }

    state menu_fav {
      [*] --> list_fav
      [*] --> add_fav
      [*] --> supp_fav
      [*] --> Retour_f
      Retour_f --> [*]: Retour menu utilisateur
    }
```

## 6e diagramme : menu administrateur


```mermaid
stateDiagram
    admin : Accès administrateur
    admin_out : Se déconnecter
    list_utilisateurs : Consulter la liste des utilisateurs
    menu_admin : Menu administrateur
    supp_compte : Supprimer un compte
    modif_compte : Modifier les informations de connexion
    
    [*] --> Accueil

    Accueil --> admin
    admin --> Saisie
    Saisie --> menu_admin: Saisie valide
    Saisie --> admin: Saisie invalide

    state menu_admin {
      [*] --> modif_compte
      [*] --> list_utilisateurs
      [*] --> supp_compte
      [*] --> admin_out
      admin_out --> [*]: Retour accueil
    }

```