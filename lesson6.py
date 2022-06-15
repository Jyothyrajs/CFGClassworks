#import wikipedia
print(wikipedia.summary("PIP Python"))

### EXERCISE 1 ###
"""
This API is called 'Open Notify' http://open-notify.org/
It gives access to data about the Intrnational Space NASA station!
This API DOES NOT require authentication,

TASK: Make a call to the API endpoint to get live information about astronauts in space

"""



### EXERCISE 2 ###
"""
TASK: Make a call with a 'PAYLOAD' (special requirements) to the API endpoint
"""




### EXERCISE 3 ###
"""
TASK: Writing a log file to monitor the movement of ISS

Make a call to the API to get the current location for the International Space Station
See what data you get back
Convert the 'timestamp' from the response into readable date and time format
Write a log to the new file that captures time and ISS's location.
"""
# import requests
# from datetime import datetime
# from pprint import pprint as pp
#
# # this endpoint tells the current location for international space station
# endpoint3 = 'http://api.open-notify.org/iss-now.json'
#
# response = # YOUR CODE GOES HERE
#
# data = response.json()
# pp(data)
#
# timestamp = # YOUR CODE GOES HERE
# dt_object = # YOUR CODE GOES HERE TO CONVERT TIMESTAMP INTO READABLE FORMAT
#
# print("dt_object =", dt_object)
# print("type(dt_object) =", type(dt_object))
#
# msg = "At {dt} the ISS was passing the following location, latitude: {lat} and longitude: {lon}".format(
#     dt = dt_object,
#     lat = # add your code,
#     lon = # add your code
# )
#
# # Write a log record to a file
# # Run the program multiple times to get more records in the log




### EXERCISE 4 -- DEMO (as requires Authentication key ###
"""
This API is called 'Open Weather Map' http://api.openweathermap.org
It gives access to data about weather at different locations in the world and much more!
This API DOES require authentication! But it is FREE to register.
In order to get some data back, you need to use a unique 'Authentication Key'
It is VERY COMMON for many APIs to use authentication, especially in the professional world.
"""



### EXERCISE 5 ###
"""
This API is called 'Pokéapi' pokeapi.co/
It gives access to data about Pokémons
This API is free and does not require any authentication!

Each Pokemon has a number that identifies it

You can retrieve information about different Pokemon from urls

https://pokeapi.co/api/v2/pokemon/6/
"""



### EXERCISE 6 ###
"""
 Get the height and weight of a specific Pokemon and print the output

!!! Extension !!!: Print the names of all of a specific Pokemon's moves
"""
