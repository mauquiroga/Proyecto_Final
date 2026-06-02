#aca tenemos guardado el nombre de usuario y contraseña principal
nombre="mau"
contraseña="123"

while True:
    #aca inicializamos el programa solicitando selecionar una opccion
    print("""Bienvenido al Sistema
            ***Carpimatic***
            Por favor, selecciona una opcion:
            1.Inciar sesion.
            2.Registrarse
            3.Salir""")
    opcion=int(input(" "))
   # en este punto podemos ingresar con el usuario principal o crear uno nuevo
    if opcion==1:
            nombreusuario=input("Ingrese su Nombre: ")
            nombreusuario.lower().strip()
            contraseñausuario=input("Ingrese una Contraseña: ")
            contraseñausuario.lower().strip()
            if nombre==nombreusuario and contraseña==contraseñausuario:
                print("***Acceso Concedido***")
                while True:
                    print("""Hola por favor seleccione una opcion
                      1.Registrar Material
                      2.Verificar Inventario
                      3. salir""")
# una vez ingresado al sistema podemor registrar nuevo material o verificar lo guardado 
                    indice=int(input("ingrese opcion: "))
                    if indice==1:
                        materialnuevo=input("Nombre de la Madera ")
                        materialnuevo.lower().strip()
                        cantidadnuevo=input("Ingrese cantidad en M2 ")
                        cantidadnuevo.lower().strip()
                        matbodega=materialnuevo
                        cantbodega=cantidadnuevo
                        print("Material Registrado")
                    elif indice==2:
                        print (" ingresado a bodega madera "+matbodega.replace("roble","mara"))
                        print ( cantbodega+" metros cuadrados a bodega.")
                    elif indice==3:
                        break
                    else:
                         break
            else: 
                
                print("usuario o contraseña invalida por favor intente de nuevo: ")
    elif opcion==2:
            nombre=input("registre su nombre de usuario: ")
            nombre.lower().strip()
            contraseña=input("Registre su contraseña: ")
            contraseña.lower().strip()
            print("**** Registrado Exitosamente ****")
            
    else:
            break