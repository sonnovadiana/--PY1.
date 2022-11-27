import json

INPUT_FILE = 'output.csv'

def csv_to_list_dict(file_name):
    dic = {}
    data = []

    with open(file_name, 'r') as f:
        columns = f.readline().split('\n')
        for i in f:
            data.append(i.splitlines())

    columns = columns[0].split(',')

    for num, col in enumerate(columns):
        data_col = []
        for d in data:
            d = d[0].split(',')
            data_col.append(d[num])
        dic.update({col:data_col})

    return dic

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))



