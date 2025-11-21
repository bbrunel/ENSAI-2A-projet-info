def combinations(ensemble: set, q: int):
    resultat = []

    def combiner(elements, debut=0, combi_actuelle=[]):
        if len(combi_actuelle) == q:
            resultat.append(set(combi_actuelle))
            return
        for i in range(debut, len(elements)):
            combiner(elements, i + 1, combi_actuelle=combi_actuelle + [elements[i]])

    combiner(list(ensemble))
    return resultat
