class Info:
    def __init__(self, segments):
        self.segments = segments
        self.n = len(segments)

    def __str__(self):
        return f'{self.n}'

class LookupInfo:
    def __init__(self, indexes):
        self.indexes = indexes
        self.potentials = []
        self.locked_status = "unlocked"

    # def get_index

def part1(data):
    count = 0
    for line in data:
        for i in range(len(line) - 4, len(line)):
            digits = line[i]
            if len(digits) in [2, 3, 4, 7]:
                count += 1
    print(f'Count part1 = {count}')


def train(training, original_display):
    model = {}
    locked_in = []
    lookup_configuration = {
        0: LookupInfo([0, 1, 2, 4, 5, 6]),
        1: LookupInfo([2, 5]),
        2: LookupInfo([0, 2, 3, 4, 6]),
        3: LookupInfo([0, 2, 3, 5, 6]),
        4: LookupInfo([1, 2, 3, 5]),
        5: LookupInfo([0, 1, 3, 5, 6]),
        6: LookupInfo([0, 1, 3, 4, 5, 6]),
        7: LookupInfo([0, 2, 5]),
        8: LookupInfo([0, 1, 2, 3, 4, 5, 6]),
        9: LookupInfo([0, 1, 2, 3, 5, 6]),
    }
    segment_numbers = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    tmp = {
        2: [1],
        3: [7],
        4: [4],
        5: [2, 3, 5],
        6: [0, 6, 9],
        7: [8]
    }
    potentials_table = {
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: []
    }
    unique_segments = [2, 3, 4, 7]

    dict = {}
    for x in range(10):
        dict[x] = ""

    # First, check if any of the training data contain unique segment numbers
    for val in training:
        # if len(val) in unique_segments:
        potential = tmp[len(val)]
        print(f'Value is {val}, and has the potential to be: {potential}')
        potentials_table[len(val)].append(val)
        # for x in potential:
            # spots = lookup_configuration[x].
            # for




    for key, val in potentials_table.items():
        print(f'{key}, {val}')

    # for key, value in potentials_table.items():


    # for key, value in potentials_table.items():
    #     n_configurations_for_value = calculate_configs(model, locked_in, value)
    #     for x in range(n_configurations_for_value):

    # for key, val in potentials_table.items():
    #     for x in val:

    return model

def calculate_configs(model, locked_in, value):
    n_configs = len(value)
    for char in value:
        if char in locked_in:
            n_configs -= 1
    print(f'Val: {value} has {n_configs} configurations')
    return n_configs


# def train_all(training, original_display):


def solve(data):
    original_display = {
        0: Info("abcefg"),
        1: Info("cf"),
        2: Info("acdeg"),
        3: Info("acdfg"),
        4: Info("bcdf"),
        5: Info("abdfg"),
        6: Info("abdefg"),
        7: Info("acf"),
        8: Info("abcdefg"),
        9: Info("abcdfg"),
    }

    # for key, value in original_display.items():
    #     print(f'Number: {key} has {value}/7 segments')

    # part1(data)

    for line in data:
        training = line[:10]
        output_digits = line[11:]
        # print(f'traning = {training}, output_digits = {output_digits}')
        model = train(training, original_display)
        # model = train_all(training, original_display)

if __name__ == '__main__':
    with open('day8.txt', 'r') as reader:
        data = [x.split() for x in reader.readlines()]
    solve(data)
