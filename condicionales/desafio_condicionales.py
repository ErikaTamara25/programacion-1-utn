# Tarifa base:
# Todas las facturas incluyen un cargo fijo de $7000 además del costo por consumo.
# El costo por metro cúbico (m³) de agua es de $200/m³.
# Bonificaciones y Recargos según tipo de cliente:
# Cliente Residencial:
# Si el consumo es menor a 30 m³, se aplica una bonificación del 10% sobre el costo del consumo.
# Si el consumo supera los 80 m³, se aplica un recargo del 15% sobre el costo del consumo.
# Cliente Comercial:
# Si el consumo es superior a 150 m³, se aplica una bonificación del 8% sobre el costo del consumo.
# Si el consumo supera los 300 m³, la bonificación aumenta al 12%.
# Si el consumo es menor a 50 m³, se aplica un recargo del 5%.
# Cliente Industrial:
# Si el consumo es superior a 500 m³, se aplica una bonificación del 20% sobre el costo del 
# consumo.
# Si el consumo supera los 1,000 m³, la bonificación aumenta al 30%.

# Si el consumo es menor a 200 m³, se aplica un recargo del 10%.
# Casos especiales:
# Si el cliente es Residencial y el total de la factura sin impuestos ni bonificaciones  es menor a $35000, se aplica un descuento adicional del 5%.
# En todos los casos, se aplica el IVA del 21% sobre el total.
# Requerimientos del programa:
# Solicitar al usuario:
# Cantidad de metros consumidos
# Tipo de cliente, que puede ser: Residencial, Comercial o Industrial.
# Calcular:
# Subtotal de consumo.
# Bonificaciones, si corresponde
# Recargos, si corresponde
# Subtotal, con recargos y bonificaciones.
# IVA aplicado (21%), si corresponde.
# Total final a pagar.
# Mostrar en pantalla el desglose de los cálculos.


tipo_cliente = input('Ingrese tipo de cliente (Residencial/Comercial/Industrial) ')
metros_consumo = int(input('Ingrese consumo de metros cubicos '))


cargo_fijo = 7000
costo_por_m3 = 200
subtotal_consumo = costo_por_m3 * metros_consumo
bonificacion = 0
recargo = 0



match tipo_cliente:
    case 'Residencial':
        if metros_consumo < 30:
            bonificacion = 10 
        elif metros_consumo > 80:
            recargo = 15

        subtotal_sin_impuestos = cargo_fijo + subtotal_consumo 

        if subtotal_sin_impuestos < 35000:
            descuento_especial =  subtotal_sin_impuestos * 5 / 100

    case 'Comercial':
        if metros_consumo > 300:
            bonificacion = 12
        elif metros_consumo > 150:
            bonificacion = 8
        elif metros_consumo < 50:
            recargo = 5

    case 'Industrial':
        if metros_consumo > 1000:
            bonificacion = 30
        elif metros_consumo > 500:
            bonificacion = 20
        elif metros_consumo < 200:
            recargo = 10
    case _:
        print('Cliente inválido')


bonificacion = subtotal_consumo * bonificacion / 100
recargo =  subtotal_consumo * recargo / 100
total_impuestos = cargo_fijo + subtotal_consumo - bonificacion + recargo - descuento_especial
        
iva = total_impuestos * 0.21
total_final = total_impuestos + iva


print(f'El subtotal del consumo es de {subtotal_consumo}')
print(f'Tiene bonificacion de {bonificacion}')
print(f'Tiene recargo de{recargo}')
print(f'subtotal con recargos y bonificaciones{total_impuestos}')
print(f'iva aplicado de {iva}')
print(f'precio total final{total_final}')
