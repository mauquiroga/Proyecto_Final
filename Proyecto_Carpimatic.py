# aqui guardamos nombre de usuario y contraseña
nombre = "mau"
contraseña = "123"
# aca se almacenaran los datos de las maderas
lista_maderas = []
lista_cantidades = []
while True:
    print("""
    Bienvenido al Sistema
    ***Carpimatic***
    Por favor, selecciona una opcion:
    1. Iniciar sesion
    2. Registrarse
    3. Salir""")
# eta es la parte donde seleccionamos en el menu que deseamos hacer    
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        nombreusuario = input("Ingrese su Nombre: ").lower().strip()
        contraseñausuario = input("Ingrese una Contraseña: ").lower().strip()
        
        if nombre == nombreusuario and contraseña == contraseñausuario:
            print("\n*** Acceso Concedido ***")
            
            while True:
                print("""
                Hola, por favor seleccione una opcion:
                1. Registrar Material
                2. Verificar Inventario
                3. Cerrar sesión""")
                
                indice = int(input("Ingrese opcion: "))
                    
                if indice == 1:
                    materialnuevo = input("Nombre de la Madera: ").lower().strip()
                    cantidad_input = input("Ingrese cantidad en M2: ").strip()
                    
# aca hemos utilizado el replace y float como se solicito
                    cantidad_limpia = cantidad_input.replace(",", ".")
                    cantidad_float = float(cantidad_limpia)
# aca Buscamos si la madera ya existe en nuestra lista se nescito ayuda de ia
                    encontrado = False
                    for i in range(len(lista_maderas)):
                        if lista_maderas[i] == materialnuevo:
                            # Si ya existe, aplicamos la SUMA en su misma posición
                            lista_cantidades[i] = lista_cantidades[i] + cantidad_float
                            encontrado = True
                            print("Material existente. ¡Cantidad sumada!")
                    
                    # Si terminamos el ciclo for y no existía, lo agregamos al final ia
                    if encontrado == False:
                        lista_maderas.append(materialnuevo)
                        lista_cantidades.append(cantidad_float)
                        print("Nuevo material registrado con éxito.")
                    
                elif indice == 2:
                    print("\n--- INVENTARIO EN BODEGA ---")
                    # Si la lista está vacía ia
                    if len(lista_maderas) == 0:
                        print("La bodega está vacía.")
                    else:
                        # Mostramos los materiales uno por uno con un ciclo básico ia
                        for i in range(len(lista_maderas)):
                            print("Madera: " + lista_maderas[i] + " | Cantidad: " + str(lista_cantidades[i]) + " m2")
                            
                elif indice == 3:
                    print("Cerrando sesión...")
                    break
                    
        else: 
            print("Usuario o contraseña invalida. Intente de nuevo.")
#aca hemor retornado a nuestro codigo original he nota que la ia realizo alguna modificacion            
    elif opcion == 2:
        nombre = input("Registre su nombre de usuario: ").lower().strip()
        contraseña = input("Registre su contraseña: ").lower().strip()
        print("\n**** Registrado Exitosamente ****")
        
    elif opcion == 3:
        print("¡Adiós!")
        break