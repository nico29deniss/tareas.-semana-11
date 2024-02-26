# Definir una matriz 3x3 con valores numéricos
matriz_nico = [
    [18, 92, 63],
    [42, 25, 67],
    [57, 38, 79]
]

# Función para buscar un valor específico en la matriz
def buscar_valor(matriz, valor_buscar):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor_buscar:
                return f"El valor {valor_buscar} se encontró dentro de la matriz en la fila {i} y columna {j}."
    return f"El valor {valor_buscar} no se encontró en la matriz."

# Valor específico a buscar en la matriz
valor_a_buscar = 25

# Llamada a la función y mostrar el resultado
resultado = buscar_valor(matriz_nico, valor_a_buscar)
print(resultado)