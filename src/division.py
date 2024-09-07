def evaluar(dividendo, divisor):
    # TODO: Coloca aquí el código del ejercicio 3: Division
    cociente = (int)(dividendo/divisor)
    residuo = dividendo%divisor
    respuesta = " es exacta. \n" \
            "Cociente: " + str(cociente) + "\n" \
            "Residuo: " + str(residuo)
    if residuo!=0: respuesta = "La división no"+respuesta
    else: respuesta = "La división"+respuesta
    return respuesta

if __name__ == '__main__':
    print("Dividendo:", end="")
    dividendo = int(input())
    print("Divisor:", end="")
    divisor = int(input())

    respuesta = evaluar(dividendo, divisor)
    print(respuesta)
