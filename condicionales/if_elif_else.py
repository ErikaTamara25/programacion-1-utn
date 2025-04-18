# IF - ELSE -ELIF

#1)
# A partir del ingreso de la altura en centímetros de un jugador de baloncesto, 
# el programa deberá determinar la posición del jugador en la cancha, considerando los siguientes parámetros:
# Menos de 160 cm: Base
# Entre 160 cm y 179 cm: Escolta
# Entre 180 cm y 199 cm: Alero
# 200 cm o más: Ala-Pívot o Pívot

ingreso_altura = int(input('Ingrese altura en cm '))

if ingreso_altura < 160:
    print('Posición base')
elif ingreso_altura >= 160 and ingreso_altura <= 179:
    print('Posición escolta')
elif ingreso_altura >= 180 and ingreso_altura <= 199:
    print('Posición alero')
else:
    print('Posición pivot')

#2)
# Calcular una nota aleatoria entre el 1 y el 10 inclusive, para luego mostrar un mensaje según el valor:
# 6, 7, 8, 9 y 10  ---> Promoción directa, la nota es ...
# 4 y 5                ---> Aprobado, la nota es ...
# 1, 2 y 3            ---> Desaprobado, la nota es ...

import random

nota_aleatoria = random.randint(1, 10)

if nota_aleatoria >= 6:
    print(f'Promoción directa, la nota es {nota_aleatoria}')
elif nota_aleatoria >= 4:
    print(f'Aprobado, la nota es {nota_aleatoria}')
else:
    print(f'Desaprobado, la nota es {nota_aleatoria}')

