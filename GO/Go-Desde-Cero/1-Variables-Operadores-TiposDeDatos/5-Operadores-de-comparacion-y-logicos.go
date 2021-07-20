package main

import "fmt"

func main(){
	// Operadores de Comparación: >, <, ==, !=, >=, <=
	var a = 89
	var b = 50
	fmt.Println(a == b)
	fmt.Println(a != b)

	// Operadores lógicos &&, ||
	fmt.Println(a > b && b != a)
	fmt.Println(a > b || a < b)

	// Operador unario
	fmt.Println(!(4 == 4))
}