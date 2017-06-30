from socket import *
from time import sleep


name = 'SERVER1'
dest = ('<broadcast>')
port = 13000
addr = (dest, port)
BSock = socket(AF_INET, SOCK_DGRAM)
BSock.setsockopt(SOL_SOCKET,SO_BROADCAST, 1)
dictionary = {}
lst = []
#UDPSock.sendto(bytes(name, "utf-8"), addr)
#---creates id---#
probe = name + ":" + "SERVER" + ":" + "1000"                #1000 == DISCOVER

BSock.sendto(bytes(probe, "utf-8"), addr)
print('PROBE SENT, SETTING UP SECURE CONNECTION')
sleep(2)

def receive():


    host = ""
    port = 13000
    buf = 1024
    addr = (host, port)
    UDPSock = socket(AF_INET, SOCK_DGRAM)
    UDPSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    UDPSock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    UDPSock.bind(addr)


    
    while True:
        (data, addr) = UDPSock.recvfrom(buf)
        data = str(data)
        addr = str(addr)
        if data[-5:-1] == '0001':                       #0001 == DISCack
            print('REPLY RECIEVED')
            print('setting up connection with ' + data[2:data.find(':')])
            dictionary.update({data[2:data.find(':')]: addr[2:addr.find(',')-1]})
            lst.append(data[2:data.find(':')])
            print(dictionary)
            print(lst)
            print(dictionary[lst[0]])
    UDPSock.close()


def connection(host, port):
    addres = (host, port)
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(addres)
    print('connected to [' + host + ']')
    data = s.recv(99999)
    s.close()
    print(str(data))


receive()

host = dictionary[lst[0]]                 #will be dictionary
port = 13000                            #will be 13000 +1 for every new connection



#connection(host, port)

