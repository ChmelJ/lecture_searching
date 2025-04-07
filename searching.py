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
    with open(file_path, "r") as file_obj:
        data = json.load(file_obj)
    if field in data.keys():
        return data[field]
    else:
        print(f'Field {field} not exist!')
        return None


def linear_search(list_of_numbers, number):
    list_of_idxs = []
    for idx, element in enumerate(list_of_numbers):
        if element == number:
            list_of_idxs.append(idx)
        else:
            pass
    dictionary_of_found_numbers = {"positions": list_of_idxs, "count": len(list_of_idxs)}
    return dictionary_of_found_numbers


def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)
    found_numbers_linear = linear_search(sequential_data, 0)
    print(found_numbers_linear)


if __name__ == '__main__':
    main()
