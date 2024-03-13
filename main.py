bandas=[]


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
        pass
