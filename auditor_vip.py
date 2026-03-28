datos = " yosvani : 1500 | erik : 900 | ana : 2500 | luis : 500 "

players = datos.split('|')
suma_vip = 0.0

for data in players:
    partes = data.split(':')
    nombre = partes[0].strip()
    puntos = partes[1].strip()
    if int(puntos) > 1000:
        suma_vip += int(puntos)
        print(f'¡Jugador VIP detectado: {nombre.upper()} con {puntos} puntos! 🏆')
        
print(f'La suma de todos los puntos de VIP es {suma_vip}')
