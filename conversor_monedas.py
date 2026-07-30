# Conversor MXN a 10 monedas - tasas ejemplo julio 2026
mxn = float(input("Cantidad en MXN: "))
print("1.USD 2.EUR 3.THB 4.JPY 5.KRW 6.AUD 7.PEN 8.CAD 9.VES 10.ARS")
op = int(input("Convierte a: "))

match op:
    case 1:
        print(f"${mxn} MXN = ${mxn*0.054:.2f} USD")
    case 2:
        print(f"${mxn} MXN = ${mxn*0.050:.2f} EUR")
    case 3:
        print(f"${mxn} MXN = ${mxn*1.95:.2f} THB")
    case 4:
        print(f"${mxn} MXN = ${mxn*8.45:.2f} JPY")
    case 5:
        print(f"${mxn} MXN = ${mxn*73.2:.2f} KRW")
    case 6:
        print(f"${mxn} MXN = ${mxn*0.082:.2f} AUD")
    case 7:
        print(f"${mxn} MXN = ${mxn*0.20:.2f} PEN")
    case 8:
        print(f"${mxn} MXN = ${mxn*0.074:.2f} CAD")
    case 9:
        print(f"${mxn} MXN = ${mxn*1.95:.2f} VES")
    case 10:
        print(f"${mxn} MXN = ${mxn*50.1:.2f} ARS")
    case _:
        print("Moneda no válida")
