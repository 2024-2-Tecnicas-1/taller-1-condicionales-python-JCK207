def evaluar(peso, estatura, edad):
    # TODO: Coloca aquí el código del ejercicio 8: Índice de masa corporal
    IMC = peso/estatura**2
    respuesta = ""
    if IMC<22:
        if edad<45: respuesta = "bajo"
        else: respuesta = "medio"
    elif edad<45: respuesta = "medio"
    else: respuesta = "alto"
        
    return respuesta

if __name__ == '__main__':
    print("Peso:", end="")
    peso = int(input())
    print("Estatura:", end="")
    estatura = float(input())
    print("Edad:", end="")
    edad = int(input())
        
    respuesta = evaluar(peso, estatura, edad)
    print(respuesta)
