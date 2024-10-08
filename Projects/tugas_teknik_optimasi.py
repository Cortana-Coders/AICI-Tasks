# Traveling Salesman Problems


# pip googlemaps (in terminal)
import googlemaps


API = open("Google Maps Platform API Key.txt", 'r')
APIKEY = API.read()

Maps = googlemaps.Client(Key= APIKEY)

StartDestination = input("Dimana kamu akan memulai perjalanannya?\n")
EndDestination = input("Dimana kamu akan mengakhiri perjalannya?\n")

# Calculate distance thorugh API call
Distance = Maps.direction(StartDestination, EndDestination)

KDMistance = (Distance[0]['legs'][0]['distance'['text']])
HrsMinsDuration = (Distance[0]['legs'][0]['duration']['text'])

print("Kamu mengemudi jarak dari " + KDMistance + " total waktu " + HrsMinsDuration + " .")
