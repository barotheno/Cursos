package main

import "fmt"

func main() {

	// Operadores Aritméticos (), *, /, %, +, -
	var a = 4
	var b = 8
	fmt.Println(a * b)

	// Operadores de asignación: =, +=, -=, *=, /=, %=
	var c = 20
	c += 10
	fmt.Println(c)

	// Declaracion post-incremento y post-decremento: ++, --
	// (no son una expresion sino una declaracion)
	var d = 3
	d++
	fmt.Println(d)
}