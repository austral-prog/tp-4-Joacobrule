import math
def line():    
    CA=float(input("Ingrese el coeficiente A: "))
    CB=float(input("Ingrese el coeficiente B: "))
    CX1=float(input("Ingrese el coeficiente X1: "))
    CX2=float(input("Ingrese el coeficiente X2: "))
    print(f"El coeficiente A de su ecuación de la recta es: {CA}")
    print(f"El coeficiente B de su ecuación de la recta es: {CB}")
    print(f"El coeficiente X1 de su ecuación de la recta es: {CX1}")
    print(f"El coeficiente X2 de su ecuación de la recta es: {CX2}")
    print("")
    print("Para la siguiente ecuación:")
    print(f"\tY = {CA}X + {CB}")
    print("")
    print("Dados los siguientes puntos:")

    Y1=CA*CX1 + CB
    Y2=CA*CX2 + CB

    print(f"\tP1 ({CX1}, {Y1})")
    print(f"\tP2 ({CX2}, {Y2})")
    print("")

    XY1=(CX1,Y1)
    XY2=(CX2,Y2)
    abc = math.dist(XY1, XY2)
    print(f"La distancia entre ellos es: {abc}")
