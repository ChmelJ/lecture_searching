from pathlib import Path
import json
import time
import matplotlib.pyplot as plt
from generators import unordered_sequence, ordered_sequence


def read_data(file_name, field):
    """
    Reads a JSON file and returns data for a given field.

    Args:
        file_name (str): Name of the JSON file.
        field (str): Key to retrieve from the JSON data.
            Must be one of: 'unordered_numbers', 'ordered_numbers' or 'dna_sequence'.

    Returns:
        list | str | None:
            - list: If data retrieved by the selected field contains numeric data.
            - str: If field is 'dna_sequence'.
            - None: If the field is not supported.
    """
    # get current working directory path
    cwd_path = Path.cwd()

    file_path = cwd_path / file_name
    with open(file_path, mode='r') as file:
        data = json.load(file)
    if field in data.keys():
        return data[field]
    else:
        return None


def linear_search(searched_data, searched_number):
    idx = 0
    count = 0
    positions = []
    searched_dictionary = {}
    while idx < len(searched_data):
        if searched_data[idx] == searched_number:
            count += 1
            positions.append(idx)
        idx += 1
    searched_dictionary['positions'] = positions
    searched_dictionary['count'] = count
    return searched_dictionary

def binary_search(searched_data, searched_number):
    left = 0
    right = len(searched_data) - 1
    while left <= right:
        middle = (left + right) // 2
        if searched_data[middle] == searched_number:
            return middle
        elif searched_data[middle] < searched_number:
            left = middle + 1
        elif searched_data[middle] > searched_number:
            right = middle - 1
    return None


def test_complexity(list_of_n):
    number = 42
    times_linear = []
    times_binary = []
    for n in list_of_n:
        unordered_data = unordered_sequence(n)
        ordered_data = ordered_sequence(n)
        duration_linear = 0
        duration_binary = 0
        repetitions = 100
        for meaurements in range(repetitions):
            start_time_linear = time.perf_counter()
            found_number = linear_search(unordered_data, number)
            end_time_linear = time.perf_counter()
            duration_linear += end_time_linear - start_time_linear

            start_time_binary = time.perf_counter()
            found_number_bin = binary_search(ordered_data, number)
            end_time_binary = time.perf_counter()
            duration_binary += end_time_binary - start_time_binary
        times_linear.append(duration_linear / repetitions)
        times_binary.append(duration_binary / repetitions)
    print(times_linear)
    print(times_binary)
    plt.plot(list_of_n, times_linear)
    plt.plot(list_of_n, times_binary)

    plt.xlabel("Velikost vstupu")
    plt.ylabel("Čas [s]")
    plt.title("Porovnaní vyhledavacích algoritmů")
    plt.show()


def pattern_search(sequency, pattern):
    indices = {}
    
    return indices

def main():
    my_data = read_data('sequential.json', 'ordered_numbers')
    number = 21
    print(my_data)
    duration = 0
    repetitions = 100
    for meaurements in range(repetitions):
        start_time = time.perf_counter()
        found_number = linear_search(my_data, number)
        end_time = time.perf_counter()
        duration += end_time - start_time
    print(found_number)
    print(duration / repetitions)
    found_number_bin = binary_search(my_data, number)
    print(found_number_bin)
    sizes = [10, 20, 50, 100]
    test_complexity(sizes)

if __name__ == "__main__":
    main()