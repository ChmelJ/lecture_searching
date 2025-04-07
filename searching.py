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


def pattern_search(sequence, pattern):
    set_of_idxs = set()
    pattern_length = len(pattern)
    for idx in range(0, len(sequence) - pattern_length):
        pattern_similarity = 0
        for idx_pattern, pattern_element in enumerate(pattern):
            if sequence[idx + idx_pattern] == pattern_element:
                pattern_similarity = pattern_similarity + 1
            else:
                pass
        if pattern_similarity == pattern_length:
            set_of_idxs.add(idx + pattern_length // 2 - 1)
        else:
            pass
    return set_of_idxs


def pattern_search_while(sequence, pattern):
   pos = set()
   index = 0
   while index < len(sequence) - len(pattern):
       if sequence[index:index + len(pattern)] == pattern:
           pos.add(index)
       index = index + 1
   return pos


def main():
    file_name = "sequential.json"
    key_of_sequence = "dna_sequence"
    searched_sequence = "ATA"
    sequential_data = read_data(file_name, key_of_sequence)
    print(sequential_data)
    found_set = pattern_search(sequential_data, searched_sequence)
    print(found_set)
    found_set = pattern_search_while(sequential_data, searched_sequence)
    print(found_set)


if __name__ == '__main__':
    main()
