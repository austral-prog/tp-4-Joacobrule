def leap_year():
    Year=int(input("Ingrese un año: "))
    BiY= Year % 4
    CBiY= Year % 400
    NBiY= Year % 100
    if (BiY == 0 and NBiY != 0) or CBiY == 0:
        print(f"El año {Year} es bisiesto")
    else:
        print(f"El año {Year} no es bisiesto")
leap_year()
