
#---it's a chat application! complete with names!
#---to be used in the room-screem project, this program allows for 2 way text communication between users.

#-montarion-3/3/2017-it now does broadcasting, which has a limit of 32 users at a time.(per port i think, cant test.)
from time import *
from socket import *
import random, string
import threading
import os


dictionary = {}



name = 'SERVER1'
dest = ('<broadcast>')
port = 13000
addr = (dest, port)
BSock = socket(AF_INET, SOCK_DGRAM)
BSock.setsockopt(SOL_SOCKET,SO_BROADCAST, 1)

#UDPSock.sendto(bytes(name, "utf-8"), addr)
#---creates id---#
probe = name + ":" + "SERVER" + ":" + "1000"                #1000 == DISCOVER


BSock.sendto(bytes(probe, "utf-8"), addr)
print('PROBE SENT, SETTING UP SECURE CONNECTION')


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
            
            print('setting up connection with ' + data[2:data.find(':')])
            dictionary.update({data[2:data.find(':')]: addr[2:addr.find(',')-1]})
            print('done.')
    UDPSock.close()

    os._exit(0)


def sending():

    while True:
        data = input("type: ")
        BSock.sendto(bytes(data, "utf-8"), addr)

    BSock.close()
    os._exit(0)


threads = []

t1 = threading.Thread(target=receive)

t2 = threading.Thread(target=sending)
t1.start()
sleep(.2)
#t2.start()


