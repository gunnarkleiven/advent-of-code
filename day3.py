def solve_part1(data):
    gamma = ""
    epsilon = ""
    print(f'range={len(data[0])}')
    for i in range(len(data[0]) - 1):

        zeros = 0
        ones = 0
        for number in data:
            if number[i] == "0":
                zeros += 1
            else:
                ones += 1
        gamma += "0" if zeros > ones else "1"
        epsilon += "0" if zeros < ones else "1"

    print(f'gamma: {gamma}\nepsilon: {epsilon}')
    converted_gamma = int(gamma, 2)
    converted_epsilon = int(epsilon, 2)
    res = converted_gamma * converted_epsilon
    print(f'Result part1 = {res}')


def solve_part2(data):
    # print(f'Initial data: {data}')
    # find oxygen generator rating
    current_data = data.copy()
    for i in range(len(data[0])):
        zeroes = 0
        ones = 0
        zero_start = []
        one_start = []
        for x in current_data:
            first_bit = x[i]
            if first_bit == "0":
                zeroes += 1
                zero_start.append(x)
            else:
                ones += 1
                one_start.append(x)
        current_data = zero_start if zeroes > ones else one_start
        # print(f'Current data: {current_data}')
        if len(current_data) == 1:
            break

    oxygen_generator_rating = current_data[0]
    oxygen_generator_rating_converted = int(oxygen_generator_rating, 2)
    print(f'ox gen rating: {oxygen_generator_rating}, converted = {oxygen_generator_rating_converted}')

    current_data = data.copy()
    for i in range(len(data[0])):
        zeroes = 0
        ones = 0
        zero_start = []
        one_start = []
        for x in current_data:
            first_bit = x[i]
            if first_bit == "0":
                zeroes += 1
                zero_start.append(x)
            else:
                ones += 1
                one_start.append(x)
        current_data = one_start if ones < zeroes else zero_start
        # print(f'Current data: {current_data}')
        if len(current_data) == 1:
            break

    c02_scrubber_rating = current_data[0]
    c02_scrubber_rating_converted = int(c02_scrubber_rating, 2)
    print(f'scubber_rating={c02_scrubber_rating}, converted = {c02_scrubber_rating_converted}')


    res = oxygen_generator_rating_converted * c02_scrubber_rating_converted
    print(f'Res = {res}')


if __name__ == '__main__':
    with open('day3.txt', 'r') as reader:
        data = [x.strip() for x in reader.readlines()]
    # solve_part1(data)
    solve_part2(data)
