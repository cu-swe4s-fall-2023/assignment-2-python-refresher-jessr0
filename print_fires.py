import my_utils

query_value='United States of America'
query_column = 1
result_column = 3
file_name = 'Agrofood_co2_emission.csv'
fires = my_utils.get_column(file_name, query_column, query_value, result_column)
print(fires)
