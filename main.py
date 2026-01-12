from adicionando import suma
from restando import resta
from multiplicando import multiplicar
from dividiendo import dividir
from exponente import potencia
from raiz import cuadrada
from login import loguear
from tabla import multiplicar_tabla

nombre="Anonimo"


def main():
    if loguear("admin", "1234"):
        print(f"Bievenido a la calculadora que he hecho despues de ir aumentando mi nivel  {nombre}")
        decision = (input("¿Desea usar la calculadora? (si/no):")).lower()

    TUPLA=(
    "1) Suma",
    "2) Resta",
    "3) Multiplicación",
    "4) División",
    "5) potencia",
    "6) raiz cuadrada",
    "7) Tablas de multiplicar",
    "8) salir"
    )


    try:
        if decision=="si":
            while True:

                print( "la calculadora está en desarrollo" )

                for i in TUPLA:
                    print(i)

                operacion=int(input("seleccione la operación que desea realizar : "))

                if operacion ==1:
                    suma()
                    decision = str(input("¿Desea realizar otra operación? (si/no):")).lower()
                    if decision == "si":
                        print("perfecto, continuemos")
                    else:
                        print("gracias por usar la calculadora, hasta luego")
                        break
                elif operacion ==2:
                    resta()
                    decision = str(input("¿Desea realizar otra operación? (si/no):")).lower()
                    if decision == "si":
                        print("perfecto, continuemos")
                    else:
                        print("gracias por usar la calculadora, hasta luego")
                        break
                elif operacion ==3:
                    multiplicar()
                    decision = str(input("¿Desea realizar otra operación? (si/no):")).lower()
                    if decision == "si":
                        print("perfecto, continuemos")
                    else:
                        print("gracias por usar la calculadora, hasta luego")
                        break   

                elif operacion ==4:    
                    dividir()
                    decision = str(input("¿Desea realizar otra operación? (si/no):")).lower()
                    if decision == "si":
                        print("perfecto, continuemos")
                    else:
                        print("gracias por usar la calculadora, hasta luego")
                        break


                elif operacion ==5:
                    print("en este momento se realizara una potencia")
                    potencia()
                    decision = str(input("¿Desea realizar otra operación? (si/no):")).lower()
                    if decision == "si":
                        print("perfecto, continuemos")
                    else:
                        print("gracias por usar la calculadora, hasta luego")
                        break
                elif operacion ==6:
                    print("en este momento se realizara una raiz cuadrada")
                    cuadrada()
                    decision = str(input("¿Desea realizar otra operación? (si/no):")).lower()

                    if decision == "si":
                        print("perfecto, continuemos")

                    elif decision == "no":
                        print("gracias por usar la calculadora, hasta luego")
                        break
                    else:
                        print("Ingrese una opción válida (si/no).")
                        
                        
                elif operacion ==7:
                    if not multiplicar_tabla():
                        print("gracias por usar la calculadora, hasta luego")
                        break

                elif operacion ==8:
                    print("gracias por usar la calculadora, hasta luego")
                    break   
                    

                else:
                    print("Operación no válida. Por favor, seleccione una opción del 1 al 8.")

    except ValueError:
        print("Ha ocurrido un error. Por favor, asegúrese de ingresar valores válidos.")       

    
    finally:
        opinion = str(input("¿Desea dejar una opinión sobre la calculadora? (si/no):")).lower()
        if opinion == "si":
            comentario = str(input("Por favor, deje su opinión aquí: "))
            persona=str(input("Por favor, ingrese su nombre: "))
            print("Gracias por su opinión:", comentario)
        else:
            print("Gracias por usar la calculadora. ¡Hasta luego!")
        with open("calificaciones.txt", "a") as archivo:
            if opinion == "si":
                archivo.write(f"Opinión de {persona}: {comentario}\n")
            else:
                archivo.write("El usuario no dejó una opinión.\n")



if __name__ == "__main__":
    main()