import requests
from operator import itemgetter

def fetch_planet_data():
    try:
        #connect and grab response from The Solar System OpenData
        url = "https://api.le-systeme-solaire.net/rest/bodies/"
        response = requests.get(url)
        planets = response.json()['bodies']
        
        #Heading for table
        print("\033[4m|Planet Name |Mass            |Orbit Period    |\033[0m")
        
        #process each planet info
        planet_list = []
        for planet in planets:
            if planet['isPlanet']:
                #store planet name, mass as kg, and orbit period as days
                name = planet['englishName']
                mass = planet['mass']['massValue'] * pow(10, planet['mass']['massExponent'])
                orbit_period = planet['sideralOrbit']
                
                #spaces for formatting table
                name_spaces = 12 - len(name)
                orbits_spaces = 16 - (len(str(orbit_period)) + 5)

                #format and print planet data to table
                output = f"\033[4m|{name}" + (" " * name_spaces) + f"|{mass:.5e}   kg|{orbit_period}" + (" " * orbits_spaces) + " days" + "|\033[0m"
                print(output)

                #append planet info as tuple to planet list for return
                planet_list.append((name, mass, orbit_period))
    
    #exceptions
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
            
    return planet_list

def find_heaviest_planet(planets):
    #find the max based on mass and store tuple of name and mass to return
    heaviest = (max(planets, key = itemgetter(1))[0], max(planets, key = itemgetter(1))[1])

    return heaviest

planets = fetch_planet_data()
name, mass = find_heaviest_planet(planets)
print(f"The heaviest planet is {name} with a mass of {mass} kg.")