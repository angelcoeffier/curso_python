'''
Crear un programa que pida dos numeros
y obtenga como resultado cual de ellos es par
o si ambos lo son.
# Si ambos son pares, mostrar el mensaje "Ambos numeros son pares"
# Si uno es par y el otro impar, mostrar "Uno es par y el otro impar
'''

a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese otro numero: "))

if (a % 2 == 0) and (b % 2 == 0):
    print("Ambos numeros son pares")
elif (a % 2 == 0) or (b % 2 == 0):
    print("Un numero es par y el otro numero es impar")
else:
    print("Ambos numeros son impares")