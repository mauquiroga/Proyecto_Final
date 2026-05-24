# inicio del programa es el usuario y contraseña
Nombre_de_Usuario = "Antonio "
Contraseña = "Quiroga"
# aqui verificamos si los datos son correctos
while True :
    Usuario = input ("ingrese usuario ")
    Clave = input ("ingrese contraseña ")
    if Usuario == Nombre_de_Usuario.strip().upper() and Clave == Contraseña.strip().lower() :
        print ("Datos correctos Acceso permitido ")
        break #el break es temporal lo cambiaremos por un continue
    else :
        print("Datos incorrectos intente de nuevo ")