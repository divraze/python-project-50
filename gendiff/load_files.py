import json


def read_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def generate_diff(file1, file2):
    data1 = read_file(file1)
    data2 = read_file(file2)

    keys = sorted(set(data1) | set(data2))

    diff = ['{']

    for key in keys:
        if key in data1 and key in data2:
            diff.append(f' {key}: {data1[key]}')
        elif key in data1 and key not in data2:
            diff.append(f'- {key}: {data1[key]}')
        elif key not in data1 and key in data2:
            diff.append(f'+ {key}: {data2[key]}')
        elif data1[key] != data2[key]:
            diff.append(f'- {key}: {data1[key]}')
            diff.append(f'+ {key}: {data2[key]}')
    diff.append('}')
    return '\n'.join(diff)
