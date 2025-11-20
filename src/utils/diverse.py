import unicodedata


def unaccent(s: str) -> str:
    """
    Cette fonction débarasse une chaîne de caractère des ses accents
    Par exemple unaccent('chaîne') renvoie 'chaine'
    Params
    ------
        s: str
    Returns
    -------
        str
    """
    n = unicodedata.normalize("NFKD", s)
    res = "".join([c for c in n if not unicodedata.combining(c)])
    return res


def only_alpha_lower(s: str | None) -> str | None:
    """Supprime les caractères non-alphabétiques d'une chaîne de caractères"""
    if s is None:
        return None
    new_str = ""
    for c in s:
        if c.isalpha() or c == " ":
            new_str += c
    return new_str.lower()
