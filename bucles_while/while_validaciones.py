# Validaciones

# Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Tendrá intentos indeterminados.
# Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Solo tendrá 3 intentos.
# Pedir al usuario el ingreso de una nota. La misma debe estar comprendida entre 1 y 10 inclusive.
# Solicitarle al usuario el ingreso de un color. Validar que el mismo sea Rojo, Verde o Azul.

# Integrador Validaciones
# Una empresa dedicada a la toma de datos para realizar estadísticas y censos, nos pide realizar la carga y validación de datos.
 
# Los datos requeridos son:
# Apellido
# Edad, entre 18 y 90 años inclusive.
# Estado civil: “Soltero/a”, ”Casado/a”, “Divorciado/a” o “Viudo/a”.
# Número de legajo: valor numérico de 4 cifras, sin ceros a la izquierda.

# Una vez ingresados y validados los datos, mostrarlos por pantalla.

#EJERCICIO 1

ingresar_clave = input('Ingresar clave ')

clave = 'Pepe'

while ingresar_clave != clave:
    ingresar_clave = input('Error, reingresar clave ')

# # #EJERCICIO 2

contador = 1

ingresar_clave2 = input('Ingrese clave ')

clave2 = 'Pepo'

while contador < 3 and ingresar_clave2 != clave2:
    ingresar_clave2 = input('Error, reingrese clave ')
    contador += 1

# #EJERCICIO 3

ingresar_nota = int(input('Ingrese nota del 1 al 10 '))

while ingresar_nota < 0 or ingresar_nota > 10:
    ingresar_nota = int(input('Error, reingresar nota '))

#EJERCICIO 4

ingresar_color = input('Ingrese un color ')

while ingresar_color != 'Rojo' and ingresar_color != 'Verde' and ingresar_color != 'Azul':
    ingresar_color = input('Error, reingrese color ')

#EJERCICIO 5


ingresar_apellido = input('Ingrese su apellido ')
ingresar_edad = int(input('Ingrese su edad '))

while ingresar_edad < 18  or ingresar_edad > 90:
    ingresar_edad = int(input('Error, reingresar edad '))

estado_civil = input('Ingresar estado civil “Soltero/a”, ”Casado/a”, “Divorciado/a” o “Viudo/a”. ')

while estado_civil != 'Soltero' and estado_civil != 'Viudo' and estado_civil != 'Divorciado' and estado_civil != 'Casado':
    estado_civil = input('Error, reingrese estado civil ')

numero_legajo = int(input('Ingrese 4 cifras sin ceros a la izquierda '))

while numero_legajo < 1000 or numero_legajo > 9999:
    numero_legajo = int(input('Error, reingrese numero de legajo '))


print(f'Su apellido es {ingresar_apellido}. Usted tiene {ingresar_edad} años.')
print(f'Estado civil: {estado_civil}. Numero de legajo: {numero_legajo}')






