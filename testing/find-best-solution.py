VALID_DOUBLES = []
VALID_SINGLES = []

with open('../elements.csv') as stream:
    ELEMENTS = [x.strip('_\n') for x in stream.read().split(',')]


# There are 5 possible combinations of symbols to form a 4 char string:
# ABCD = { AbCd, AbCD, ABcD, ABCd, ABCD }
# 1. Generate 5 cases per test case.
# 2. Find number of invalid chars.
# 3. Select solution with least invalid chars.
def main():
    with open('test-cases.txt') as stream:
        cases = [x.strip() for x in stream.readlines()]
    output = []
    for case in cases:
        key, val = case.split(",")
        # index = number of misses
        ordered_solutions = [[], [], [], [], []]
        solutions = [
                # A       B        C        D
                [val[0], val[1], val[2], val[3]],
                # A       B        Cd
                [val[0], val[1], val[2:4]],
                # A       Bc         D
                [val[0], val[1:3], val[3]],
                # Ab        Cd
                [val[0:2], val[2:4]],
                # AbCd      C        D
                [val[0:2], val[2], val[3]]]

        discard = False
        for sol in solutions:
            score = 0
            # If length of item > 2 && is invalid, discard it.
            for item in sol:
                if item not in ELEMENTS:
                    if len(item) == 2:
                        discard = True
                    score += 1
            if not discard:
                ordered_solutions[score].append(sol)
            discard = False

        index, best_solution = parse_best_solution(ordered_solutions)
        output.append(f"{key};{val};{index};{best_solution}")

    with open('solutions.txt', 'w') as stream:
        stream.write('\n'.join(output))


# indices represent number of misses.
def parse_best_solution(solutions: list):
    for i, r in enumerate(solutions):
        # Find the lowest index that is populated.
        if len(r) > 0:
            rank = r
            index = i
            break

    # Find subset with shortest length.
    min_length = 5
    for solution in rank:
        if len(solution) < min_length:
            # 
            min_length = len(solution)
            best_solution = solution
    return index, best_solution


if __name__ == "__main__":
    main()
