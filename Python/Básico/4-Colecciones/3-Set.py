"""
    No mantiene un orden, tampoco permite almacenar elementos dupkicados, no permite modificar elementos pero si permite
    eliminarlos o alargar mas elementos.
"""

planetas = {'Marte', 'Jupiter', 'Venus'}
print(planetas)
#Conocer largo
print(len(planetas))
#Revisar si un elemento está presente
print('Marte' in planetas)
#Agregar un elemento
planetas.add('Tierra')
print(planetas)
#Eliminar elemento
planetas.remove('Tierra')# Con .discard si elimina un elemento que no existe no da error
print(planetas)
#Limpiar set
planetas.clear()
print(planetas)
#Eliminar el set
del planetas
print(planetas)