def multiplicar_tabla():
    try:



        diccionario_tablas={
        1: "ver varias tablas de multiplicar",
        2: "ver una tabla de multiplicar",
        3: "salir"}


        for clave in diccionario_tablas:
            print(f"{clave}) {diccionario_tablas[clave]}")


        decision=int(input("Elija una opcion del menu :"))
        print()

        if decision== 1:
            inicio=int(input("Ingrese el número inicial para las tablas de multiplicar: "))
            fin=int(input("Ingrese el número final para las tablas de multiplicar: "))
            limite=int(input("Ingrese hasta qué número desea multiplicar: "))

            print()
            for num in range(inicio, fin + 1):
                print(f"Tabla de multiplicar del {num} hasta el {limite}:")
                for i in range(1, limite + 1):
                    resultado = num * i
                    print(f"{num} x {i} = {resultado}")
                print()
        
        
        elif decision==2:
            print(f"haz seleccionado con Exito la opcion {diccionario_tablas[2]}")
            num1=int(input("Ingrese el número para generar su tabla de multiplicar: "))
            limite=int(input("Ingrese hasta qué número desea multiplicar: "))


            print()
            print(f"Tabla de multiplicar del {num1} hasta el {limite}:")
            for i in range(1, limite + 1):
                resultado = num1 * i
                print(f"{num1} x {i} = {resultado}")
            print()

        elif decision==3:
            print("saliendo...")
            return False   

    except ValueError:
        print("Error: Entrada inválida. Por favor, ingrese un número entero.")
        

        
