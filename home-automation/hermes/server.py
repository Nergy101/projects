from time import *
from socket import *
import random, string
import threading
import os


dictionary = {}
name = 'SERVER1'




#UDPSock.sendto(bytes(name, "utf-8"), addr)
#---creates id---#
probe = name + ":" + "SERVER" + ":" + "1000"                #1000 == DISCOVER
def sendprobe():

    dest = ('<broadcast>')
    port = 13000
    addr = (dest, port)
    BSock = socket(AF_INET, SOCK_DGRAM)
    BSock.setsockopt(SOL_SOCKET,SO_BROADCAST, 1)
    i = 0
    while i < 5:
        BSock.sendto(bytes(probe, "utf-8"), addr)
        print('PROBE SENT.')
        i = i + 1
        sleep(2)


def receive():
    print('receiving')
    while True:
        host = ""
        port = 13000
        buf = 1024
        addr = (host, port)
        UDPSock = socket(AF_INET, SOCK_DGRAM)
        UDPSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        UDPSock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
        UDPSock.bind(addr)




        print('waiting for replies')
        (data, addr) = UDPSock.recvfrom(buf)
        #kills sendprobe
        print('recieved the deets')
        data = str(data)
        addr = str(addr)
        if data[-5:-1] == '0001':                       #0001 == DISCack
            clientname = data[2:data.find(':')]
            print(clientname)
            print('setting up connection with ' + data[2:data.find(':')])
            dictionary.update({data[2:data.find(':')]: addr[2:addr.find(',')-1]}                                                                                                                                                             )
            print('done.')
            print(dictionary)
            UDPSock.close()
        print('next')
        sleep(3)
    #os._exit(0)


def sending():

    while True:
        BSock.sendto(bytes(data, "utf-8"), addr)

    BSock.close()
    os._exit(0)


threads = []

t1 = threading.Thread(target=receive)

t2 = threading.Thread(target=sendprobe())
t1.start()
sleep(2)
#t2.start()

