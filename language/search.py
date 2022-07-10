from namedb import search as searche
def search(user_id: int):
  return searche(str(user_id), categorie="language")
