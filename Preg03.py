horas= int(input("Horas: "))

if horas<=4:
    costo=6.0
else:
    costo=6.0+(horas-4)*2.0
    
print("Importe a pagar:",costo)