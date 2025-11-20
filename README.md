# Projet informatique de 2ème année ENSAI

Cette application est une API permettant d'interroger une base de données
de cocktails et d'ingrédients afin de trouver des idées de recettes en
fonction des ingrédients que vous possédez. L'utilisateur peut créer un
compte, ajouter des cocktails en favoris et des ingrédients qu'il possède
dans son inventaire.

Pour lancer l'API la commande à exécuter est l'une des suivantes:
```bash
uv run src/main.py
python src/main.py
```

Il faut au préalable initialiser la base de données PostgreSQL avec:
```bash
uv run src/utils/init_database.sql
```