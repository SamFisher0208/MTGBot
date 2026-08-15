import requests #http library
import json #json library
#import SQLstuff

def getCard(cardType):
  headers = {'user-agent': 'MTGBot/1.0', 'Accept': '*/*'}
  url = f"https://api.scryfall.com/cards/random{cardType}"
  card = requests.get(url, headers=headers)
  jsonData = json.loads(card.text)
  imgURL = jsonData['image_uris']['png']
  return imgURL

def getVibe():
  headers = {'user-agent': 'MTGBot/1.0', 'Accept': '*/*'}
  url = "https://api.scryfall.com/cards/random"
  card = requests.get(url, headers=headers)
  jsonData = json.loads(card.text)
  imgURL = jsonData['image_uris']['png']
  #SQLstuff.updateDB(imgURL)
  return imgURL

def getCreature():
  return getCard("?q=type%3Acreature")

def getInstant():
  return getCard("?q=type%3Ainstant")

def getSorcery():
  return getCard("?q=type%3Asorcery")
