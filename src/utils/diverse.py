import unicodedata

def unaccent(s: str) -> str:
    n = unicodedata.normalize('NFKD', s)
    res = ''.join([c for c in n if not unicodedata.combining(c)])
    return res
