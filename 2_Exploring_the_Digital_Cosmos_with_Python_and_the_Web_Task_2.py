import requests

def fetch_planet_data():
    try:
        #connect and grab response from The Solar System OpenData
        url = "https://api.le-systeme-solaire.net/rest/bodies/"
        response = requests.get(url)
        planets = response.json()['bodies']

        #process each planet info
        #iterate through bodies and print information from bodies that are planets
        for planet in planets:
            if planet['isPlanet']:
                name = planet['englishName']
                mass = planet['mass']['massValue']
                orbit_period = planet['sideralOrbit']
                print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

fetch_planet_data()