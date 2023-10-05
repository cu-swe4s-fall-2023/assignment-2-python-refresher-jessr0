import csv


def data_subset(full_data, test_data, num_rows):
    with open(full_data, 'r', newline='') as source:
        reader = csv.reader(source)
        with open(test_data, 'w', newline='') as target:
            writer = csv.writer(target)

            for i, row in enumerate(reader):
                if i == num_rows:
                    break
                writer.writerow(row)

    return test_data


data_subset("Agrofood_co2_emission.csv", "Agro_short.csv", 5)
