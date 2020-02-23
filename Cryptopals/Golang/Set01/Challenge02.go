package main

import (
	"encoding/hex"
	"fmt"
)

func HexDecode(input string) []byte {
	hexStr, _ := hex.DecodeString(input)
	return hexStr
}

func HexEncode(input []byte) string {
	return hex.EncodeToString(input)
}

func main() {
	byte1 := HexDecode("1c0111001f010100061a024b53535009181c")
	byte2 := HexDecode("686974207468652062756c6c277320657965")
	finalByteArray := make([]byte, 18)
	for i := 0; i < 18; i++ {
		finalByteArray = append(finalByteArray, byte1[i]^byte2[i])
	}
	fmt.Println(HexEncode(finalByteArray))
}
