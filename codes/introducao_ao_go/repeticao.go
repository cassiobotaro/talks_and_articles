package main

import (
	"fmt"
)

func main() {
	valor := 0

	// repetição C-like
	for i := 0; i < 10; i++ {
		valor++
		fmt.Printf("valor +1 = %v\r\n", valor)
	}
	// Parando iteração utilizando break
	for {
		valor--
		fmt.Printf("valor -1 = %v\r\n", valor)

		if valor == 0 {
			break
		}
	}

	potato := "Batata"
	for indice, letra := range potato {
		fmt.Printf("potato[%v] = %q\r\n", indice, letra)
	} // range
}
