# crear una variable nombre de tipo string con el valor inicial "Python" a la variable nombre:
# 1) ponerla en mayusculas y mostrar en pantalla
# 2) ponerla en minusculas y mostrar en pantalla
# 3) mostrar la longitud de la cadena
# 4) mostrar la primera letra de la cadena
# 5) mostrar la ultima letra de la cadena
# 6) mostrar la letra que esta en la posicion 3 de la cadena
# 7) mostrar la cadena en orden inverso
# 8) mostrar la cadena en orden inverso pero sin la primera letra
# 9) mostrar la cadena en orden inverso pero sin la ultima letra
# 10) mostrar la cadena en orden inverso pero sin la primera ni la ultima letra
# 11) mostrar la cadena en orden inverso pero solo los 3 ultimos caracteres
# 12) mostrar la cadena en orden inverso pero solo los 3 primeros caracteres
# 13) mostrar la cadena en orden inverso pero solo los 3 ultimos y los 3 primeros caracteres pero en mayusculas
# 14) concatenar la cadena con la cadena " es un lenguaje de programacion"
# 15) concatenar la cadena con la cadena " es un lenguaje de programacion" y mostrar la longitud de la cadena resultante

#ej ejercicio1 
lenguaje = "Python"
print(lenguaje.upper()) 

#2)
lenguaje = "Python"
print(lenguaje.lower())

#3) 
lenguaje = "Python"
print(len(lenguaje)) 

#4)
lenguaje = "Python"
print(lenguaje[0]) 

#5)
lenguaje = "Python"
print(lenguaje[-1]) 

#6)
lenguaje = "Python"
print(lenguaje[2])

#7)
cadena = "Python"
invertida = cadena[::-1] 
print(invertida)

#8)     
cadena = "Python"
invertida = invertida[1:]
print(invertida)

#9) 
cadena = "Python" 
cadena_inversa_sin_ultima = cadena[::-1][:-1]
print(cadena_inversa_sin_ultima)

#10)
cadena = "Python"
cadena_inversa_sin_primera_y_ultima = cadena[::-1][1:-1]
print(cadena_inversa_sin_primera_y_ultima)

#11)
cadena = "Python"
resultado = cadena[-3:][::-1]
print(resultado)

#12) 
cadena = "Python"
resultado = cadena[:3][::-1]
print(resultado) 


#13)
cadena = "Python"
resultado = cadena[:3][::-1].upper() + cadena[-3:][::-1].lower()
print(resultado)

#14) 
cadena = "Python"
extension = " es un lenguaje de programación"
resultado = cadena + extension
print(resultado)

#15
cadena = "Python"
extension = " es un lenguaje de programación"
resultado = cadena + extension
print(len(resultado))



