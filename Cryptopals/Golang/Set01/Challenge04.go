package main

import (
	"bufio"
	"fmt"
	"io"
	"net/http"
)

// LinesFromReader takes ioreader and returns array of strings
func LinesFromReader(r io.Reader) ([]string, error) {
	var lines []string
	scanner := bufio.NewScanner(r)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	if err := scanner.Err(); err != nil {
		return nil, err
	}

	return lines, nil
}

func main() {
	resp, err := http.Get("https://cryptopals.com/static/challenge-data/4.txt")
	if err != nil {
		panic(err)
	}
	defer resp.Body.Close()
	xorStrings, err := LinesFromReader(resp.Body)
	if err != nil {
		panic(err)
	}

	for i := 0; i < len(xorStrings); i++ {
		fmt.Println(xorStrings[i])
	}
}
