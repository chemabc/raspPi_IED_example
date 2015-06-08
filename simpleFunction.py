#Creamos una función.
''' Una función es un pedazo de código que se va a usar muchas veces.
En vez de escribirlo como los anteriores, lo escribimos en la forma
de función que tendrá un nombre apropiado. Cada vez que llamemos a
esa función por su nombre se ejecutara el pedazo de código que contiene.
Además permite aceptar parámetros y devolver un resultado.
Ejemplo: función suma. ¿Cómo se escribiría en nuestro lenguaje?
'''
#1) Primero definimos la función con "def" + nombreFuncion + (parametros...):
def suma(num1, num2):
    return num1 + num2

#2) Luego la usamos desde nuestro código:
resultado = suma (3, 5)
print(resultado)

