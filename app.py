#Author : H. M. Tarek Ullah
#Backend (console app) of Location based food delivery service using 
# Google Map APIs and raw Python 2.7 


import requests,josn
import simplejson as json
import googlemaps
from datetime import datetime
from geolocation.main import GoogleMaps from geolocation.distance_matrix.client import DistanceMatrixApiClient


chosen_cruise = ""
past_selected= []
value = [] 
chosen_rest_lat = 0.0 
chosen_rest_lng = 0.0
user_lat = 0.0
user_long = 0.0 

API_KEY = "#################"  ##API key is hidden for security purpose

gmaps = googlemaps.Client(key='API_KEY')

##user locaion detection
def getuser_loc():  
    response = requests.post("https://www.googleapis.com/geolocation/v1/geolocate?key=API_KEY")
    res_json = josn.loads(response)
    user_lat = res_json.get("location").get("lat")
    user_long = res_json.get("location").get("lng")


chosen_cruise = raw_input("Enter Cuisine name")
past_selected.append(chosen_cruise)

##Nearby search using google map
def find_nearbyrest():
    near_restaurants = requests.post("https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=user_lat,user_long&radius=500&type=restaurant&keyword=chosen_cruise&key=API_KEY") 
    near_restaurants_json = json.loads(near_restaurants)
    for rest in near_restaurants_json:
        for key,value in rest.iter_items():
            if value=="name":
                nearby.append(value)

# showing nearby restaurants
def print_near_rest():
    for i in range(0,len(nearby)):
        print i 

#showing past selected restaurants
def print_past_selected_rest(): 
    for i in past_selected:
        print i

##Extract selected restaurant lat, lng 
def get_chosenrest_loc():
    for res in near_restaurants:
        for key,value in rest.iter_items():
            if nearby_restaurants_json.get("results").get("name")== chosen_cruise:
                chosen_rest_lat = near_restaurants_json.get("results").get("geometry").get("location").get("lat")
                chosen_rest_long = near_restaurants_json.get("results").get("geometry").get("location").get("lng") 




##Reverse geocoding restaurant location 
rest_reverse_geocode_result = gmaps.reverse_geocode((rest_lat, rest_long))
user_reverse_geocode_result = gmaps.reverse_geocode((user_lat, user_long))

##showing distance and duration of delivery 



def show_dist_delivery_time():
    origins = [user_reverse_geocode_result] 
    destinations = [rest_reverse_geocode_result]
    google_maps = GoogleMaps(api_key=’API_KEY’)
    items = google_maps.distance(origins, destinations).all() # default mode parameter is DistanceMatrixApiClient.MODE_DRIVING.
    
    for item in items:
        print item.distance.kilometers
        print item.distance.meters
        print item.duration

##Showing direction on Google Map from user to selected restaurants 

# Request direction via public transit
def show_direction_inmap():
    now = datetime.now()
    directions_result = gmaps.directions(origins,
                                     destinations,
                                     mode="transit",
                                     departure_time=now)


if __name__ == "__main__":
    
    ##call functions according to needs 
