import wikipedia
import pprint as pp
pp.pprint(wikipedia.summary("Python API"))

### EXERCISE 1 ###
"""
This API is called 'Open Notify' http://open-notify.org/
It gives access to data about the Intrnational Space NASA station!
This API DOES NOT require authentication,

TASK: Make a call to the API endpoint to get live information about astronauts in space

"""
import requests
import pprint as pp
url = 'http://api.open-notify.org/astros.json'
response = requests.get(url)
data = response.json()
# pp.pprint(data)

with open('astro.txt', 'w') as astro_files:
    for person in data['people']:
        astro_files.write(person['name'])
        astro_files.write("\n")

with open('astro2.txt', 'w') as astro_files:
    crafts_l = []
    for person in data['people']:
        crafts_l.append(person['craft'])
    crafts = set(crafts_l)
    for cr in crafts:
        astro_files.write("\n")
        astro_files.write(cr)
        astro_files.write("space ship astros \n")
        for person in data['people']:
            if cr == person['craft']:
                astro_files.write(person['name'])
                astro_files.write("\n")



### EXERCISE 2 ###
"""
TASK: Make a call with a 'PAYLOAD' (special requirements) to the API endpoint
http://api.open-notify.org/iss-pass.json

API URL
http://api.domain.com/[resource-location]?param1=value1&param2=value2
"""
import  requests
import pprint as pp
url = "http://api.open-notify.org/iss-pass.json"
payload = {
    "lat":9.70556,
    "lon":76.34959
}
response = requests.get(url,params=payload)
data = response.json()
pp.pprint(data)


### EXERCISE 3 ###
"""
TASK: Writing a log file to monitor the movement of ISS

Make a call to the API to get the current location for the International Space Station
See what data you get back
Convert the 'timestamp' from the response into readable date and time format
Write a log to the new file that captures time and ISS's location.
"""
import requests
import datetime as dt
from pprint import pprint as pp

# this endpoint tells the current location for international space station
endpoint3 = 'http://api.open-notify.org/iss-now.json'
response = requests.get(endpoint3)
data = response.json()
pp(data)

timestamp = data['timestamp']
dt_object = dt.datetime.fromtimestamp(timestamp) # YOUR CODE GOES HERE TO CONVERT TIMESTAMP INTO READABLE FORMAT

print("dt_object =", dt_object)
print("type(dt_object) =", type(dt_object))

msg = "At {dt} the ISS was passing the following location, latitude: {lat} and longitude: {lon}".format(
    dt = dt_object,
    lat = data['iss_position']['latitude'],
    lon = data['iss_position']['longitude']
)
print(msg)
#
# # Write a log record to a file
# # Run the program multiple times to get more records in the log

with open("locationlog.txt",'a+') as log_file:
    log_file.write(msg)
    log_file.write("\n")
print("Success")


### EXERCISE 4 -- DEMO (as requires Authentication key ###
"""
This API is called 'Open Weather Map' http://api.openweathermap.org
It gives access to data about weather at different locations in the world and much more!
This API DOES require authentication! But it is FREE to register.
In order to get some data back, you need to use a unique 'Authentication Key'
It is VERY COMMON for many APIs to use authentication, especially in the professional world.
"""
# import requests
# import datetime as dt
# import pprint as pp
# endpoint3 = 'http://api.open-notify.org/iss-now.json'
# response = requests.get(endpoint3)
#
# data = response.json()
# pp.pprint(data)
#
# a = dt.datetime.fromtimestamp(data['timestamp'])
# lat = data['iss_position']['latitude']
# lon = data['iss_position']['longitude']
#
# msg = f"At {dt} the ISS was passing the following location, latitude: {lat} and longitude: {lon}"
#
#
# with open('log.txt', 'w+') as log_file:
#     log_file.write(msg)
#
# with open('log.txt', 'r') as file:
#     print(file.read())

import requests

import pprint as pp

API_key = ""
city_name = 'London'
url = 'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}'
response = requests.get(url)
data = response.json()
pp.pprint(data)
### EXERCISE 5 ###
"""Œ
This API is called 'Pokéapi' pokeapi.co/
It gives access to data about Pokémons
This API is free and does not require any authentication!

Each Pokemon has a number that identifies it

You can retrieve information about different Pokemon from urls
WAP to get pokeman name/id from user and print its Name,height and weight
https://pokeapi.co/api/v2/pokemon/6/
"""
import requests
import pprint as pp
input_id = int(input("ID of pokemon you need the details: "))
url = f'https://pokeapi.co/api/v2/pokemon/{input_id}'
response = requests.get(url)
data = response.json()
pp.pprint(data['name'])
pp.pprint(data['height'])
pp.pprint(data['weight'])


### EXERCISE 6 ###
"""
 Get the height and weight of a specific Pokemon and print the output

!!! Extension !!!: Print the names of all of a specific Pokemon's moves
"""
import requests
import pprint as pp
input_id = int(input("ID of pokemon you like to get details: "))
url_move = f'https://pokeapi.co/api/v2/pokemon/{input_id}'
response = requests.get(url_move)
data = response.json()
moves = (data['moves'])

for i in range(len(moves)):
    pp.pprint(moves[i]['move']['name'])