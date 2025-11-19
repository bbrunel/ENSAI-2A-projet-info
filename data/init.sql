CREATE EXTENSION pg_trgm;

CREATE TABLE cocktails (
   id_recipe int NOT NULL,
   recipe_name varchar(255) NOT NULL,
   category varchar(255),
   alcoholic boolean,
   glass_type varchar(255),
   instruction text,
   iba_category varchar(255),
   cocktail_pic_url text,
   PRIMARY KEY (id_recipe)
);

CREATE TABLE ingredients (
   id_ingredient int NOT NULL,
   ingredient_name varchar(255) NOT NULL,
   ingredient_type varchar(255),
   description text,
   alcoholic boolean,
   abv int,
   PRIMARY KEY(id_ingredient)
);

CREATE TABLE composition (
   id_composition int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
   id_recipe int NOT NULL,
   id_ingredient int NOT NULL,
   quantity VARCHAR(50),
   FOREIGN KEY(id_recipe) REFERENCES cocktails(id_recipe),
   FOREIGN KEY(id_ingredient) REFERENCES ingredients(id_ingredient)
);

CREATE TABLE users (
   id_user int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
   username varchar(255) NOT NULL UNIQUE,
   hashed_password varchar(255) NOT NULL,
   is_admin boolean DEFAULT FALSE
);

CREATE TABLE have (
   id_user int NOT NULL,
   id_ingredient int NOT NULL,
   PRIMARY KEY (id_user, id_ingredient),
   FOREIGN KEY(id_user) REFERENCES users(id_user),
   FOREIGN KEY(id_ingredient) REFERENCES ingredients(id_ingredient)
);

CREATE TABLE favorites (
   id_user int NOT NULL,
   id_recipe int NOT NULL,
   PRIMARY KEY (id_user, id_recipe),
   FOREIGN KEY(id_user) REFERENCES users(id_user),
   FOREIGN KEY(id_recipe) REFERENCES cocktails(id_recipe)
);
