def evaluar(num_victorias_a, num_victorias_b):
    # TODO: Coloca aquí el código del ejercicio 1: Set de tenis
    respuesta = "Ganó "
    x = 0
    y = 0
    if num_victorias_a>=num_victorias_b:
        x = num_victorias_a
        y = num_victorias_b
        respuesta += "A"
    else:
        x = num_victorias_b
        y = num_victorias_a
        respuesta += "B"
        
    match (x):
        case 6:
            if x-y<2: respuesta = "Aún no termina"
        case 7:
            if y!=5 and y!=6: respuesta = "Inválido"
        case _:
            if x<6: respuesta = "Aún no termina"
            else: respuesta = "Inválido"
        
    return respuesta

if __name__ == '__main__':
    print("Los juegos ganaddor por A:", end="")
    num_victorias_a = int(input())
    print("Los juegos ganaddor por B:", end="")
    num_victorias_b = int(input())

    respuesta = evaluar(num_victorias_a, num_victorias_b)
    print(respuesta)
