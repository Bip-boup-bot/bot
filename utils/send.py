import requests
from .url import url
from .error import st
from os import environ
def send_msg(id: int, payload: dict) -> None:
  r = requests.post(f'{url}/channels/{id}/messages', json=payload, headers={"authorization": "Bot " + environ['token']})
  st(r.status_code)
  return None
