import requests

# URL-1 for Open Weather:
url1 = "https://api.openweathermap.org/data/2.5/weather"

# # Secret Keys, created separately for each scenario/URL/user:
# name_API_key = "1dc944dfde3b0e2a5047bc2a8654b87e"
# lat_lon_API_key = "789a3bf1feab0c81d28561fda262eaf2"
# zip_API_key = "78a1db8aeb3720f2745c06ede9090f26"

# Test Data as expected value and validation variable:
city_name = ("London", "New York", "Toronto")
lat_lon = [("51.5085", "-0.1257"), ("40.7128", "74.0060"), (41.8781, 87.6298)]
zip_ctr_code = [("10002,US", "New York"), ("SW1A 1AA,GB", "London"), ("100-0001,JP", "Chiyoda")]

import validation_methods as val_meth
#step1 = val_meth.Validate_city_name(city_name).validate_city_name()

#step2 = val_meth.Validate_lat_lon(lat_lon).validate_lat_lon()

step3 = val_meth.Validate_zip(zip_ctr_code).validate_zip()


# Base requests:
# name_base_request = "https://api.openweathermap.org/data/2.5/weather?q=" + str(city_name1[i]) + "&appid=" + name_API_key
# lat_lon_base_request = "https://api.openweathermap.org/data/2.5/weather?lat=" + str(lat_lon1[i][0]) + "&lon=" + str(lat_lon1[i][1]) + "&appid=" + lat_lon_API_key
# zip_base_request = "https://api.openweathermap.org/data/2.5/weather?zip=" + zip_ctr_code1[i][0] + "&appid=" + zip_API_key


# temp test:

# class Construct_request_name_message():
#     from config_folder import config
#
#     global name_base_request
#     name_base_request = config.name_base_request
#
#     def __init__(self, city_name1, name_API_key):
#         self.city_name1 = city_name1
#         self.name_API_key = name_API_key
#
#     def request_message_name(self):
#         return str(name_base_request % (self.city_name1, self.name_API_key))
# import construct_request_message as construct_folder
# a = construct_folder.Construct_request_name_message("New York")
# print(a.request_message_name())


# import construct_request_message as construct_folder
# def validate_city_name(city_name1):
#     print("#" * 19 + "> CITY NAME <" + "#" * 19)
#     for i in range(len(city_name1)):  # iterating through test data set
#         print("Expected city name: " + city_name1[i])
#         request_name = construct_folder.Construct_request_name_message(city_name1[i]).request_message_name()  # constructing request message
#         response_json_name = requests.get(request_name)  # hitting the end point
#         name_validation = response_json_name.json()  # capturing the json response
#
#         # validating if actual is matching expected result:
#         if name_validation["name"] == city_name1[i]:
#             print("PASS, Actual city name: " + name_validation["name"])
#         if name_validation["name"] != city_name1[i]:
#             print("FAIL, City name doesn't match. Expected: " + city_name1[i] + " Actual: " + name_validation["name"])
#         # else: # can handle errors or load logs or email alerts and so on:
#         #     print("Check logs, path: /cartaX/app/dev/logs/...")
#         print("_" * 50)
#validate_city_name(city_name) #requires to pass the city name/s






# city by name test:
# for i in range(len(city_name1)): # iterating through test data set
#     print("Calling for city name: " + city_name1[i])
#     request_name = "https://api.openweathermap.org/data/2.5/weather?q=" + str(city_name1[i]) + "&appid=" + name_API_key # request message
#     response_json_name = requests.get(request_name) # hitting the end point
#     name_validation = response_json_name.json() # capturing the json response
#
#     #validating if actual is matching expected result:
#     if name_validation["name"] == city_name1[i]:
#         print("PASS, city name: " + name_validation["name"])
#     if name_validation["name"] != city_name1[i]:
#         print("FAIL, City name doesn't match. Expected: " + city_name1[i] + " Actual: " + name_validation["name"])
#     # else: # can handle errors or load logs or email alerts and so on:
#     #     print("Check logs, path: /cartaX/app/dev/logs/...")
#     print("_"*50)


# # # lat lon test:
# for i in range(len(lat_lon1)): # iterating through test data set
#     print("Calling lat/lon: " + str(lat_lon1[i]))
#     request_lat_lon = "https://api.openweathermap.org/data/2.5/weather?lat=" + str(lat_lon1[i][0]) + "&lon=" + str(lat_lon1[i][1]) + "&appid=" + lat_lon_API_key
#     response_json_lat_lon = requests.get(request_lat_lon) # hitting the end point
#     lat_lon_validation = response_json_lat_lon.json() # capturing the json response
#
#     # validating if actual is matching expected result:
#     if lat_lon_validation["coord"]['lat'] == float(lat_lon1[i][0]) and lat_lon_validation["coord"]['lon'] == float(lat_lon1[i][1]):
#         print("PASS " + str(lat_lon1[i]))
#     if lat_lon_validation["coord"]['lat'] != float(lat_lon1[i][0]) or lat_lon_validation["coord"]['lon'] != float(lat_lon1[i][1]):
#         print("FAIL, lat or lon are not matching for " + str(lat_lon1[i]) + ". Actual lat and lon: ('" + str(lat_lon_validation["coord"]['lat']) + "', '" + str(lat_lon_validation["coord"]['lon']) + "')")
#     # else: # can handle errors or load logs or email alerts and so on:
#     #     print("Check logs, path: /cartaX/app/dev/logs/...")
#     print("_"*50)
#
# #zip test, validate "name":
# for i in range(len(zip_ctr_code1)): # iterating through test data set
#     print("Calling zip/country: " + str(zip_ctr_code1[i]))
#     request_zip = "https://api.openweathermap.org/data/2.5/weather?zip=" + zip_ctr_code1[i][0] + "&appid=" + zip_API_key # request message
#     response_json_zip = requests.get(request_zip) # hitting the end point
#     zip_ctr_code_validation = response_json_zip.json() # capturing the json response
#
#     # validating if actual is matching expected result:
#     if zip_ctr_code_validation["name"] == zip_ctr_code1[i][1]:
#         print("PASS, zip as Expected: " + str(zip_ctr_code_validation["name"]))
#     if zip_ctr_code_validation["name"] != zip_ctr_code1[i][1]:
#         print("FAIL, zip Expected: " + str(zip_ctr_code1[i][1]) + ". Actual: " + str(zip_ctr_code_validation["name"]))
#     print("_" * 50)