def to_csv_file(filename, headers, rows, delimiter=',', new_line = '\n'):
    with open('{}.csv'.format(filename), 'w') as f:
        f.write(str(headers) + new_line)
    with open('{}.csv'.format(filename), 'a') as f:
        for i in rows:
            f.write(str(i) + new_line)

print(to_csv_file('lol', ['col1', 'col2'], [('123','data1'), ('456', 'data2')]))
