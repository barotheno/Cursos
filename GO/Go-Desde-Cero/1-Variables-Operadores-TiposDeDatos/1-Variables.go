package main // Declaramos el paquete "main"

import "fmt"


func main() {
	var dog string //Declaración de variable
	dog = "Perrito"
	// Si no utilizamos una variable, saltará error
	// Asignacion de varias variables
	var cat, snake string = "Mariano", "Solid"
	// Tampoco hace falta especificar el tipo de dato

	fmt.Println(dog) // Imprimir en consola
	fmt.Println(cat, snake)
}