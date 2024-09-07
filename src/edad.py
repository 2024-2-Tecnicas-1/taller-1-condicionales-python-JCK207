from time import localtime

def evaluar(dia, mes, anno):
    # TODO: Coloca aquí el código del ejercicio 6: Edad
    t = localtime()
    diaL = t.tm_mday
    mesL = t.tm_mon
    annoL = t.tm_year
    annosT = annoL-anno
    if mes>=mesL and dia>diaL: annosT -= 1
    return "Usted tiene "+(str)(annosT)+ " años"

if __name__ == '__main__':
    print("Ingrese su fecha de nacimiento")
    print("Día:", end="")
    dia = int(input())
    print("Mes:", end="")
    mes = int(input())
    print("Año:", end="")
    anno = int(input())
        
    respuesta = evaluar(dia, mes, anno)
    print(respuesta)
