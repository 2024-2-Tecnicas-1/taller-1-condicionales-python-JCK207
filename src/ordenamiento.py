def evaluar(numero1, numero2, numero3, numero4):
    # TODO: Coloca aquí el código del ejercicio 5: Ordenamiento
    arreglo = [numero1, numero2, numero3, numero4]
    arreglo.sort()
    respuesta = ""
    for i in range (0, len(arreglo), 1):
        respuesta += (str)(arreglo[i])
        if i<len(arreglo)-1: respuesta += " "
    return respuesta

if __name__ == '__main__':
    print("Número 1:", end="")
    numero1 = int(input())
    print("Número 2:", end="")
    numero2 = int(input())
    print("Número 3:", end="")
    numero3 = int(input())
    print("Número 4:", end="")
    numero4 = int(input())
        
    respuesta = evaluar(numero1, numero2, numero3, numero4)
    print(respuesta)
