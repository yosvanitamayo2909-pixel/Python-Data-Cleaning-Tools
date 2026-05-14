def calcular_ganancias_netas(monto_bruto, impuesto_porcentaje, gasto_fijo):
    impuesto = monto_bruto * (impuesto_porcentaje/100)
    total = monto_bruto - impuesto - gasto_fijo
    return total

mi_dinero = calcular_ganancias_netas(5000, 5, 1000)

print(f'Mi dinero disponible para el mes es: {mi_dinero}')
