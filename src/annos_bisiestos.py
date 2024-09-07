def evaluar(anno):
    # TODO: Coloca aquí el código del ejercicio 2: Años bisiestos
    respuesta = " es bisiesto"
    if anno%4!=0: respuesta = " no"+respuesta
    elif anno%400!=0 and anno%100==0: respuesta = " no"+respuesta
    return str(anno)+respuesta

if __name__ == '__main__':
    print("Año:", end="")
    anno = int(input())

    respuesta = evaluar(anno)
    print(respuesta)
