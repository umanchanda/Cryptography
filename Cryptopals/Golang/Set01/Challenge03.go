package main

import (
	"encoding/hex"
	"fmt"
	"strings"
)

// HexDecode decodes a hex input
func HexDecode(input string) []byte {
	hexStr, _ := hex.DecodeString(input)
	return hexStr
}

// HexEncode encodes a string input
func HexEncode(input []byte) string {
	return hex.EncodeToString(input)
}

func main() {
	var hexInputStr string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
	hexDecode := HexDecode(hexInputStr)

	for i := 0; i <= 256; i++ {
		repeatingCharacters := strings.Repeat(string(i), len(hexDecode))
		finalByteArray := make([]byte, 0)
		for j := 0; j < len(hexDecode); j++ {
			finalByteArray = append(finalByteArray, hexDecode[j]^repeatingCharacters[j])
		}
		fmt.Println(string(i), HexEncode(finalByteArray))
	}
}
