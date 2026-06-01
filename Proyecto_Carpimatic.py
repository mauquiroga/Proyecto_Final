nombre="mau"
contraseña="123"
while True:
    print("""Bienvenido al Sistema
            ***Carpimatic***
            Por favor, selecciona una opcion:
            1.Inciar sesion.
            2.Registrarse
            3.Salir""")
    opcion=int(input(" "))
   
    if opcion==1:
            nombreusuario=input("Ingrese su Nombre: ")
            nombreusuario.lower()
            contraseñausuario=input("Ingrese una Contraseña: ")
            contraseñausuario.lower()
            if nombre==nombreusuario and contraseña==contraseñausuario:
                print("***Acceso Concedido***")
                while True:
                    print("""Hola por favor seleccione una opcion
                      1.Registrar Material
                      2.Verificar Inventario
                      3. salir""")
                    indice=int(input("ingrese opcion: "))
                    if indice==1:
                        materialnuevo=input("Nombre de la Madera ")
                        materialnuevo.lower().strip()
                        cantidadnuevo=input("Ingrese cantidad en M2 ")
                        cantidadnuevo.lower().strip()
                        print("Material Registrado")
                    elif indice==2:
                        print(materialnuevo)
                        print(cantidadnuevo)
                    elif indice==3:
                        break
            else: 
                
                print("usuario o contraseña invalida por favor intente de nuevo: ")
    elif opcion==2:
            nombre=input("registre su nombre de usuario: ")
            nombre.lower()
            contraseña=input("Registre su contraseña: ")
            contraseña.lower()
            print("**** Registrado Exitosamente ****")
            break
    else:
            break