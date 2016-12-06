package main

import "fmt"
import "log"

// Unsafe division divide number1 by the number2.
func Unsafe_division(number1, number2 int) (int, error) {
	if number2 == 0 { // HL
		return 0, fmt.Errorf("integer division or modulo by zero") // HL
	} // HL
	return number1 / number2, nil
}

// Main handles an exception.
func main() {
	res, err := Unsafe_division(3, 0)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(res)
	fmt.Println("Good bye!")
}
