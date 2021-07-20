package main

import "fmt"

func main() {
	// bool/booleanos | string | numeric

	var a bool = true 
	var b string = "string"
	var c int = 2021
	/**
		UINT = Solo almacena valores positivos

			# uint8 	=	(0 to 255)
			# uint16	=	(0 to 65535)
			# uint32	=	(0 to 4294967295)
			# uint64 	=	(0 to 18446744073709551615)

		INT = NEGATIVOS Y POSITIVOS

			# int8		=	(-128 to 127)
			# int16 	=	(-32768 to 32767)
			# int32		=	(-2147483648 to 2147483647)
			# int64		=	(-9223372036854775808 to 9223372036854775807)
			
	*/
	var d float64 = 134.9384
	var e float32 = 23.76

	// Para sumar dos numeros de tipos diferentes, debemos cambiar el tipo de la siguiente manera

	resultado := float64(c) + d

	// Imprimir en pantalla con formatos | %T = Tipo de datos | %v = Valor o variable
	fmt.Printf("Tipo: %T %T %T %T %T, Valor: %v %v %v %v %v",a,b,c,d,e,a,b,c,d,e)
	fmt.Printf("\nHemos cambiado el tipo de 'c' y lo hemos sumado con d, el resultado es: \n%v",resultado)
	// Si queremos tener una variable, pero no usarla aun, tenemos que utilizar el identificados blank

	_ = "Ruben"
	// ooo!!
	var _ string = "Pedroche Ranz"
}