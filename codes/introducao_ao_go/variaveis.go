package main

import "fmt"

var (
	nome  = "Cássio"
	idade = 19
)

const Pi = 3.14

func main() {
	fmt.Println("Antes da mudança: ", nome)
	nome = "Cássio Botaro"
	fmt.Println("Depois da mudança: ", nome)
	//Pi = 3.1

	// ...
	var variavel string
	variavel = "https://httpbin.org"

	inferenciaTipo := 3 + 4i

	funçãoOlá := func() {
		fmt.Printf("Olá da função anônima!\r\n")
	}

	fmt.Printf("%v tipo %T\n", variavel, variavel)
	fmt.Printf("%v tipo %T\n", inferenciaTipo, inferenciaTipo)
	fmt.Printf("%T\n", funçãoOlá)
	funçãoOlá()
}
