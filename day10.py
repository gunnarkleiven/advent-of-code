def solve(data):
    opens = ["(", "[", "{", "<"]
    closes = [")", "]", "}", ">"]

    # close_open_pairs = {")": "(", "]": "[", "}": "{", ">": "<"}
    close_open_pairs = {"(": ")", "[": "]", "{": "}", "<": ">"}

    corrupted_points = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137
    }
    points = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4
    }

    corrupted_lines_explanation = []
    corrupted_lines = []
    illegal_chars = []

    # not_corrupted_lines = {}
    not_corrupted_lines = []
    for line in data:
        # print(line)
        opens_stack = []
        closes_stack = []
        illegal_line = False
        for i in range(len(line)):
            char = line[i]
            if char in opens:
                opens_stack.append(char)
            else:
                closes_stack.append(char)
                found = char
                # found = opens_stack.pop(-1)
                expected = close_open_pairs[opens_stack.pop(-1)]
                if expected != found:
                    corrupted_lines_explanation.append(f"{line} expected {expected}, but found {found} instead")
                    corrupted_lines.append(line)
                    illegal_chars.append(found)
                    illegal_line = True
                    break
        if illegal_line:
            continue

        ostack = opens_stack.copy()
        cstack = closes_stack.copy()
        while opens_stack and closes_stack:
            open_val = opens_stack.pop(-1)
            close_val = closes_stack.pop(-1)
            if close_open_pairs[open_val] != close_val:
                # print(f"{open_val} and {close_val} does not pair")
                break

        if opens_stack or closes_stack:
            not_corrupted_lines.append(ostack)
            # print(f"Incomplete line: {line}")
            # print(f"ostack: {ostack}, cstack: {cstack}")

    # for line in corrupted_lines_explanation:
    #     print(line)
    # score = 0
    # for char in illegal_chars:
    #     score += corrupted_points[char]
    # print(f'Part1 = {score}')

    part2_scores = []
    # for key, val in not_corrupted_lines:
    for stack in not_corrupted_lines:
        add_order = []
        while stack:
            val = stack.pop(-1)
            add_order.append(close_open_pairs[val])
        # print(f'Complete by adding {"".join(add_order)}')
        score = 0
        for x in add_order:
            score *= 5
            score += points[x]
        part2_scores.append(score)
    part2_scores.sort()
    # print(f'Part2 scores = {part2_scores}')
    res = part2_scores[len(part2_scores) // 2]
    print(f"Res part2 = {res}")



if __name__ == '__main__':
    with open('day10.txt', 'r') as reader:
        data = [x.strip() for x in reader.readlines()]
    solve(data)
