import requests #http library
import json #json library
#import SQLstuff

def getCard(cardType):
  headers = {'user-agent': 'MTGBot/1.0', 'Accept': '*/*'}
  card = requests.get(f"https://api.scryfall.com/cards/random{cardType}", headers=headers)
  jsonData = json.loads(card.text)
  imgURL = jsonData['image_uris']['png']
  return imgURL

def getVibe():
  card = requests.get("https://api.scryfall.com/cards/random")
  jsonData = json.loads(card.text)
  print(jsonData)
  imgURL = jsonData['image_uris']['png']
  #SQLstuff.updateDB(imgURL)
  return imgURL

def getCreature():
  return getCard("?q=type%3Acreature")

def getInstant():
  return getCard("?q=type%3Ainstant")

def getSorcery():
  return getCard("?q=type%3Asorcery")
