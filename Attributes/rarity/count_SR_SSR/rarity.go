package main

import (
	"NFT_Generator/read_excel"
	"fmt"
	"strconv"
	"time"
)

// RarityAtt 统计每组 SSR、SR 的数量
func RarityAtt(row map[string]string, valueN, valueR, valueMean, valueSR, valueSSR float32) (rowRarity map[string]int) {

	var countSSR, countSR, countMean, countR, countN int

	//for i, v := range row {
	//	if i != "" {
	//		value, _ := strconv.ParseFloat(v, 64)
	//		if float32(value) >= valueSSR {
	//			countSSR++
	//		} else if float32(value) >= valueSR && float32(value) < valueSSR {
	//			countSR++
	//		} else if float32(value) < valueN {
	//			countN++
	//		}
	//	}
	//}
	for i, v := range row {
		// 把每一行的第一个序号元素去掉
		if i != "" {
			// 因为从 Excel 中取出的数据是以 string 形式存在 map 中，所以首先转换格式
			value, _ := strconv.ParseInt(v, 10, 32)
			if float32(value) >= valueSSR {
				countSSR++
			} else if float32(value) >= valueSR && float32(value) < valueSSR {
				countSR++
			} else if float32(value) >= valueMean && float32(value) < valueSR {
				countMean++
			} else if float32(value) >= valueR && float32(value) < valueMean {
				countR++
			} else if float32(value) < valueN {
				countN++
			}
		}
	}

	rowRarity = make(map[string]int, 5)
	rowRarity["SSR"] = countSSR
	rowRarity["SR"] = countSR
	rowRarity["Mean"] = countMean
	rowRarity["R"] = countR
	rowRarity["N"] = countN

	return rowRarity
}

// RarityAttSSRCount 统计10000组中，每组 SSR 的数量情况(与SR分开统计)
func RarityAttSSRCount(rarity []map[string]int) (countSSR map[string]int) {
	var countSSR0, countSSR1, countSSR2, countSSR3, countSSR4, countSSR5, countSSR5M int

	countSSR = make(map[string]int, 10)
	for _, v := range rarity { // v：一组 attributes 的 SSR、SR 的数量
		switch v["SSR"] {
		//case 0:
		//	countSSR0++
		//	break
		//case 1:
		//	countSSR1++
		//	break
		//case 2:
		//	countSSR2++
		//	break
		//case 3:
		//	countSSR3++
		//	break
		//case 4:
		//	countSSR4++
		//	break
		//case 5:
		//	countSSR5++
		//	break
		//default:
		//	countSSR5M++
		//	break
		case 0:
			countSSR0++
			break
		case 1:
			if v["SR"] >= 8 {
				countSSR2++
				break
			} else {
				countSSR1++
				break
			}
		case 2:
			if v["SR"] >= 8 {
				countSSR3++
				break
			} else {
				countSSR2++
				break
			}
		case 3:
			if v["SR"] >= 8 {
				countSSR4++
				break
			} else {
				countSSR3++
				break
			}
		case 4:
			if v["SR"] >= 8 {
				countSSR5++
				break
			} else {
				countSSR4++
				break
			}
		case 5:
			if v["SR"] >= 8 {
				countSSR5M++
				break
			} else {
				countSSR5++
				break
			}
		default:
			countSSR5M++
			break
		}

	}
	countSSR["SSR=0"] = countSSR0
	countSSR["SSR=1"] = countSSR1
	countSSR["SSR=2"] = countSSR2
	countSSR["SSR=3"] = countSSR3
	countSSR["SSR=4"] = countSSR4
	countSSR["SSR=5"] = countSSR5
	countSSR["SSR>5"] = countSSR5M

	return countSSR
}

// RarityAttSRCount 统计10000组中，每组 SR 的数量情况(与SSR分开统计)
func RarityAttSRCount(rarity []map[string]int) (countSR map[string]int) {
	var countSR0, countSR5, countSR10, countSR15, countSR20, countSR20M int

	countSR = make(map[string]int, 10)
	for _, v := range rarity { // v：一组 attributes 的 SSR、SR 的数量
		if v["SR"] == 0 {
			countSR0++
		} else if v["SR"] > 0 && v["SR"] <= 5 {
			countSR5++
		} else if v["SR"] > 5 && v["SR"] <= 10 {
			countSR10++
		} else if v["SR"] > 10 && v["SR"] <= 15 {
			countSR15++
		} else if v["SR"] > 15 && v["SR"] <= 20 {
			countSR20++
		} else if v["SR"] > 20 && v["SR"] <= 32 {
			countSR20M++
		}
	}
	countSR["SR=0"] = countSR0
	countSR["0<SR<=5"] = countSR5
	countSR["5<SR<=10"] = countSR10
	//countSR["SR=11"] = countSR11
	//countSR["SR=12"] = countSR12
	//countSR["SR=13"] = countSR13
	countSR["10<SR<=15"] = countSR15
	countSR["15<SR<=20"] = countSR20
	countSR["20<SR<=32"] = countSR20M

	return countSR
}

func RarityStatistics(rarity []map[string]int) (countRarity map[string]int) {
	var rarityN, rarityR, raritySR, raritySSR int

	for _, v := range rarity {
		if v["N"] != 0 && v["SR"] == 0 && v["SSR"] == 0 && v["R"] <= 12 {
			rarityN++
		} else if v["N"] == 0 && v["SSR"] == 0 && v["SR"] == 6 && v["R"] >= 17 {
			rarityR++
		} else if v["N"] == 0 && v["SSR"] == 1 && v["SR"] == 8 && v["R"] == 14 {
			raritySR++
		} else if v["N"] == 0 && v["SSR"] >= 5 && v["SR"] >= 2 && v["R"] >= 12 && v["Mean"] >= 6 {
			raritySSR++
		}

	}

	countRarity = make(map[string]int, 5)

	countRarity["N"] = rarityN
	countRarity["R"] = rarityR
	countRarity["SR"] = raritySR
	countRarity["SSR"] = raritySSR

	return countRarity
}

func Rarity(fileName string, valueN, valueR, valueMean, valueSR, valueSSR float32) (countRarity map[string]int) {
	excel := read_excel.ReadExcel(fileName)
	var rowRarity map[string]int
	var rarity []map[string]int
	for _, row := range excel {
		rowRarity = RarityAtt(row, valueN, valueR, valueMean, valueSR, valueSSR)
		rarity = append(rarity, rowRarity)
	}
	countRarity = RarityStatistics(rarity)
	//fmt.Println(countRarity)
	return countRarity
}

func RarityResult(fileName []string, mu, sigma float32) (rowsRarity map[string]int) {

	valueN, valueR, valueMean, valueSR, valueSSR := RarityValue(mu, sigma)
	rowsRarity = make(map[string]int, 5)
	for i, file := range fileName {
		rowRarity := Rarity(file, valueN, valueR, valueMean, valueSR, valueSSR)
		fmt.Printf("%d:%v\n", i, rowRarity)
		rowsRarity["N"] += rowRarity["N"]
		rowsRarity["R"] += rowRarity["R"]
		rowsRarity["SR"] += rowRarity["SR"]
		rowsRarity["SSR"] += rowRarity["SSR"]
		//fmt.Println(rowsRarity)
	}
	fmt.Println(rowsRarity)
	return rowsRarity

}

func RarityValue(mu, sigma float32) (valueN, valueR, valueMean, valueSR, valueSSR float32) {
	valueN = mu - 2*sigma
	valueR = mu - sigma
	valueMean = mu
	valueSR = mu + sigma
	valueSSR = mu + 2*sigma
	return valueN, valueR, valueMean, valueSR, valueSSR

}

func main() {
	//countSSR := RarityAttSSRCount(Rarity)
	//fmt.Println(countSSR)
	//countSR := RarityAttSRCount(Rarity)
	//fmt.Println(countSR)

	startTime := time.Now().UnixNano()
	filePath := "D:\\PyCharm\\PycharmProjects\\pythonProject\\Attributes\\attributes_Generator\\axis-rarity-test-xlsx\\"
	var fileName []string
	for i := 0; i < 1000; i++ {
		fileNameStr := filePath + "axis_rarity_" + strconv.Itoa(i+1) + ".xlsx"
		fileName = append(fileName, fileNameStr)
	}
	RarityResult(fileName, 127.5, 42.5)

	endTime := time.Now().UnixNano()
	seconds := float64((endTime - startTime) / 1e9)
	//milliSeconds:= float64((endTime - startTime) / 1e6)
	//nanoSeconds:= float64(endTime - startTime)
	fmt.Println(seconds)

}
