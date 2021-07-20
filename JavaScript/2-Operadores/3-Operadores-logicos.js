/**
 * AND "&&"
 * or "||"
*/

let a = 10
let b = 1
let c = 30

// Saber si b es mayor que a y mayor que c

let resultado = (b > a) && (b > c)
if (resultado == true) {
    console.log("Ehectivamente es mayor")
} else {
    console.log("Pues va a ser que no")
}
console.log(resultado)

// Saber si b es menor que a o si b es menor que c

let resultado2 = (b > a) || (b > c)
if (resultado2 == true) {
    console.log("Ehectivamente es mayor")
} else {
    console.log("Pues va a ser que no")
}
console.log(resultado2)