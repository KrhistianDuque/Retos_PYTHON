listaInstructores=[]
repetirarticulo="s"
repetir="s"

while repetir=="s" or repetir=="S":
    selección=input("Digite que opción desea hacer: \n1. Agregar el nombre de un instructor a la lista\n2. Listar los instructores que están en la lista\n3. Modificar un elemento de la lista (seleccionado por el usuario)\n4. Borrar un elemento de la lista (seleccionado por el usuario)\n5. Buscar un elemento particular de la lista por su nombre sin importar las mayúsculas o minúsculas.\n6. Ordenar la lista de instructores de la A-Z\nO cualquier otra letra para Salir\n")
    if selección=="1":
        repetirarticulo="s"
        while repetirarticulo=="s" or repetirarticulo=="S":
         listaInstructores.append(input("Digite el nombre del instructor que desea agregar a la lista de instructores\n"))
         repetirarticulo=input("digite s si desea agregar mas instructores a la lista o n para salir\n")
    elif selección=="2":
        if len(listaInstructores)==0:
            print("La lista esta vacía\n")
        else:
            for i,e in enumerate(listaInstructores):
                print(i,": Instructor",e,"\n")
    elif selección=="3":
        if len(listaInstructores)==0:
            print("No hay nada que modificar, la lista esta vacía\n")
        else:
            for i,e in enumerate(listaInstructores):
                print(i,": Instructor(a)",e,"\n")
            modificar=int(input("Ingrese el numero del instructor que desea modificar\n"))
            ValorNuevo=input("Ingrese el nuevo instructor que desea agregar\n")
            listaInstructores[modificar]=ValorNuevo
            print("Cambio Con Exito!!, La lista quedo de la siguiente manera:\n")
            for i,e in enumerate(listaInstructores):
                print(i,": Instructor(a)",e,"\n")  
    elif selección=="4":
        if len(listaInstructores)==0:
            print("No hay nada que borrar, la lista esta vacía\n")
        else:
            for i,e in enumerate(listaInstructores):
                print(i,": Instructor(a)",e,"\n")
            borrarSelección=input("Digite el nombre del instructor que desea borrar de la lista\n").lower()
            listaInstructores.remove(borrarSelección)
            print("Usted borró el instructor",borrarSelección,"\n la lista quedó de la siguiente manera\n")
            for i,e in enumerate(listaInstructores):
                print(i,": Instructor(a)",e,"\n")
    elif selección=="5": 
        if len(listaInstructores)==0:
            print("No hay nada que consultar, la lista esta vacía\n")
        else: 
            buscar=input("Ingrese el nombre del instructor que desea buscar para mirar si esta en la lista\n").lower()
            verificar=False
            for instructor in listaInstructores :
                if instructor==buscar.lower():
                    verificar=True
                    print("El instructor se encuentra en la lista\n")
            if not verificar:
                print("El instructor no se encuentra en la lista\n")
            
    elif selección=="6":
        if len(listaInstructores)==0:
            print("No hay nada que ordenar, la lista esta vacía")
        else:
            listaInstructores.sort()
            print("Usted acaba de listar los articulos de forma ascendente\n")
            for i,e in enumerate(listaInstructores):
                print(e)
    else:
        repetir=("Usted seleccionó la opción de salir, digite s para seguir o cualquier tecla para salir\n").lower()