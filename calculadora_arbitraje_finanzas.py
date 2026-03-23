# Script para cálculo de comisiones y montos netos (Crypto Fee Calculator)
# Incluye validación de entrada numérica para evitar caídas del sistema.

while True:
    entrada = input('Monto total a enviar en USDT (o "fin"): ').strip()

    if entrada.lower() == 'fin':
        break

    # Truco de seguridad para aceptar decimales
    if entrada.replace(".", "", 1).isdigit():
        monto = float(entrada)
        comision = monto * 0.02  # Comisión fija del 2%
        neto = monto - comision
        
        print(f"--- Recibo de Transacción ---")
        print(f"Neto a enviar: {neto:.2f} USDT")
        print(f"Comisión Red:  {comision:.2f} USDT")
        print(f"-----------------------------")
    else:
        print("Error: Ingrese un monto numérico válido.")
