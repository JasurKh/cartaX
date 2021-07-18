import code_base.validation_methods as val_meth

# loading txt test data set from data folder:
with open('/Users/jasur/PycharmProjects/cartaX/data_folder/city_names') as f:
    city_names = eval(f.read())
    # print(city_names[1])
    f.close()


#calling validation class and passing all city names:
val_meth.Validate_city_name(city_names).validate_city_name()
