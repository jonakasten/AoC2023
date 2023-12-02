
def main():
    with open("input.txt", "r") as calibration_document:
        sum = 0
        for line in calibration_document:
            digits = [x for x in line if x.isdigit()]
            value = int(digits[0] + digits[-1])
            sum += value
        print(sum)


if __name__ == '__main__':
    main()
