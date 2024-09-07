def evaluar(a, b, c):
    # TODO: Coloca aquí el código del ejercicio 1: Set de tenis
    respuesta = "No es un triángulo válido"
    if a<b+c and b<a+c and c<a+b:
        respuesta = "El triángulo es "
        if a==b or a==c:
            if b==c: respuesta += "equilátero"
            else: respuesta += "isósceles"
        elif b==c: respuesta += "isósceles"
        else: respuesta += "escaleno"
        
    return respuesta

if __name__ == '__main__':
    print("a:", end="")
    a = float(input())
    print("b:", end="")
    b = float(input())
    print("c:", end="")
    c = float(input())
        
    respuesta = evaluar(a, b, c)
    print(respuesta)
