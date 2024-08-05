import requests

#Task 3
def fetch_pokemon_data(pokemon_name):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'
    try:
        #
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

def calculate_average_weight(pokemon_list):
    weight_list = []
    output = 'The average weight of '
    for pokemon in pokemon_list:
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
        response = requests.get(url)
        pokemon_data = response.json()
        if isinstance(pokemon_data, dict):
            name = pokemon_data.get('name','No Name')
            weight = pokemon_data.get('weight','No Weight')
            if pokemon_list.index(pokemon) == 0:
                output = output + name
            elif pokemon_list.index(pokemon) == (len(pokemon_list) - 1):
                output = output + ', and ' + name
            else:
                output = output + ', ' + name
            weight_list.append(int(weight))
        else:
            status = pokemon_data.get('status')
            reason = pokemon_data.get('reason', 'unknown reason')
            print(f"Error {status}: {reason}")
    
    average = sum(weight_list) / len(weight_list)
    output = output + f" is {average} hectograms or {average * 100} grams"
    print(output)
        
pokemon_names = ['pikachu', 'bulbasaur', 'charmander']

for pokemon in pokemon_names:
    fetch_pokemon_data(pokemon)

calculate_average_weight(pokemon_names)

