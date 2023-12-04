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

	gearPairings := map[Coordinates][]int{}
	sum := 0
	currentNumber := 0
	isPartNumber := false
	for row, line := range lineSlice {
		if isPartNumber {
			fmt.Println(currentNumber)
			sum += currentNumber
		}
		isPartNumber = false
		isGear := false
		gearCoordinates := Coordinates{}
		currentNumber = 0
		for col, c := range line {
			//surroundings := make([]rune, 0)
			surroundings := map[rune]Coordinates{}

			if unicode.IsDigit(c) {
				if row > 0 && col > 0 {
					topLeft := rune(lineSlice[row-1][col-1])
					surroundings[topLeft] = Coordinates{
						x: row - 1,
						y: col - 1,
					}
				}

				if row > 0 {
					top := rune(lineSlice[row-1][col])
					surroundings[top] = Coordinates{
						x: row - 1,
						y: col,
					}
				}

				if col > 0 {
					left := rune(lineSlice[row][col-1])
					surroundings[left] = Coordinates{
						x: row,
						y: col - 1,
					}
				}

				if col < len(line)-1 && row > 0 {
					topRight := rune(lineSlice[row-1][col+1])
					surroundings[topRight] = Coordinates{
						x: row - 1,
						y: col + 1,
					}
				}

				if col < len(line)-1 {
					right := rune(lineSlice[row][col+1])
					surroundings[right] = Coordinates{
						x: row,
						y: col + 1,
					}
				}

				if row < len(lineSlice)-1 {
					bottom := rune(lineSlice[row+1][col])
					surroundings[bottom] = Coordinates{
						x: row + 1,
						y: col,
					}
				}

				if row < len(lineSlice)-1 && col > 0 {
					bottomLeft := rune(lineSlice[row+1][col-1])
					surroundings[bottomLeft] = Coordinates{
						x: row + 1,
						y: col - 1,
					}
				}

				if row < len(lineSlice)-1 && col < len(line)-1 {
					bottomRight := rune(lineSlice[row+1][col+1])
					surroundings[bottomRight] = Coordinates{
						x: row + 1,
						y: col + 1,
					}
				}

				currentNumber *= 10
				currentNumber += int(c - '0')

				for char, co := range surroundings {
					if IsSymbol(char) {
						isPartNumber = true
					}
					if char == '*' {
						isGear = true
						gearCoordinates = co
					}
				}
			} else {
				if isPartNumber {
					sum += currentNumber
				}
				if isGear {
					if _, ok := gearPairings[gearCoordinates]; !ok {
						gearPairings[gearCoordinates] = []int{}
					}
					gearPairings[gearCoordinates] = append(gearPairings[gearCoordinates], currentNumber)
				}
				currentNumber = 0
				isPartNumber = false
				isGear = false
				gearCoordinates = Coordinates{}
			}

		}
	}
	ratioSum := 0
	for _, ratioList := range gearPairings {
		if len(ratioList) > 1 {
			ratioProd := 1
			for _, ratio := range ratioList {
				ratioProd *= ratio
			}
			ratioSum += ratioProd
		}
	}

	fmt.Println(ratioSum)
	fmt.Println(sum)

	defer file.Close()
}

func IsSymbol(c rune) bool {
	return !unicode.IsDigit(c) && c != '.'
}

type Coordinates struct {
	x int
	y int
}
