#Un maestro desea saber qué porcentaje de hombres y que
#porcentaje de mujeres hay en un grupo de estudiantes.

a = float(input("ingresa el numero de mujeres: "))
b = float(input("ingresa el numero de hombres: "))

total = a + b
print("el porcentaje de mujeres es:",(a / total) * 100)
print("el porcentaje de hombres es:",(b/total) * 100)