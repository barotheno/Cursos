'''
    En python tenemos diferentes tipos de clases de errores que nos pueden lanzar, las clasificamos segun gerarquía:

                                        BaseException
                                        Exception

        AritmeticError  OSError RuntimeError    LookupError     SyntaxError

        ZerodivisionError

                    FileNotFoundError   PermissionError     IndexError      KeyError

    Creando un ejemplo, si realizamos una operacion por ejemplo:
    10/0
    El resultado sera un error, en este caso ZerodivisionError
    Para procesar dicho error y evitar que el programa termine de forma abrupta, hacemos lo siguiente:           
'''
# De esta forma capturamos un posible error.
try:
    10/0
except Exception as e:
    print(f'Ocurrió un error: {e}')