import argparse
from itertools import chain

import utils


@utils.timeit
def count_with_for(filename):
    count = 0
    with open(filename, 'r') as f:
        for _ in f:
            count += 1
    return count


@utils.timeit
def count_with_readlines(filename):
    count = 0
    with open(filename, 'r') as f:
        count = len(f.readlines())
    return count


@utils.timeit
def merge_lists_with_comprehension(data_list):
    return [item for sublist in data_list for item in sublist]


@utils.timeit
def merge_lists_with_chain(data_list):
    return list(chain.from_iterable(data_list))


def count_test(input_file):
    print(input_file.name)
    count_with_for(input_file)
    count_with_readlines(input_file)


def merge_list_test(data):
    merge_lists_with_comprehension(data)
    merge_lists_with_chain(data)


def main(params):
    input_files = params['input']
    if input_files is not None:
        for f in input_files:
            count_test(utils.get_path_obj(f))

    repeated_times = params['merge']
    if repeated_times > 0:
        merge_list_test([[1, 2, 3], [4, 5, 6], [7], [8, 9]] * repeated_times)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', dest='input', action='append',
                        type=str, help='input data file')
    parser.add_argument('-m', '--merge', dest='merge', type=int, default=0,
                        help='data repeated times for merge list test (default: 0)')

    args = parser.parse_args()
    main(vars(args))
