from graphviz import Digraph

# Création du graphe UML vs MPD
dot = Digraph("Comparaison", format="png")
dot.attr(rankdir="LR", fontsize="12")

# Cluster UML
with dot.subgraph(name="cluster_uml") as c:
    c.attr(label="Diagramme de classes UML", style="rounded", color="lightblue")
    
    c.node("EtudiantU", """Etudiant
-----------------
- nom: String
- prenom: String
- dateNaiss: Date
+ sInscrire()""", shape="record")
    
    c.node("CoursU", """Cours
-----------------
- intitule: String""", shape="record")
    
    c.node("InscriptionU", """Inscription
-----------------
- dateInscr: Date""", shape="record")
    
    c.edge("EtudiantU", "InscriptionU", label="1..*")
    c.edge("CoursU", "InscriptionU", label="1..*")

# Cluster MPD
with dot.subgraph(name="cluster_mpd") as c:
    c.attr(label="Modèle Physique de Données (MPD)", style="rounded", color="lightgrey")
    
    c.node("EtudiantM", """Etudiant
-----------------
id_etudiant INT PK
nom VARCHAR(100) NOT NULL
prenom VARCHAR(100)
date_naissance DATE""", shape="record")
    
    c.node("CoursM", """Cours
-----------------
id_cours INT PK
intitule VARCHAR(100) NOT NULL""", shape="record")
    
    c.node("InscriptionM", """Inscription
-----------------
id_etudiant INT FK
id_cours INT FK
date_inscription DATE
PK(id_etudiant, id_cours)""", shape="record")
    
    c.edge("EtudiantM", "InscriptionM", label="FK")
    c.edge("CoursM", "InscriptionM", label="FK")

# Génération du fichier
output_path = "/mnt/data/comparaison_uml_mpd"
dot.render(output_path, format="png", cleanup=True)

output_path + ".png"
