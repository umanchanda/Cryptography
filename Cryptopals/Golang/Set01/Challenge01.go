package main

import (
	b64 "encoding/base64"
	"encoding/hex"
	"fmt"
)

// HexToBase64 converts a hex string to base64 string
func HexToBase64(input string) string {
	bytes, _ := hex.DecodeString(input)
	return b64.StdEncoding.EncodeToString(bytes)
}

func main() {
	var hexInput string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
	fmt.Println(HexToBase64(hexInput))
}
