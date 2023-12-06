import re

with open("input.txt", "r") as input:
    races = []
    for line in input:
        races.append([x for x in re.findall(r"\d+", line)])
    time = int(''.join(races[0]))
    distance = int(''.join(races[1]))
    winning_results = [x for x in range(time + 1) if (-1 * x**2 + time * x) > distance]
    print(len(winning_results))


