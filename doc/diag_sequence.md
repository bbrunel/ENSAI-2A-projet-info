# Diagramme de séquence

Ce diagramme est codé avec [mermaid](https://mermaid.js.org/syntax/stateDiagram.html).

J'ai fait le choix de ne représenter qu'une action possible de l'utilisateur pour un soucis de lisibilité.
L'objectif de ce diagramme est de comprendre l'utilité de chaque couche du logiciel et leurs interractions.

```mermaid
sequenceDiagram
   actor User
   participant API
   participant Service
   participant Business Object
   participant DAO
   participant Database@{"type":"database"}
   User->>API: search for cocktails they can make
   API->>Service: calls find_doable_cocktails from UserService
   Service->>DAO: calls list_user_ingredients from UserDAO
   DAO->>Database: retrieve persistent data
   Database->>DAO: send data (list of dictionnaries)
   DAO->>Business Object: instantiate a business object for each ingredient
   Business Object->>DAO: return Ingredient object
   DAO->>Service: returne list of ingredients (business objects)
   Service->>DAO: calls find_cocktails_by_ingredients from CocktailDAO
   DAO->>Database: retrieve persistent data
   Database->>DAO: send data (list of dictionnaries)
   DAO->>Business Object: instantiate a business object for each cocktail
   Business Object->>DAO: return Ingredient object
   DAO->>Service: return list of cocktails (business objects)
   Service->>API: supply the list of cocktails
   API->>User: supply list of cocktails in JSON format
```