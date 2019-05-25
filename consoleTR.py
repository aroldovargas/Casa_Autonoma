import socket
from datetime import datetime
 
def leArq():
    arq = open("resposta_cliente_termometro.txt","r")
    txt = arq.read()
    txt = txt.split()
    arq.close()

    return txt

#Função do cliente Termmometro = TR
def clienteTR(lista):

    HOST = socket.gethostbyname(socket.gethostname())       # Endereco IP do Servidor
    PORT = 5000                                             # Porta que o Servidor esta
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest = (HOST, PORT)
    tcp.connect(dest)


    #Indica que o equipamento é do tipo TERMOMETRO e recebe uma id para esse equipamento
    tcp.send(("TERMOMETRO").encode())
    id_equipamento,hora,msg = (tcp.recv(1024)).decode().split(",")
    temperatura = input("Indique a temperatura em graus Celsius do termometro " + id_equipamento +": ")
    tcp.send((id_equipamento+","+(datetime.now().strftime("%d/%m/%Y %H:%M"))+","+temperatura).encode())
    print("ID: "+id_equipamento+"     HORA: "+hora+"     MSG: "+msg)


    hora_antiga = int(datetime.now().strftime("%M"))
    while True:


    tcp.close()



lista = leArq()
clienteTR(lista)