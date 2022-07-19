from namedb import get
from .search import search
from .set import set
def load(user_id: str) -> str:
  if search(user_id) is False: 
    set(user_id, 'en')
    return 'en'
  return get(user_id, categorie="language")
