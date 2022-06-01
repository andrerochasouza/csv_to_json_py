def csv_to_json(csv_file, json_file):
    d = []
    h = []
    c = []
    n = 0

    with open(csv_file, 'r') as f:
        d = f.readlines()
        d = [x.strip() for x in d]
        n = len(d)
    f.close()
        
    with open(json_file, 'w') as f:
        f.write('{')
        for i in range(n):
            h.append(d[i].split(',')) if i == 0 else c.append(d[i].split(','))
        for i in range(len(h[0])):
            f.write('\n \t"' + h[0][i] + '": [')
            for j in range(len(c)):
                f.write('"' + c[j][i] + '"')
                f.write(',') if j < len(c)-1 else None
            f.write(']')
            f.write(',') if i < len(h[0])-1 else None
        f.write('\n}')
    f.close()


csv_to_json('csv_to_json_py/csv_file.csv', 'csv_to_json_py/json_file.json')