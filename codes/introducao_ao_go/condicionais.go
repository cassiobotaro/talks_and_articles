package main

import "fmt"

func main() {

	// condicional simples
	if i := 42; i == 42 {
		fmt.Println("Ni!")
	} else if i == 2 {
		fmt.Println("Dois!")
	} else {
		fmt.Println("Else!")
	}
	// o i não existe fora do if

	// condição para mútiplas condicionais
	condicao := 3
	switch condicao {
	case 1:
		fmt.Println("Primeiro caso")
	case 2:
		fmt.Println("Segundo caso")
		fallthrough
	case 3, 4:
		fmt.Println("Terceiro caso")
	default:
		fmt.Println("caso inexistente.")
	}
	// fim da condicional múltipla
}
