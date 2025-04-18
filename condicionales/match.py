# Una agencia de viajes nos pide informar si hacemos viajes a lugares según la estación del año. 
# En caso de hacerlo mostrar por print  el mensaje “Se viaja”, caso contrario mostrar “No se viaja”. 
# Si es invierno: solo se viaja a Bariloche.
# Si es verano: se viaja a Mar del plata y Cataratas.
# Si es otoño: se viaja a todos los lugares.
# Si es primavera: se viaja a todos los lugares menos Bariloche.


estacion_del_año = input('Ingrese estación del año ')
hace_viaje = input('Ingrese lugar de viaje(Bariloche/Mar del Plata/Cataratas) ')

viaja = False

match estacion_del_año:
    case 'Invierno':
        if hace_viaje == 'Bariloche':
            viaja = True
    case 'Verano':
        if hace_viaje == 'Mar del Plata' or hace_viaje == 'Cataratas':
            viaja = True
    case 'Otoño':
        viaja = True
    case 'Primavera':
        if hace_viaje != 'Bariloche':
            viaja = True
    case _:
        print('Estacion inválida')

if viaja:
    print('Se viaja.')
else:
    print('No se viaja')

