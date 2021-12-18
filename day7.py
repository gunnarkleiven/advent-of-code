def solve(data):
    least_cost = float('inf')
    cheapest_idx = 0
    for i in range(len(data)):
        tmp_cost = 0
        for d in data:
            tmp_cost += abs(d - i)
        if tmp_cost < least_cost:
            least_cost = tmp_cost
            cheapest_idx = i
    print(f'Result = {cheapest_idx}, with a fuel consumption of {least_cost}')


def solve_part2(data):
    least_cost = float('inf')
    cheapest_idx = 0
    for i in range(len(data)):
        tmp_cost = 0
        for d in data:
            # tmp_cost += sum([x for x in range(i, d, 1 if i < d else -1)])
            tmp_cost += sum([x for x in range(1, abs(i-d) + 1)])
        if tmp_cost < least_cost:
            least_cost = tmp_cost
            cheapest_idx = i
    print(f'Result = {cheapest_idx}, with a fuel consumption of {least_cost}')


if __name__ == '__main__':
    with open('day7.txt', 'r') as reader:
        data = [int(x) for x in reader.readline().split(",")]
    solve(data)
    solve_part2(data)
