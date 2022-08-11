package generator

import (
	"Character-NFT/utils"
	"math/big"
	"strconv"
	"strings"
)

const (
	N = iota
	R
	SR
	SSR
)

func AttributesValueToUint256(rowValue map[string]string) *big.Int {
	var rowValueStr string
	var rowValueSlice []string
	for i := 0; i < 32; i++ {
		zeroValue := "0"
		num, _ := strconv.ParseInt(rowValue[strconv.Itoa(i)], 10, 32)
		value := utils.DecimalToAny(int(num), 2)
		if len(value) != 8 {
			for j := 0; j <= 8-len(value); j++ {
				value = zeroValue + value
			}
		}
		rowValueSlice = append(rowValueSlice, value)
	}
	var rowSlice []string
	rowValueStr1 := strings.Join(rowValueSlice[:10], "")
	rowSlice = append(rowSlice, rowValueStr1)
	rowValueStr2 := strings.Join(rowValueSlice[10:20], "")
	rowSlice = append(rowSlice, rowValueStr2)
	rowValueStr3 := strings.Join(rowValueSlice[20:30], "")
	rowSlice = append(rowSlice, rowValueStr3)
	rowValueStr4 := strings.Join(rowValueSlice[30:], "")
	rowSlice = append(rowSlice, rowValueStr4)

	rowValueStr = strings.Join(rowSlice, "")
	attributes, _ := new(big.Int).SetString(rowValueStr, 2)
	return attributes
}

func AppearanceValueToUint256(rowValue map[string]string) (appearance *big.Int) {

	return appearance
}
