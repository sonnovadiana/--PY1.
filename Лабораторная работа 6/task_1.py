def to_csv_file(filename, headers, rows, delimiter=',', new_line = '\n'):
    line = ''
    with open('{}'.format(filename), 'w') as f:
        for i in headers:
            line += i+'\t'
        f.writelines(line + new_line)
    with open('{}'.format(filename), 'a') as f:
        for l in rows:
            line_data = ''
            for i in l:
                line_data += i + '\t'
            f.writelines(line_data + new_line)

OUTPUT_FILE = 'out.csv'
headers_list = ['col1', 'col2', 'col3']
data = [['346346', '457346', '346663'],['34662415','23526','34635'],
        ['346375', '579457246', '468346'], ['234673', '48346', '96748346']]

to_csv_file(OUTPUT_FILE, headers_list, data)

with open(OUTPUT_FILE) as f:
    for i in f:
        print(i, end='')
