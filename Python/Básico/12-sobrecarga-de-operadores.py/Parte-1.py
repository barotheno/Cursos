# La sobrecarga de un operador significa que un mismo operador puede comportarse de diferentes formas
# Ejemplo:
#   El operador de suma +
#       Este operador se puede comportar de maneras diferentes dependiendo si está trabajando con tipos string o númericos.

# En este caso ponemos como ejemplo un operador de suma númerico

a = 2
b = 3
print(a+b)

# Ejemplo tipo string

a = 'Hola'
b = 'Mundo'
print(a + b)

# Ejemplo con listas

a = [1,2,3]
b = [6,7,8]
print(a+b)

# Tambien se puede hacer esto con clases, agregando la sobrecarga de un método dependiendo del operador
# LISTA DE MÉTODOS SEGÚN EL OPERADOR QUE QUERAMOS SOBRECARGAR.
"""
    + ====== __add__(self, other)
    - ====== __sub__(self, other)
    * ====== __mul__(self, other)
    / ====== __truediv__(self, other)
    // ===== __floordiv__(self, other)
    % ====== __mod__(self, other)
    ** ===== __pow__(self, other)

    < ====== __it__(self, other)
    > ====== __gt__(self, other)
    <= ===== __le__(self, other)
    >= ===== __ge__(self, other)
    == ===== __eq__(self, other)
    != ===== __ne__(self, other)

    -= ===== __isub__(self, other)
    += ===== __iadd__(self, other)
    *= ===== __imul__(self, other)
    /= ===== __idiv__(self, other)
    //= ==== __ifloordiv__(self, other)
    %= ===== __imod__(self, other)
    **= ==== __ipow__(self, other)
"""