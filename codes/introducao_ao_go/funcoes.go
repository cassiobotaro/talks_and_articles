package main

import (
	"fmt"
)

// Retorno simples
func soma(x int, y int) int {
	return x + y
}

// Retorno duplo
func troca(x string, y string) (string, string) {
	return y, x
}

// ...
//Retorno assinado
func divide(x, y int) (resultado, resto int) { // os dois retornos são inteiros nesse exemplo
	resto = x % y
	resultado = x / y
	return
}

// função que recebe uma função como parâmetro
func executaFuncao(f func(string) string, valor string) {
	aux := f(valor)
	fmt.Printf(aux)
}

func ValorByRef(valor *int) {
	*valor++
}

// ...
func main() {
	fmt.Printf("Funções!\n")

	fmt.Printf("Soma 1+1 = %v\n", soma(1, 1))

	b, a := troca("A", "B")
	fmt.Printf("troca A, B = %v, %v\n", b, a)

	resu, rest := divide(5, 2)
	fmt.Printf("A divisão de 5 por 2 é = %v\n", resu)
	fmt.Printf("O resto da divisão de 5 por 2 é = %v\n", rest)

	// função anonima que vamos passar para printFunc
	ola := func(v string) string {
		return "Olá " + v + "!\n"
	}

	executaFuncao(ola, "Cássio")

	valor := 4
	ValorByRef(&valor)
	fmt.Printf("Esperado 5, e encontrado %d", valor)

}
