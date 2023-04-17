compra = float(input("¿Cuanto fue el total de la compra?:"))

if  compra > 800000:
    descu = compra * 0.10
    total = compra - descu
    print("El descuento fue = ${:,.0f} y el total a pagar es = ${:,.0f}".format(descu,total))
else:
    print("No tiene descuento, el total a pagar es = ${:,.0f}".format(compra))

