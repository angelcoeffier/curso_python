'''
Ejemplos de listas en Python
'''

array = ["futbol", "Pc",18.6, 18,[6,7,10.4],True, False]

print(array)

# Acceso a los elementos de la lista
print(array[0])
print(array[4])
print(array[0:3]) 
print(len(array))  # Longitud de la lista   
array.append(66)  # Añadir un elemento al final de la lista
print(array)
array.insert(2, "baloncesto")  # Insertar un elemento en una posición específica
print(array)
array.extend(["tenis", "natación"])  # Añadir varios elementos al final de la lista
print(array)
array.remove("Pc")  # Eliminar un elemento específico
print(array)
array.pop()  # Eliminar el último elemento de la lista
print(array)
array.pop(2)  # Eliminar un elemento en una posición específica
print(array)
array.clear()  # Limpiar la lista
print(array)
array = ["futbol", "Pc", 18.6, 18, [6, 7, 10.4], True, False]  # Volver a inicializar la lista
array2=["baloncesto", "tenis", "natación"]
array3 = array + array2  # Concatenar dos listas
print(array3)
print("futbol" in array3) 
print(array3.index("baloncesto")) 
print(array3.count("natación"))  # Contar cuántas veces aparece un elemento en la lista
array4=[1,2,3,4,5,6,7,8,9,10]
array4.reverse()  # Invertir el orden de los elementos en la lista
print(array4)
array5=[1,3,2,4,6,5,8,7,9,10]
array5.sort()  # Ordenar los elementos de la lista
print(array5)   
