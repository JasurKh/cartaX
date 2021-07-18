from behave import given, when,then
import requests

@given(u'city names in the data folder')
def create_tuple_city_names(context):
    with open('data/city_names.txt') as f:
        city_names = tuple(f.read())
        print(city_names)
