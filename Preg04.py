ganancias=float(input("Ganancia:"))

if ganancias<=1000:
    donativo=ganancias * 0.05
elif ganancias<=1500:
    donativo=ganancias * 0.07
elif ganancias<=2000:
    donativo=ganancias * 0.08
elif ganancias<=5000:
    donativo=ganancias * 0.10
else:
    donativo=ganancias * 0.15

print("Donacion:",donativo)