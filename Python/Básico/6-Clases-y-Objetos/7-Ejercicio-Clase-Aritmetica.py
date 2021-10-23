class Aritmetica:
    """
    A si es como es escriben comentarios en clases de python.

    Clase Aritmetica para realizar las operaciones de sumar, restar, etc

    """
    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    # Definimos el método sumar

    def sumar(self):
        return self.operandoA + self.operandoB
    
    # Metodo restar

    def restar(self):
        return self.operandoA - self.operandoB

    # Metodo multiplicar

    def multiplicar(self):
        return self.operandoA * self.operandoB

    # Metodo dividir

    def dividir(self):
        return self.operandoA / self.operandoB

# Creamos objetos de nuestra clase aritmética

aritmetica1 = Aritmetica(5,3)
print(f'Suma: {aritmetica1.sumar()}')
print(f'Restar: {aritmetica1.restar()}')
print(f'Multiplicar: {aritmetica1.multiplicar()}')
print(f'Dividir: {aritmetica1.dividir():.2f}')# Con ":.2f" Indicamos cuando digitos flotantes o decimales queremos