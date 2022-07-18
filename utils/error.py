from os import system
def st(status_code: int):
  if status_code == 200: 
    return
  elif status_code == 401: 
    raise ValueError('Invalid token')
  elif status_code == 400:
    raise ValueError('invalid payload')
  elif status_code == 429: 
    raise ValueError("RATE LIMITED")
  elif status_code == 404:
    raise ValueError('Not found')
  else:
    raise ValueError("invalid shit")
