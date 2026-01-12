def cuadrada():
    numero = float(input("Ingrese el número para calcular su raíz cuadrada: "))
    if numero < 0:
        print("Error: No se puede calcular la raíz cuadrada de un número negativo.")
    else:
        resultado = numero ** 0.5
        print(f"La raíz cuadrada de {numero} es {resultado}")