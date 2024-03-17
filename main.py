""" """ """ bandas=[]


#construyendo la interfaz
print("***ALTA VOZ ES TU VOZ***")
print("************************")

opcion=100
while(opcion!=5):
    print("1. Registrar Bandas")
    print("2. Buscar Informacion de una Banda")
    print("3. Agenda del evento")
    print("4. Modificar una banda")
    print("5. SALIR")
    opcion=int(input("Digita una opcion: "))

    if opcion==1:
        banda={}
        #crear daos del diccionario
        banda["id"]=int(input("Digita l id: ")) 
        banda["nombre"]=input("Nombre de la banda: ")
        banda["genero"]=input("Genero: ")
        banda["clasificacion"]=input("Clasificacion: ")
        banda["tiempo"]=int(input("tiempo: "))
        banda["costo"]=int(input("Costo: $"))
        
        #agregar diccionario a un alista
        bandas.append(banda)

        
    elif opcion==2:

        bandaBuscada=input("digita el nombre de la bandaque estas buscando")
        for bandAuxiliar in bandas:
            if bandAuxiliar["nombre"]==bandaBuscada:
                #como se encontro muestro los datos de bandaAuxiliar
                print(f"id: {bandAuxiliar["id"]} --- nombre: {bandAuxiliar["nombre"]}")
            else:
                print("sigue buscando")    


                            
    elif opcion==3:
        print(bandas)
    elif opcion==4:
        pass
    elif opcion==5:
        pass
    else:
        pass ""

********************************************************************************************************************************************************************************** 

                                                                  VALIDAR QUE LA ENTRADA SEA SOLO NUMERICO """

""" bandas = []

# Construyendo la interfaz
print("***ALTA VOZ ES TU VOZ***")
print("************************")

opcion = 100
while opcion != 5:
    print("1. Registrar Bandas")
    print("2. Buscar Informacion de una Banda")
    print("3. Agenda del evento")
    print("4. Modificar una banda")
    print("5. SALIR")
    opcion = input("Digita una opcion: ")

    while not opcion.isdigit():  # Validación para asegurar que la entrada sea numérica
        print("Por favor, ingresa un valor numérico.")
        opcion = input("Digita una opcion: ")

    opcion = int(opcion)

    if opcion == 1:
        banda = {}
        # Crear datos del diccionario
        banda["id"] = int(input("Digita el id: "))
        banda["nombre"] = input("Nombre de la banda: ")
        banda["genero"] = input("Genero: ")
        banda["clasificacion"] = input("Clasificacion: ")
        banda["tiempo"] = int(input("Tiempo: "))
        banda["costo"] = int(input("Costo: $"))

        # Agregar diccionario a una lista
        bandas.append(banda)

    elif opcion == 2:
        bandaBuscada = input("Digita el nombre de la banda que estás buscando: ")
        for bandAuxiliar in bandas:
            if bandAuxiliar["nombre"] == bandaBuscada:
                # Como se encontró, muestro los datos de bandAuxiliar
                print(f"id: {bandAuxiliar['id']} --- nombre: {bandAuxiliar['nombre']}")
            else:
                print("Sigue buscando")

    elif opcion == 3:
        print(bandas)
    elif opcion == 4:
        pass
    elif opcion == 5:
        pass
    else:
        pass

    ********************************************************************************************************************************************************************************** 

                                                                  DATO TIEMPO Y CONTROLARLO "" """

""" bandas = []

# Construyendo la interfaz
print("***ALTA VOZ ES TU VOZ***")
print("************************")

opcion = 100
while opcion != 5:
    print("1. Registrar Bandas")
    print("2. Buscar Informacion de una Banda")
    print("3. Agenda del evento")
    print("4. Modificar una banda")
    print("5. SALIR")
    opcion = int(input("Digita una opcion: "))

    if opcion == 1:
        banda = {}
        # Crear datos del diccionario
        banda["id"] = int(input("Digita el id: "))
        banda["nombre"] = input("Nombre de la banda: ")
        banda["genero"] = input("Genero: ")
        banda["clasificacion"] = input("Clasificacion: ")
        banda["tiempo"] = int(input("Tiempo (en minutos): "))
        banda["costo"] = int(input("Costo: $"))

        # Agregar diccionario a una lista
        bandas.append(banda)

    elif opcion == 2:
        bandaBuscada = input("Digita el nombre de la banda que estás buscando: ")
        for bandAuxiliar in bandas:
            if bandAuxiliar["nombre"] == bandaBuscada:
                # Como se encontró, muestro los datos de bandAuxiliar
                print(f"id: {bandAuxiliar['id']} --- nombre: {bandAuxiliar['nombre']}")
            else:
                print("Sigue buscando")

    elif opcion == 3:
        print(bandas)
    elif opcion == 4:
        pass
    elif opcion == 5:
        pass
    else:
        pass

    ********************************************************************************************************************************************************************************** 

                                                                  SACAR UN ELEMENTO DE UNA LISTA "" """ ""

""" bandas = []

# Construyendo la interfaz
print("***ALTA VOZ ES TU VOZ***")
print("************************")

opcion = 100
while opcion != 5:
    print("1. Registrar Bandas")
    print("2. Buscar Informacion de una Banda")
    print("3. Agenda del evento")
    print("4. Modificar una banda")
    print("5. SALIR")
    opcion = int(input("Digita una opcion: "))

    if opcion == 1:
        banda = {}
        # Crear datos del diccionario
        banda["id"] = int(input("Digita el id: "))
        banda["nombre"] = input("Nombre de la banda: ")
        banda["genero"] = input("Genero: ")
        banda["clasificacion"] = input("Clasificacion: ")
        banda["tiempo"] = int(input("Tiempo (en minutos): "))
        banda["costo"] = int(input("Costo: $"))

        # Agregar diccionario a una lista
        bandas.append(banda)

    elif opcion == 2:
        bandaBuscada = input("Digita el nombre de la banda que estás buscando: ")
        for bandAuxiliar in bandas:
            if bandAuxiliar["nombre"] == bandaBuscada:
                # Como se encontró, muestro los datos de bandAuxiliar
                print(f"id: {bandAuxiliar['id']} --- nombre: {bandAuxiliar['nombre']}")
            else:
                print("Sigue buscando")

    elif opcion == 3:
        print(bandas)
        
    elif opcion == 4:
        if bandas:  # Verificar si la lista no está vacía
            indice_eliminar = int(input("Ingrese el índice del elemento que desea eliminar: "))
            if indice_eliminar >= 0 and indice_eliminar < len(bandas):
                elemento_eliminado = bandas.pop(indice_eliminar)
                print(f"Elemento eliminado: {elemento_eliminado}")
            else:
                print("Índice fuera de rango. Inténtalo de nuevo.")
        else:
            print("La lista de bandas está vacía.")
            
    elif opcion == 5:
        pass
    else:
        pass """

"""      ********************************************************************************************************************************************************************************** 

                                                                  ID AUTOMATICO "" """ ""

""" bandas = []
next_id = 1

def generar_id():
    global next_id
    new_id = next_id
    next_id += 1
    return new_id

# Función para registrar una banda
def registrar_banda():
    banda = {}
    banda["id"] = generar_id()
    banda["nombre"] = input("Nombre de la banda: ")
    banda["genero"] = input("Género: ")
    banda["clasificacion"] = input("Clasificación: ")
    banda["tiempo"] = int(input("Tiempo (en minutos): "))
    banda["costo"] = int(input("Costo: $"))
    
    bandas.append(banda)
    print("Banda registrada con éxito.")

# Construyendo la interfaz
print("***ALTA VOZ ES TU VOZ***")
print("************************")

opcion = 100
while opcion != 5:
    print("1. Registrar Bandas")
    print("2. Buscar Informacion de una Banda")
    print("3. Agenda del evento")
    print("4. Modificar una banda")
    print("5. SALIR")
    opcion = int(input("Digita una opcion: "))

    if opcion == 1:
        registrar_banda()

    elif opcion == 2:
        bandaBuscada = input("Digita el nombre de la banda que estás buscando: ")
        for bandAuxiliar in bandas:
            if bandAuxiliar["nombre"] == bandaBuscada:
                print(f"id: {bandAuxiliar['id']} --- nombre: {bandAuxiliar['nombre']}")
            else:
                print("Sigue buscando")

    elif opcion == 3:
        print(bandas)
        
    elif opcion == 4:
        pass

    elif opcion == 5:
        pass

    else:
        pass
 """

"""      ********************************************************************************************************************************************************************************** 

                                                                  CLASIFICACION DENTRO DEL RANGO "" """ ""

""" bandas = []

# Construyendo la interfaz
print("***ALTA VOZ ES TU VOZ***")
print("************************")

opcion = 100
while opcion != 5:
    print("1. Registrar Bandas")
    print("2. Buscar Informacion de una Banda")
    print("3. Agenda del evento")
    print("4. Modificar una banda")
    print("5. SALIR")
    opcion = int(input("Digita una opcion: "))

    if opcion == 1:
        banda = {}
        # Crear datos del diccionario
        banda["id"] = int(input("Digita el id: "))
        banda["nombre"] = input("Nombre de la banda: ")
        banda["genero"] = input("Genero: ")
        
        # Validar la clasificación dentro de un rango específico
        while True:
            clasificacion = input("Clasificación (1-5): ")
            if clasificacion.isdigit() and 1 <= int(clasificacion) <= 5:
                banda["clasificacion"] = int(clasificacion)
                break
            else:
                print("Por favor, ingresa un valor numérico entre 1 y 5 para la clasificación.")

        banda["tiempo"] = int(input("Tiempo: "))
        banda["costo"] = int(input("Costo: $"))

        # Agregar diccionario a una lista
        bandas.append(banda)

    elif opcion == 2:
        bandaBuscada = input("Digita el nombre de la banda que estás buscando: ")
        for bandAuxiliar in bandas:
            if bandAuxiliar["nombre"] == bandaBuscada:
                print(f"id: {bandAuxiliar['id']} --- nombre: {bandAuxiliar['nombre']}")
            else:
                print("Sigue buscando")

    elif opcion == 3:
        print(bandas)
        
    elif opcion == 4:
        pass

    elif opcion == 5:
        pass

    else:
        pass

    ********************************************************************************************************************************************************************************** 

                                                                 CODIGO FULL "" """ "" ""

bandas = []
next_id = 1

def generar_id():
    global next_id
    new_id = next_id
    next_id += 1
    return new_id

# Función para registrar una banda
def registrar_banda():
    banda = {}
    banda["id"] = generar_id()
    banda["nombre"] = input("Nombre de la banda: ")
    banda["genero"] = input("Género: ")
    
    # Validar la clasificación dentro de un rango específico
    while True:
        clasificacion = input("Clasificación (1-5): ")
        if clasificacion.isdigit() and 1 <= int(clasificacion) <= 5:
            banda["clasificacion"] = int(clasificacion)
            break
        else:
            print("Por favor, ingresa un valor numérico entre 1 y 5 para la clasificación.")

    banda["tiempo"] = int(input("Tiempo (en minutos): "))
    banda["costo"] = int(input("Costo: $")
    
    bandas.append(banda)
    print("Banda registrada con éxito.")

# Construyendo la interfaz
print("***ALTA VOZ ES TU VOZ***")
print("************************")

opcion = 100
while opcion != 5:
    print("1. Registrar Bandas")
    print("2. Buscar Informacion de una Banda")
    print("3. Agenda del evento")
    print("4. Modificar una banda")
    print("5. SALIR")
    opcion = int(input("Digita una opcion: "))

    if opcion == 1:
        registrar_banda()

    elif opcion == 2:
        bandaBuscada = input("Digita el nombre de la banda que estás buscando: ")
        for bandAuxiliar in bandas:
            if bandAuxiliar["nombre"] == bandaBuscada:
                print(f"id: {bandAuxiliar['id']} --- nombre: {bandAuxiliar['nombre']}")
            else:
                print("Sigue buscando")

    elif opcion == 3:
        print(bandas)
        
    elif opcion == 4:
        pass

    elif opcion == 5:
        pass

    else:
        pass





