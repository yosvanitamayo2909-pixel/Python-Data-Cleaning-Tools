total_procesado = 0.0

while True:

    id = input('Escriba el ID de la transaccion (o fin para terminar y ver el cierre): ')
    id_limpio = ''

    if id.lower() == 'fin':
        break
    for new in id:
        if new != ' ' and new != '.':
            id_limpio += new

    id_limpio = id_limpio.upper()

    if not id_limpio.startswith('TX'):
        print('Error: ID de transacción inválido ❌')
    elif len(id_limpio) < 5:
        print('Error: ID demasiado corto ⚠️')
    else:
        monto = input('Escriba el monto a depositar: ')
        if monto.replace('.', '', 1).isdigit():
            monto = float(monto)
            total_procesado += monto
            print(f'Depósito {id_limpio} por {monto:.2f} USDT aceptado ✅')
        else:
            print('Monto invalido. Intentelo de nuevo.')

print(f'El total de todos los depositos acumulados es {total_procesado} USD. Que tenga un excelente dia')
