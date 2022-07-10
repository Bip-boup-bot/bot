from namedb import get
def translate(sentence: str, language: str):
  return get(sentence, categorie=language)
