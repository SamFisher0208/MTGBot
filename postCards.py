import requests #http library
import json #json library
import SQLstuff

def getCard(cardType):
  card = requests.get(f"https://api.scryfall.com/cards/random{cardType}")
  jsonData = json.loads(card.text)
  imgURL = jsonData['image_uris']['png']
  return imgURL

def getVibe():
  card = requests.get("https://api.scryfall.com/cards/random")
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
