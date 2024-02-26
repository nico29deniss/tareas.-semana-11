# Definir una matriz 3x3 con valores numéricos
matriz_soto = [
    [12, 54, 27],
    [33, 91, 46],
    [65, 78, 82]
]

# Mostrar la matriz original
print("Matriz Original:")
for fila in matriz_soto:
    print(fila)

# Solicitar al usuario la fila que desea ordenar
fila_a_ordenar = int(input("Ingrese el número de fila que desea ordenar (0, 1, o 2): "))

# Utilizar el algoritmo de ordenación de burbuja para ordenar la fila específica
fila = matriz_soto[fila_a_ordenar]
n = len(fila)

for i in range(n - 1):
    for j in range(0, n - i - 1):
        if fila[j] > fila[j + 1]:
            # Intercambiar elementos si están en el orden incorrecto
            fila[j], fila[j + 1] = fila[j + 1], fila[j]

# Mostrar la matriz con la fila ordenada
print("\nMatriz con la Fila Ordenada:")
for fila in matriz_soto:
    print(fila)