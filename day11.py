from collections import defaultdict


class Solution:
    def __init__(self):
        self.count = 0
        self.count_part2 = 0

    def solve(self, data):
        graph = defaultdict(list)
        for connection in data:
            a, b = connection.split("-")
            graph[a].append(b)
            graph[b].append(a)

        # visited_numbers = [0 for _ in range(len(graph.keys()))]
        visited_numbers = defaultdict(int)
        visited_twice = defaultdict(bool)
        for k in graph.keys():
            visited_numbers[k] = 0
            visited_twice[k] = False

        # visited = [False for _ in range(len(graph.keys()))]
        visited = defaultdict(bool)
        for k in graph.keys():
            visited[k] = False

        # print(f"visisted: {visited}")
        #
        # for key, val in graph.items():
        #     print(f'key={key}, val={val}')

        all_paths = []
        # dfs(graph, visited, "start", all_paths, [])

        # for p in all_paths:
        #     print(f"Path: {p}")

        # visited_numbers["start"] += 1
        # paths = []
        # current_path = []
        # search_all_paths("start", "end", graph, visited_numbers, path

        all_paths = []
        # self.every_path_part1("start", graph, visited, all_paths, [])
        # print(f"Count part1 = {self.count}")

        self.every_path_part2("start", graph, visited, visited_twice, all_paths, [])
        print(f"Count part2 = {self.count}")

    def every_path_part1(self, a, graph, visited_numbers, all_paths, path):
        visited_numbers[a] += 1
        path.append(a)

        if a == "end":
            # print(path)
            self.count += 1
        else:
            for nbr in graph[a]:
                if nbr.isupper() or visited_numbers[nbr] < 1:
                    self.every_path_part1(nbr, graph, visited_numbers, all_paths, path)

        path.pop()
        visited_numbers[a] -= 1

    def every_path_part2(self, a, graph, visited_numbers, visited_twice, all_paths, path):
        visited_numbers[a] += 1
        if visited_numbers[a] == 2:
            visited_twice[a] = True
        path.append(a)

        has_been_visited_twice = any(visited_twice.values())

        if a == "end":
            print(path)
            self.count += 1
            return
        else:
            for nbr in graph[a]:
                if nbr != "start" and nbr.isupper() or visited_numbers[nbr] < (1 if has_been_visited_twice else 2):
                    self.every_path_part2(nbr, graph, visited_numbers, visited_twice, all_paths, path)

        path.pop()
        visited_numbers[a] -= 1


# def search_all_paths(vertex, end, grid, visited_numbers, paths, curr_path):
#     visited_numbers[vertex] += 1
#     for nbr in grid[vertex]:
#         if nbr == end:
#             curr_path.append(nbr)
#             return
#         if nbr.isupper() or visited_numbers[vertex] < 1:
#             search_all_paths(nbr, end, grid, visited_numbers, paths, curr_path)
#         curr_path.append(nbr)


# def dfs(grid, visited, vertex, all_paths, path):
#     visited[vertex] = True
#     for x in grid[vertex]:
#         if not visited[x]:
#             dfs(grid, visited, x, all_paths, path)
#         path.append(x)
#     all_paths.append(path)

if __name__ == '__main__':
    with open('day11.txt', 'r') as reader:
        data = [x.strip() for x in reader.readlines()]

    solution = Solution()
    solution.solve(data)
