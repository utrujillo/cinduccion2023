# pip install requests
import requests
import pprint as pp

api_url = "https://pokeapi.co/api/v2/pokemon/charizard"
response = requests.get(api_url)
charizard = response.json()

pp.pprint(charizard['types'][0]['type']['name'])