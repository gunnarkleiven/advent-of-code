def solve_part1(list_of_fish):
    print(f'Initial state = {list_of_fish}')

    for day in range(80):
        for i in range(len(list_of_fish)):
            list_of_fish[i] -= 1
            if list_of_fish[i] < 0:
                list_of_fish.append(8)
                list_of_fish[i] = 6
        # print(f'After {day} day(s): {list_of_fish}')
    res = len(list_of_fish)
    print(f'Result = {res}')


def solve_part2(list_of_fish):
    list_of_fish = [3, 4, 3, 1, 2]
    sum_fishes = len(list_of_fish)
    day_number = 18
    rebirth_age = 6
    saved_offspring_counts = {}
    for fish in list_of_fish:
        if fish in saved_offspring_counts.keys():
            print(f'Fish with age {fish} already checked out')
            sum_fishes += saved_offspring_counts[fish]
            continue
        tmp_count = 1
        # n_offsprings = (day_number - fish) // rebirth_age
        # sum_fishes += n_offsprings
        days_left = day_number
        while days_left - fish > 0:
            days_left -= fish
            fish = rebirth_age
            sum_fishes += 1
            offspring_number = add_offsprings(days_left - 1, rebirth_age, 8)
            # sum_fishes += add_offsprings(days_left - 1, rebirth_age, 8)
            sum_fishes += offspring_number
            tmp_count += 1
            tmp_count += offspring_number
        print(f'Initial fish tmp count = {tmp_count}')
        saved_offspring_counts[fish] = tmp_count
        print("-" * 30)
    print(f'Offsprings from the initial fishes: {sum_fishes}')


def add_offsprings(remaining_days, rebirth_age, fish_age):
    print(f'Offspring with {remaining_days} remaining days')
    tmp_count = 0
    while remaining_days - fish_age > 0:
        remaining_days -= fish_age
        fish_age = rebirth_age
        # sum_fishes += 1
        tmp_count += 1
        tmp_count += add_offsprings(remaining_days - 1, rebirth_age, 8)
    print(f'offspring tmp_count = {tmp_count}')
    return tmp_count


def solve_part2_v2(data):
    fish = data.copy()

    for _ in range(18):
        for idx, n_fish in enumerate(fish):
            if n_fish == 0:
                continue
            if idx == 0:
                continue
            fish[idx - 1] = n_fish
            fish[idx] = 0

        if fish[0] != 0:
            fish[7] += fish[0]
            fish[9] += fish[0]
            fish[0] = 0

    print(f'Res = {sum(fish)}')


def move_left(fish):
    tmp_first = fish[0]
    for i in range(1, len(fish)):
        fish[i - 1] = fish[i]
    # fish[-1] = tmp_first
    fish[-1] = tmp_first


def solve_part3_final(data):
    # By Øyvind Johannesen.
    fish = [0 for x in range(9)]
    for d in data:
        fish[d] += 1
    print(f'Fish= {fish}')

    for i in range(256):
        # print(f'Fish before move left: {fish}')
        move_left(fish)
        fish[6] += fish[8]
        # print(f'Fish after move left: {fish}')
    res = sum(fish)
    print(f'Final fish: {fish}\nFinal sum = {res}')


if __name__ == '__main__':
    with open('day6.txt', 'r') as reader:
        data = [int(x) for x in reader.readline().split(",")]
    # solve_part1(data)
    # solve_part1(data)
    # solve_part2(data)
    # solve_part2_v2(data)
    solve_part3_final(data)
