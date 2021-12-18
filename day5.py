# from https://stackoverflow.com/questions/328107/how-can-you-determine-a-point-is-between-two-other-points-on-a-line-segment
from math import sqrt

class Pos:
    def __init__(self, pos):
        self.x, self.y = [int(x) for x in pos.split(",")]

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


def distance(pos1, pos2):
    return sqrt((pos1.x - pos2.x) ** 2 + (pos1.y - pos2.y) ** 2)


def distance_to_origo(pos):
    return distance(pos, Pos(f'{0}, {0}'))


def is_between(pos1, pos2, check_pos):
    return distance(pos1, check_pos) + distance(check_pos, pos2) == distance(pos1, pos2)


def fill_grid(grid, start, end):
    print(f'Filling grid start:{start}, end:{end}')
    # Fill start and end pos. Put it in a for loop so we don't have to write the code twice
    for pos in [start, end]:
        add_point(grid, pos)

    # Now fill every point in between
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            curr_pos = Pos(f'{x},{y}')
            if curr_pos == start or curr_pos == end:
                continue
            if is_between(start, end, curr_pos):
                add_point(grid, curr_pos)


def add_point(grid, pos):
    # if not grid[pos.y][pos.x]:
    #     grid[pos.y][pos.x] = 1
    # else:
    #     grid[pos.y][pos.x] += 1
    grid[pos.y][pos.x] += 1


def fill_grid_v2(grid, pos1, pos2):
    # count = 0
    for pos in [pos1, pos2]:
        add_point(grid, pos)

    if distance_to_origo(pos1) < distance_to_origo(pos2):
        closest = pos1
        furthest = pos2
    else:
        closest = pos2
        furthest = pos1
    print(f'closest={closest}, furthest={furthest}')
    tmp_count = 0
    while True:
        # tmp_count += 1
        # if tmp_count > 10:
        #     return
        if closest.x < furthest.x:
            closest.x += 1
        if closest.y < furthest.y:
            closest.y += 1
        if closest == furthest:
            break
        # add_point(grid, closest)
        grid[closest.y][closest.x] += 1
        print(f'Current pos= {closest}')
        # if grid[closest.y][closest.x] == 2:
        #     count += 1


def fill_grid_v3(grid, pos1, pos2):
    global final_count
    for pos in [pos1, pos2]:
        add_point(grid, pos)

    increment_x = True if pos1.x < pos2.x else False
    increment_y = True if pos1.y < pos2.y else False

    while_counter = 0
    while True:

        if increment_x:
            if pos1.x < pos2.x:
                pos1.x += 1
        else:
            if pos1.x > pos2.x:
                pos1.x -= 1

        if increment_y:
            if pos1.y < pos2.y:
                pos1.y += 1
        else:
            if pos1.y > pos2.y:
                pos1.y -= 1

        if pos1 == pos2:
            break

        grid[pos1.y][pos1.x] += 1
        if grid[pos1.y][pos1.x] == 2:
            final_count += 1

        # print(f'Current pos1= {pos1}')


def solve_part1():
    global final_count

    with open('day5.txt', 'r') as reader:
        data = reader.readlines()
    grid_size = 10 if len(data) < 15 else 1000
    grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]

    # count = 0
    for x in data:
        pos1, _, pos2 = x.split()
        pos1 = Pos(pos1)
        pos2 = Pos(pos2)
        # print(f'pos1 = {pos1}, pos2 = {pos2}')

        # if pos1.x == pos2.x or pos1.y == pos2.y:
        #     fill_grid_v2(grid, pos1, pos2)
        fill_grid_v3(grid, pos1, pos2)

    # print(grid)
    count = 0
    # for y in grid:
    #     for x in y:
    #         print(f'{x} ', end="")
    #         if x > 1:
    #             print(x)
    #             count += 1
    #     print()
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] != 0:
                print(grid[y][x])
            if grid[y][x] > 1:
                count += 1
    print(f'Count = {count}')
    print(f'Final count = {final_count}')


if __name__ == '__main__':
    solve_part1()
