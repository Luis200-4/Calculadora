def loguear(user, password):
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    
    if usuario==user and contraseña==password:
        print(f"Bienvenido, {usuario}!")
        return True
    else:
        print("Nombre de usuario o contraseña incorrectos.")
        return False
    
    