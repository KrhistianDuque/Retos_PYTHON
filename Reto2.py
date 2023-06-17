Fruver={}
repetirarticulo="s"

while True:
    opcion=input("Fruver Supermercados Noé\n1. Añadir/Modificar\n2. Buscar\n3. Borrar\n4. Listar\n5. Salir\n¿Qué Opción Desea Digitar?\n")
    
    if opcion=="1":
        Articulo=input("Ingrese el nombre del articulo\n").lower()
        if Articulo in Fruver:
            print("El articulo ya se encuentra registrado")
            opcion= input("¿Que Deseá Hacer Con El Articulo?\n1. Modificar el precio del articulo\n2. Modificar el tipo de articulo\n3. Terminar\n").lower()
            while repetirarticulo=="s" or repetirarticulo=="S":
                
                if opcion=="1":
                    precio = int(input("Deme el nuevo precio del articulo:\n"))
                    Fruver[Articulo]['precio']=precio
                    repetirarticulo="n"
                if opcion=="2":
                    tipo=int(input("Selecciona el nuevo tipo del artículo\n1. Vegetal\n2. Fruta\n"))
                    if tipo==1:
                        variedad="Vegetal"
                    elif tipo==2:
                        variedad="Fruta"
                        repetirarticulo="n"
                    else:
                        print("Opción No Valida")
                    Fruver[Articulo]['tipo']=variedad
                elif opcion=="3":
                    print("Adiós")
                    repetirarticulo="n"               
        else:
            Fruver[Articulo]={}
            precio=int(input("Dame precio del artículo:\n"))
            Fruver[Articulo]['precio']=precio
            tipo=int(input("Seleccione el tipo del articulo\n1. Vegetal\n2. Fruta\n"))
            if tipo==1:
                variedad="Vegetal"
            elif tipo==2:
                variedad="Fruta"
            Fruver[Articulo]['tipo']=variedad
            print("Articulo Añadido Exitosamente\n")
    elif opcion=="2":
        if len(Fruver)==0:
            print("No hay nada que buscar, la lista esta vacía\n")
        else:
            texto=input("Ingrese el articulo a buscar\n")
            for fruta,datos in Fruver.items():
                print("Se encontraron los siguientes resultados\n")
                if Articulo.startswith(texto):
                    print(f"Este articulo {Fruver[Articulo]['tipo']} lleva por nombre {Articulo} y tiene un costo de {Fruver[Articulo]['precio']}\n")
                else:
                    print("La fruta no se encuentra en la lista\n")
    elif opcion=="3":
        if len(Fruver)==0:
            print("No hay nada que borrar, la lista esta vacía\n")
        else:
            for a,b in Fruver.items():
                print(a, " = ",b)
            borrarSelección=input("Digite el nombre del articulo que desea borrar de la lista\n").lower()  
            if borrarSelección in Fruver:    
                Fruver.pop(borrarSelección)
                print("Usted borró el articulo ",borrarSelección,"\nLa lista quedó de la siguiente manera:\n")
                if len(Fruver)==0:
                    print("No hay Lista que mostrar\n")
                else:
                    for a,b in Fruver.items():
                        print(a, " = ",b)   
            else:
                print("el articulo no se encuentra en la lista\n")
    elif opcion=="4":
        for a,b in Fruver.items():
          print(a, " = ",b)
    elif opcion=="5":
        print("Hasta Luego")
        break
    else:
        print("NO valido")