
def main():
    with open("input.txt", "r") as games:
        max_values = {
            "green": 13,
            "red": 12,
            "blue": 14
        }
        game_id = 0
        id_sum = 0
        for game in games:
            game_id += 1
            # remove the prefix "Game 'game_id': " from the string
            grabs = game[len(str(game_id)) + 7:]
            grab_results = grabs.split(";")
            is_possible = True
            for result in grab_results:
                cubes = result.split(",")
                for cube in cubes:
                    amount = int(cube.split()[0])
                    color = cube.split()[1]
                    is_possible &= (max_values[color] >= amount)
            if is_possible:
                id_sum += game_id
        print(id_sum)


if __name__ == '__main__':
    main()