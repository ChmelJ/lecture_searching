import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path) as data_file:
        data = json.load(data_file)
    if field in data.keys():
        return data[field]
    else:
        return None


def linear_search(sequence, searched_number):
    list_of_positions = []
    for position, number in enumerate(sequence):
        if number == searched_number:
            list_of_positions.append(position)
    return {'positions': list_of_positions, 'count': len(list_of_positions)}


def main():
    sequential_data = read_data('sequential.json', 'unordered_numbers')
    print(sequential_data)
    search_number_info = linear_search(sequential_data, 0)
    print(search_number_info)


if __name__ == '__main__':
    main()