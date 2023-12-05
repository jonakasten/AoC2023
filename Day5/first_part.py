import re

with open("input.txt", "r") as almanac:
    almanac_maps = []
    read_cnt = 0
    for line in almanac:
        line = line.strip()
        if line == "":
            read_cnt += 1
            continue

        if read_cnt == 0:
            almanac_maps.append([int(x) for x in re.findall(r"\d+", line)])
        else:
            matches = [int(x) for x in re.findall(r"\d+", line)]
            if len(almanac_maps) < (read_cnt + 1) and matches:
                almanac_maps.append([matches])
            elif matches:
                almanac_maps[read_cnt].append(matches)

    lowest_location = None

    # numbers are too big for brute forcing
    #for i in range(1, len(almanac_maps)):
    #    almanac_dict = {}
    #    for j in range(0, 100):
    #        almanac_dict[j] = j
    #    for entry in almanac_maps[i]:
    #        for k in range(entry[2]):
    #            almanac_dict[entry[1] + k] = entry[0] + k
    #    almanac_maps[i] = almanac_dict

    for seed in almanac_maps[0]:
        location = -1
        ref = seed
        for i in range(1, len(almanac_maps)):
            for entry in almanac_maps[i]:
                dest = entry[0]
                source = entry[1]
                ran = entry[2]
                if source <= ref <= (source + ran):
                    ref = dest + (ref - source)
                    break

            location = ref

            print(location)
        if not lowest_location:
            lowest_location = location
        elif location < lowest_location:
            lowest_location = location
    print(lowest_location)
