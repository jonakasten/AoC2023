package main

import (
	"bufio"
	"fmt"
	"os"
	"unicode"
)

func main() {
	file, err := os.Open("input.txt")

	if err != nil {
		fmt.Println("Error opening input")
		return
	}

	scanner := bufio.NewScanner(file)

	lineSlice := make([]string, 0)
	for scanner.Scan() {
		line := scanner.Text()
		lineSlice = append(lineSlice, line)
	}

	sum := 0
	currentNumber := 0
	isPartNumber := false
	for row, line := range lineSlice {
		if isPartNumber {
			fmt.Println(currentNumber)
			sum += currentNumber
		}
		isPartNumber = false
		currentNumber = 0
		for col, c := range line {
			surroundings := make([]rune, 0)

			if unicode.IsDigit(c) {
				if row > 0 && col > 0 {
					topLeft := rune(lineSlice[row-1][col-1])
					surroundings = append(surroundings, topLeft)
				}

				if row > 0 {
					top := rune(lineSlice[row-1][col])
					surroundings = append(surroundings, top)
				}

				if col > 0 {
					left := rune(lineSlice[row][col-1])
					surroundings = append(surroundings, left)
				}

				if col < len(line)-1 && row > 0 {
					topRight := rune(lineSlice[row-1][col+1])
					surroundings = append(surroundings, topRight)
				}

				if col < len(line)-1 {
					right := rune(lineSlice[row][col+1])
					surroundings = append(surroundings, right)
				}

				if row < len(lineSlice)-1 {
					bottom := rune(lineSlice[row+1][col])
					surroundings = append(surroundings, bottom)
				}

				if row < len(lineSlice)-1 && col > 0 {
					bottomLeft := rune(lineSlice[row+1][col-1])
					surroundings = append(surroundings, bottomLeft)
				}

				if row < len(lineSlice)-1 && col < len(line)-1 {
					bottomRight := rune(lineSlice[row+1][col+1])
					surroundings = append(surroundings, bottomRight)
				}

				currentNumber *= 10
				currentNumber += int(c - '0')

				for _, char := range surroundings {
					if IsSymbol(char) {
						isPartNumber = true
						break
					}
				}
			} else {
				if isPartNumber {
					fmt.Println(currentNumber)
					sum += currentNumber
				}
				currentNumber = 0
				isPartNumber = false
			}

		}
	}
	fmt.Println(sum)

	defer file.Close()
}

func IsSymbol(c rune) bool {
	return !unicode.IsDigit(c) && c != '.'
}
