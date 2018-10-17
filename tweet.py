"""
Ten plik bierze wszystkie dane wygenerowane przez poprzednie skrypty i umieszcza je na Twitterze.
"""
import os

# Kolejnosc wykonywania dzialan:

# 1. Zdobadz klatke z Youtube.
import randomowa_klatka
# 2. Zdobadz cytat.
import zdobadz_cytat
# 3. Polacz cytat i klatke w jednym obrazie.
import obrazek


from obrazek import BibliaCytat
cytat = BibliaCytat['cytat']
ksiega = BibliaCytat['ksiega']
autor = BibliaCytat['autor']

status = f'Cytat na dziś!\n{ksiega}: {autor}.'

# python-twitter
import twitter

if ids.on_heroku:
    consumer_key = os.environ['consumer_key']
    consumer_secret = os.environ['consumer_secret']
    access_token = os.environ['access_token']
    access_token_secret = os.environ['access_token_secret']
else:
    import config
    consumer_key = config.consumer_key
    consumer_secret = config.consumer_secret
    access_token = config.access_token
    access_token_secret = config.access_token_secret

api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token,
                  access_token_secret=access_token_secret)


print(api.VerifyCredentials)
api.PostUpdate(status, 'klatka_ready.jpg')

# Posprzataj
os.remove('klatka_ready.jpg')
os.remove('klatka.jpg')
