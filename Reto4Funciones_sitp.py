repetir="s"

def subida():
    SubidaSITP=input("Se subio al sitp? \nsi\nno\n").lower()
    return SubidaSITP
def informacion():
    TipoTarjeta=input("Digite su tipo de tarjeta \nPersonalizada \nNormal\n").lower()
    SaldoTarjeta=int(input("Digite su saldo\n"))
    CantidadPasajes=int(input("Digite cuantos pasajes va a pagar\n"))
    
    return (TipoTarjeta,SaldoTarjeta,CantidadPasajes)
def ejecucion():
    SubidaSITP=subida()
    if SubidaSITP=="si":
        TipoTarjeta,SaldoTarjeta,CantidadPasajes=informacion()
        PrecioPasaje=2900
        CantidadPasajesAcumulable=PrecioPasaje*CantidadPasajes
        SaldoTarjeta=SaldoTarjeta-CantidadPasajesAcumulable
        if TipoTarjeta=="personalizada":
            if SaldoTarjeta<PrecioPasaje and CantidadPasajes==1:
                print("Recargué la tarjeta antes de la siguiente subida",SaldoTarjeta)
            elif SaldoTarjeta>=0:
                print("Gracias..., su saldo actual es",SaldoTarjeta)
            elif SaldoTarjeta<0:
                print("Saldo insuficiente...")
        elif TipoTarjeta=="normal":
            if SaldoTarjeta<0:
                print("Saldo Insuficiente, su saldo actual es ",SaldoTarjeta)
            elif SaldoTarjeta>=0:
                print("Gracias..., su saldo actual es",SaldoTarjeta)
        else:
            print("Ese no es un tipo de tarjeta existente")
    else:
        print("Vayase a pie")

while repetir=="s":
    print("Bienvenido al Transmilenio")
    ejecucion()
    repetir=input("Digite s para seguir o cualquier tecla para salir\n").lower()
