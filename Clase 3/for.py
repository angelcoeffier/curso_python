'''
Ejemplo estructura de control for
'''

#Ejemplo en C++
# for (int i = 0; i < 10; i++) {
#     cout << "El valor de i es: " << i << endl;
# }
#contador=10
#for i in range(contador):
#    print("El valor de i es:", i) # Imprimir el valor de i
#print("Fin del bucle for")  # Mensaje al finalizar el bucle

# Ejemplo con una lista
array = ["futbol", "Pc", 18.6, 18, [6, 7, 10.4], True, False]   
print(len(array)) 
array.append("PC") 
print(array)
for i in range(len(array)):  # Iterar sobre el rango de la longitud del array
    print("El valor del array es:", array[i])   
print("Fin del bucle for con lista")  # Mensaje al finalizar el bucle   