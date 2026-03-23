# Script profesional para validación de direcciones de red (ERC-20)
# Valida: Prefijo, Longitud y Caracteres Alfanuméricos.

while True:
    wallet = input('Dirección de wallet (o "fin" para salir): ').strip()

    if wallet.lower() == 'fin':
        break
    
    # Reglas: Empieza con 0x, solo letras/números y tiene 42 caracteres
    if wallet.startswith('0x') and wallet.isalnum() and len(wallet) == 42:
        print(f'Billetera Válida: {wallet} ✅')
    else:
        print('Error: Dirección de billetera corrupta o inválida ❌')

print("Proceso finalizado.")
