import requests
import code_base.construct_request_message as construct_folder

# the city name validation step:
class Validate_city_name():
    def __init__(self, city_name1):
        self.city_name1 = city_name1

    def validate_city_name(self):
        print("#" * 19 + "> CITY NAME <" + "#" * 19)
        for i in range(len(self.city_name1)):  # iterating through test data set
            print("Expected city name: " + self.city_name1[i])
            request_name = construct_folder.Construct_request_name_message(self.city_name1[i]).request_message_name()  # constructing the request by calling the class-method
            response_json_name = requests.get(request_name)  # hitting the end point
            name_validation = response_json_name.json()  # capturing the json response

            # validating if actual is matching expected result:
            if name_validation["name"] == self.city_name1[i]:
                print("PASS, Actual city name: " + name_validation["name"])
            if name_validation["name"] != self.city_name1[i]:
                print("FAIL, City name doesn't match. Expected: " + self.city_name1[i] + " Actual: " + name_validation["name"])
            # else: # can handle errors or load logs or email alerts and so on:
            #     print("Check logs, path: /cartaX/app/dev/logs/...")
            print("_" * 50)

# latitude and longitude validation step:
class Validate_lat_lon():
    def __init__(self, lat_lon1):
        self.lat_lon1 = lat_lon1

    def validate_lat_lon(self):
        print("#" * 20 + "> LAT LON <" + "#" * 20)
        for i in range(len(self.lat_lon1)): # iterating through test data set
            print("Expected lat/lon: " + str(self.lat_lon1[i]))
            request_lat_lon = construct_folder.Construct_request_lat_lon_message(self.lat_lon1[i][0], self.lat_lon1[i][1]).request_message_lat_lon() # constructing the request by calling the class-method
            response_json_lat_lon = requests.get(request_lat_lon) # hitting the end point
            lat_lon_validation = response_json_lat_lon.json() # capturing the json response

            # validating if actual is matching expected result:
            if lat_lon_validation["coord"]['lat'] == float(self.lat_lon1[i][0]) and lat_lon_validation["coord"]['lon'] == float(self.lat_lon1[i][1]):
                print("PASS " + str(self.lat_lon1[i]))
            if lat_lon_validation["coord"]['lat'] != float(self.lat_lon1[i][0]) or lat_lon_validation["coord"]['lon'] != float(self.lat_lon1[i][1]):
                print("FAIL, lat or lon are not matching for " + str(self.lat_lon1[i]) + ". Actual lat and lon: ('" + str(lat_lon_validation["coord"]['lat']) + "', '" + str(lat_lon_validation["coord"]['lon']) + "')")
            # else: # can handle errors or load logs or email alerts and so on:
            #     print("Check logs, path: /cartaX/app/dev/logs/...")
            print("_"*50)

# zip code validation the "city name" step:
class Validate_zip():
    def __init__(self, zip_ctr_code1):
        self.zip_ctr_code1 = zip_ctr_code1

    def validate_zip(self):
        print("#" * 22 + "> ZIP <" + "#" * 22)
        for i in range(len(self.zip_ctr_code1)): # iterating through test data set
            print("Expected zip/country: " + str(self.zip_ctr_code1[i]))
            request_zip = construct_folder.Construct_request_zip_message(self.zip_ctr_code1[i][0]).request_message_zip() # constructing the request by calling the class-method
            response_json_zip = requests.get(request_zip) # hitting the end point
            zip_ctr_validation = response_json_zip.json() # capturing the json response

            # validating if actual is matching expected result:
            if zip_ctr_validation["name"] == self.zip_ctr_code1[i][1]:
                print("PASS, zip Actual: " + str(zip_ctr_validation["name"]))
            if zip_ctr_validation["name"] != self.zip_ctr_code1[i][1]:
                print("FAIL, zip Expected: " + str(self.zip_ctr_code1[i][1]) + ". Actual: " + str(zip_ctr_validation["name"]))
            print("_" * 50)