intructores2557861={}
repetir="s"

while True:
    opcion=input("Lista Instructores Ficha 2557861\n1. Añadir/Modificar\n2. Buscar\n3. Borrar\n4. Listar\n5. Salir\n¿Qué Opción Desea Digitar?\n")
    
    if opcion=="1":
        Articulo=input("Ingrese el nombre del Instructor(a)\n").lower()
        if Articulo in intructores2557861:
            print("El Instructor(a) ya se encuentra registrado en la lista\n")
            for a,b in intructores2557861.items():
                print(a, " = ",b)  
            opcion= input("¿Que Deseá Hacer Con El Instructor(a)?\n1. Modificar la materia que dicta\n2. Modificar el telefono del instructor\n3. Terminar\n")
            while repetir=="s" or repetir=="S":
                
                if opcion=="1":
                    Materia= input("Deme la materia actual que dicta el Instructor(a):\n")
                    intructores2557861[Articulo]['materia']=Materia
                    print("Materia Cambiada Exitosamente")
                    repetir="n"
                elif opcion=="2":
                    Telefono=input("Deme el telefono actual del Instructor(a)\n")
                    intructores2557861[Articulo]['telefono']=Telefono
                    print("Telefono Cambiado Exitosamente")
  
                    repetir="n"
                elif opcion=="3":
                    print("Usted Decidío Salir De Esta Opción, Adiós")
                    repetir="n"      
                else:
                    print("Opción no valida")         
        else:
            intructores2557861[Articulo]={}
            
            Materia=input("Deme La Materia que dicta el Instructor(a):\n")
            intructores2557861[Articulo]['materia']=Materia
            
            Telefono=input("Deme el Telefono Del Instructor(a)\n")
            intructores2557861[Articulo]['telefono']=Telefono
            
            print("Instructor(a) Añadido Exitosamente A La Lista 2557861\n")
    elif opcion=="2":
        if len(intructores2557861)==0:
            print("No hay nada que buscar, la lista esta vacía\n")
        else:
            texto=input("Ingrese el Instructor(a) a buscar\n")
            for instructor,datos in intructores2557861.items():
                if Articulo.startswith(texto):
                    print(f"Este Instructor(a) lleva por nombre {instructor} y tiene los siguientes datos : {datos}\n")
                else:
                    print("El Instructor(a) no se encuentra en la lista\n")
    elif opcion=="3":
        if len(intructores2557861)==0:
            print("No hay nada que borrar, la lista esta vacía\n")
        else:
            borrarSelección=input("Digite el nombre del Instructor(a) Para Comprobar Si Se Encuentar En La Lista\n").lower()  
            if borrarSelección in intructores2557861: 
                opcionInstructor=input(f"Seleccione \n1. Si desea borrar el instructor(a) de la lista\n2. Si desea Borrar Atributos del Instructor(a) {borrarSelección}\n")
                if opcionInstructor=="1":
                    intructores2557861.pop(borrarSelección)
                    print("Usted borró el Instructor(a) ",borrarSelección,"\nLa lista quedó de la siguiente manera:\n")
                    if len(intructores2557861)==0:
                        print("No hay Lista que mostrar\n")
                    else:
                     for a,b in intructores2557861.items():
                            print(a, " = ",b)  
                elif opcionInstructor=="2":
                   KeyBorrada=input(f"Digite el atributo que desea Borrar Del Instructor(a), Si es Materia o Telefono escribalo en este espacio \n").lower()
                   if KeyBorrada in intructores2557861[Articulo]:
                        del intructores2557861[borrarSelección][KeyBorrada]
                        print(f"Usted borró el Atributo {KeyBorrada} Del Instructor",borrarSelección,"\nLa lista quedó de la siguiente manera:\n")
                        if len(intructores2557861)==0:
                            print("No hay Lista que mostrar")
                        else:
                            for a,b in intructores2557861.items():
                                print(a, " = ",b) 
                   else:
                        print("El atributo no se encuentra")
                else:
                    print("Opción no valida")
            else:
                print("el Instructor(a) no se encuentra en la lista\n")
    elif opcion=="4":
        if len(intructores2557861)==0:
            print("No hay Lista")
        else:
            for a,b in intructores2557861.items():
                print(a, " = ",b)
    elif opcion=="5":
        print("Hasta Luego")
        break
    else:
        print("NO valido")