import requests
import json

#Task 2
def fetch_pokemon(pokemon_name):
    url = (f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}')
    try:
        response = requests.get(url)
        pokemon_data = response.json()
        if isinstance(pokemon_data, dict):
            name = pokemon_data.get('name', 'No Name')
            abilities = pokemon_data.get('abilities', 'No abilities')
            abilities_out = abilities[0]['ability']['name']
            for i in range(1,len(abilities)) :
                abil_out = abilities_out + ', ' + abilities[i]['ability']['name']
            print(f"Name: {name}\nAbilities: {abil_out}")

        else: 
            status = pokemon_data.get('status')
            reason = pokemon_data.get('reason', 'unknown reason')
            print(f"Error {status}: {reason}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        
fetch_pokemon('pikachu')
