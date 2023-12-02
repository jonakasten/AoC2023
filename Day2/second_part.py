
def main():
    with open("input.txt", "r") as games:
        game_id = 0
        id_sum = 0
        powers = 0
        for game in games:
            max_values = {
                "red": 0,
                "green": 0,
                "blue": 0
            }
            game_id += 1
            # remove the prefix "Game 'game_id': " from the string
            grabs = game[len(str(game_id)) + 7:]
            grab_results = grabs.split(";")
            for result in grab_results:
                cubes = result.split(",")
                for cube in cubes:
                    amount = int(cube.split()[0])
                    color = cube.split()[1]
                    if max_values[color] <= amount:
                        max_values[color] = amount
            power = 1
            for value in max_values.values():
                power *= value
            powers += power
        print(powers)





if __name__ == '__main__':
    main()
