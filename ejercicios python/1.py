resp = "aplica"
while resp == "aplica" or "si" or "si aplica" or "cuanto es la bonificacion":
    
    sueldo = float(input("Digite su sueldo:  "))
    
    if sueldo <= 655000:
        sueldo = sueldo 
        bono = sueldo * 0.04
        total = bono + sueldo
        print("Tienebonificacion del 4% sobre el sueldo base devengado = ${:,.0f} y el total a pagar es = ${:,.0f}".format(sueldo,total))
    else:
        print("No tiene bonificacion, el total a pagar es = ${:,.0f}".format(sueldo))
        resp = input("¿Decea calcular otro sueldo? ")
        