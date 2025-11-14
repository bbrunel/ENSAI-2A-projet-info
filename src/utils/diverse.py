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
