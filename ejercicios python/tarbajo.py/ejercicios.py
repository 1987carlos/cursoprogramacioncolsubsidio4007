cal1 = float(input("Digite la calificacion 1: "))
cal2 = float(input("Digite la calificacion 2: "))
cal3 = float(input("Digite la calificacion 3: "))


prom = round((cal1 + cal2 + cal3)/3, 2)

if prom < 3.0:
    estado =  "Reprobado --"
else:
    estado = "Aprobado ++"
    
    print(f"El promedrio es= {prom} y el estado es= {estado}")
    
