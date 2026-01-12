def dividir():
    print("apartir de ahora puede iniciar la división que desea")
    num1=float(input("Ingrese el primer número: "))
    num2=float(input("Ingrese el segundo número: "))
    if num2 == 0:
        print("Error: No se puede dividir entre cero.")
    else:
        print(f"La división es {num1}/{num2} el resultado es {num1 / num2}")
        