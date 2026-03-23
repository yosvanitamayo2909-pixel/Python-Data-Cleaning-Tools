# Script para limpieza masiva de productos (Data Cleaning)
# Elimina: Símbolos, IDs internos, guiones y espacios basura.

while True:
    dato_sucio = input('Ingrese nombre sucio del producto (o "salir"): ')
    
    if dato_sucio.lower() == 'salir':
        break
        
    # Limpieza en cadena: eliminamos $, _, IDs y normalizamos a mayúsculas
    limpio = dato_sucio.replace("$", "").replace("_", " ").replace("ID-99", "").strip().upper()

    if len(limpio) > 3:
        print(f'Producto Normalizado: {limpio} ✅')
    else:
        print('Error: El dato extraído es insuficiente o corrupto ❌')
