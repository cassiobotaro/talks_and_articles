package main

import "fmt"
import "log"

// Divisao divide o numero 1 pelo numero 2, caso 2 seja diferente de 0..
func Divisao(number1, number2 int) (int, error) {
	if number2 == 0 { // HL
		return 0, fmt.Errorf("divisão de inteiro por 0") // HL
	} // HL
	return number1 / number2, nil
}

func main() {
	res, err := Divisao(3, 0)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(res)
	fmt.Println("Good bye!")
}
