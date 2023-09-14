def get_column(file_name, query_column, query_value, result_column=1):
    array_con = []
    with open(file_name, 'r') as f:
        for line in f:
            columns = line.strip().split(",")
            array_con.append(columns)
    new_array = []
    for i in array_con:
        for j in i:
            if j == query_value:
                new_array.append(i[result_column])
                print(new_array)

