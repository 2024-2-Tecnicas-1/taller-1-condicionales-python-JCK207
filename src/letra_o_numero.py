def evaluar(caracter):
    # TODO: Coloca aquí el código del ejercicio 4: Letra o número
    respuesta = "No es letra ni número"
    if 48<=(ord)(caracter)<=57: respuesta = "Es número"
    if 65<=(ord)(caracter)<=90: respuesta = "Es letra mayúscula"
    if 97<=(ord)(caracter)<=122: respuesta = "Es letra minúscula"
    return respuesta

if __name__ == '__main__':
    print("Caracter:", end='')
    caracter = input()
        
    respuesta = evaluar(caracter)
    print(respuesta)
