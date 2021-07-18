import code_base.validation_methods as val_meth
import csv

# another approach of the test data input:
rows = []
with open('/Users/jasur/PycharmProjects/cartaX/data_folder/zip_input2.csv', 'r') as csv_input_file:
    csv_input_file = csv.reader(csv_input_file)

    for row in csv_input_file:
        rows.append(tuple(row))
    # print(rows)

# calling validation class/method:
val_meth.Validate_zip(rows).validate_zip()