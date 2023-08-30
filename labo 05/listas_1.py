edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
edades.sort()
E_min = edades[0]
E_max = edades[-1]
#edad minima y maxima
print("la edad minima es: ", E_min)
print("la edad maxima es: ", E_max)
#agregar la notas minima y maxima a la lista
edades.insert(10, 19)
edades.insert(11, 24)
print(edades)
#edad mediana
edad_med = edades[5] + edades[6] /2
print(edad_med)
#edad promedio
promedio = sum(edades)/len(edades)
print("el promedio es: ", promedio)
#encuentra el rango de edades
edades.sort()
r_min = edades[0]
r_max = edades[-1]
ran_edad = r_max - r_min
print("el rango de edad es: ", ran_edad)
#comparar el valor
Valor_1 = r_min - promedio
Valor_2 = r_max - promedio
valor_comparado = abs(Valor_1 - Valor_2)
print("El valor comparado es: ", valor_comparado)
