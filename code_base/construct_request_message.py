from config_folder import config

# class to construct the request message the CITY NAME api, requires 1 argument the city name:
class Construct_request_name_message():
    global name_base_request
    name_base_request = config.name_base_request
    name_API_key = config.name_API_key

    def __init__(self, city_name1):
        self.city_name1 = city_name1

    def request_message_name(self):
        return str(name_base_request % (self.city_name1, self.name_API_key))

# class to construct the request message the LAT LON api, requires 2 arguments the city latitude and longitude:
class Construct_request_lat_lon_message():
    global lat_lon_base_request
    lat_lon_base_request = config.lat_lon_base_request
    lat_lon_API_key = config.lat_lon_API_key

    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def request_message_lat_lon(self):
        return str(lat_lon_base_request % (self.lat, self.lon, self.lat_lon_API_key))

# class to construct the request message the ZIP api, requires 2 arguments the city "zip,coutry-code" as a single string with comma and Expected value for a city that zip indicates:
class Construct_request_zip_message():
    global zip_base_request
    zip_base_request = config.zip_base_request
    zip_API_key = config.zip_API_key

    def __init__(self, zip1):
        self.zip1 = zip1

    def request_message_zip(self):
        return str(zip_base_request % (self.zip1, self.zip_API_key))