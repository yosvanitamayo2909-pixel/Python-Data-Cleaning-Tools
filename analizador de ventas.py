# Datos brutos (como vendrían de un archivo externo)
datos_ventas = [
    "001 | Teclado | 2 | 25 | Madrid",
    "002 | Monitor | 1 | 150 | Barcelona",
    "003 | Mouse | 5 | 10 | Madrid",
    "004 | Laptop | 1 | 800 | Valencia",
    "005 | Teclado | 3 | 25 | Madrid"
]

ventas_madrid = []
totales = 0

for data in datos_ventas:
    partes = data.split(' | ')
    if partes[4].lower() == 'madrid':
        cantidad = int(partes[2])
        precio = int(partes[3])
        total = cantidad * precio
        totales += total
        ventas_madrid.append((partes[1], total))


print(f'Aqui se muestran los productos con su respectiva ganancia: {ventas_madrid}. En total serian {totales}')
