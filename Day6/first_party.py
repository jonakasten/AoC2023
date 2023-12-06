import re

with open("input.txt", "r") as input:
    races = []
    for line in input:
        races.append([int(x) for x in re.findall(r"\d+", line)])
    winning_cnt = 1
    for i in range(len(races[0])):
        time = races[0][i]
        distance = races[1][i]
        winning_results = [x for x in range(time + 1) if (-1 * x**2 + time * x) > distance]
        winning_cnt *= len(winning_results)
    print(winning_cnt)


