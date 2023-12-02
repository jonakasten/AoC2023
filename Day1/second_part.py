import re

def main():
    number_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    with open("input.txt", "r") as calibration_document:
        sum = 0
        for line in calibration_document:
            for i in range(len(number_words)):
                # the number word will be replaced with the actual number AND the actual number word, since some
                # number words are overlapping (e.g. 'eightwo')
                line = re.sub(fr"{number_words[i]}", str(f"{number_words[i]}{i+1}{number_words[i]}"), line)
            print(line)
            digits = [x for x in line if x.isdigit()]
            value = int(digits[0] + digits[-1])
            sum += value

        print(sum)


if __name__ == '__main__':
    main()
