import json

stuff = []
record_data = []


def process_last_record(record_data):
    process_record(record_data)


def remove_empty_records(l):
    return list(filter(None, l))


def process_record(record_data):
    node = {'name': record_data[0].strip().split(',')[0], 'choices': []}
    for i in range(1, len(record_data)):
        choices_node = {'person': '',
                        'likes': []}
        split_record = remove_empty_records(record_data[i].strip().split(','))
        choices_node['person'] = split_record[0]
        del split_record[0]
        choices_node['likes'] = split_record
        node['choices'].append(choices_node)
    stuff.append(node)


def process_csv_data(csv_data):
    global record_data

    for line in csv_data:
        words = line.split(',')
        if len(words[0]) == 0:
            process_record(record_data)
            record_data = []
        else:
            record_data.append(line)
    process_last_record(record_data)
    out_data = json.dumps(stuff)
    print(out_data)

    return out_data


def main():
    import fileinput
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='CSV file to convert')
    process_csv_data(fileinput.input(parser.parse_args().filename))


if __name__ == '__main__':
    main()
