import code_base.validation_methods as val_meth

# test data passed in the test case:
lat_lon = [("51.5085", "-0.1257"), ("40.7128", "74.0060"), (41.8781, 87.6298)] # any data format is handled

# calling validation class/method:
val_meth.Validate_lat_lon(lat_lon).validate_lat_lon()
