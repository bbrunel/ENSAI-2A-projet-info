# Work in progress, ne pas tenir compte pour le moment...

from unittest.mock import MagicMock

from service.ingredient_utilisateur_service import IngredientUtilisateurService

from dao.ingredient_utilisateur_dao import IngredientUtilisateurDao

from business_object.utilisateur import Utilisateur

from business_object.ingredient import Ingredient


liste_utilisateurs = [
    Utilisateur(pseudo="jp", mdp="1234", statut="utilisateur"),
    Utilisateur(pseudo="lea", mdp="0000", statut="utilisateur"),
    Utilisateur(pseudo="gg", mdp="abcd", staut="utilisateur"),
]

liste_ingredients = [
    Ingredient(id=1, nom="eau", desc="", type="boisson", alcoolise=False, abv=0),
    Ingredient(id=2, nom="citron", desc="", type="fruit frais", alcoolise=False, abv=0),
    Ingredient(id=3, nom="menthe", desc="", type="herbe", alcoolise=False, abv=0),
]



def test_ajout_ingredient_utilisateur_ok():
    """Ajout de l'ingrédient par l'utilisateur réussi."""

    # GIVEN
    pseudo, mdp, statut = "jp", "1234", "utilisateur"
    id, nom, desc, type, alcoolise, abv = 1, "citron", "", "fruit frais", False, 0
    IngredientUtilisateurDao().ajout_ingredient_utilisateur() = MagicMock(return_value=ingredient)

    # WHEN
    utilisateur = UtilisateurService().(pseudo, mdp, age, mail, fan_pokemon)
    ingredient = IngredientService().(id, nom, desc, type, alccolise, abv)

    # THEN
    assert utilisateur.ajout_ingredient_utilisateur == pseudo


def test_ajout_ingredient_utilisateur_echec():
    """Ajout de l'ingredient par l'utilisateur échoué."""

    # GIVEN
    pseudo, mdp, statut = "jp", "1234", 15, "z@mail.oo", True
    IngredientUtilisateurDao().ajout_ingredient_utilisateur = MagicMock(return_value=None)

    # WHEN
    joueur = JoueurService().creer(pseudo, mdp, age, mail, fan_pokemon)

    # THEN
    assert joueur is None


def test_supprimer_ingredient_utilisateur_true():
    """Suppression de l'ingrédient par l'utilisateur réussie."""

    # GIVEN
    JoueurDao().lister_tous = MagicMock(return_value=liste_joueurs)

    # WHEN
    res = JoueurService().lister_tous(inclure_mdp=True)

    # THEN
    assert len(res) == 3
    for joueur in res:
        assert joueur.mdp is not None


def test_supprimer_ingredient_utilisateur_false():
    """Suppression de l'ingrédient par l'utilisateur échouée.
    """


def test_liste_tous_ingredients_utilisateur_ok():
    """La liste des ingrédients de l'utilisateur est bien retournée.
    """

    # GIVEN
    IngredientUtilisateurDao().liste_tous_ingredients_utilisateur() = MagicMock(return_value=liste_ingredients)

    # WHEN
    res = UtilisateurService().liste_tous_ingredients_utilisateur()

    # THEN
    assert len(res) == 3
    for joueur in res:
        assert not joueur.mdp

    # # GIVEN
    # pseudo = "lea"

    # # WHEN
    # JoueurDao().lister_tous = MagicMock(return_value=liste_joueurs)
    # res = JoueurService().pseudo_deja_utilise(pseudo)

    # # THEN
    # assert res


def test_liste_tous_ingredients_utilisateur_echec():
    """La liste des ingrédients de l'utilisateur n'est pas retournée.
    (Préciser dans quel(s) cas.)
    """

    # GIVEN
    pseudo = "chaton"

    # WHEN
    JoueurDao().lister_tous = MagicMock(return_value=liste_joueurs)
    res = JoueurService().pseudo_deja_utilise(pseudo)

    # THEN
    assert not res


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
