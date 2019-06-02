def connect():
    import network
 
    ssid = "Inserir o nome da rede wifi"
    password =  "senha da rede"
 
    station = network.WLAN(network.STA_IF)
 
    if station.isconnected() == True:
        print("Já está conectado")
        return
 
    station.active(True)
    station.connect(ssid, password)
 
    while station.isconnected() == False:
        pass
 
    print("Conexão bem sucedida!")
    print(station.ifconfig())