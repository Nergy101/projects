
from time import *
from socket import *
import random, string
import threading
import os

localstatus = '0000'
name = input('name?')
base = name + ":" + "CLIENT" + ":"
def receive():


    host = ""
    port = 13000
    buf = 1024
    addr = ((host, port))
    UDPSock = socket(AF_INET, SOCK_DGRAM)
    UDPSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    UDPSock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    UDPSock.bind(addr)

    while True:
        (data, addr) = UDPSock.recvfrom(buf)
        data = str(data)
        addr = str(addr)
        #--commands--#
        if data[-5:-1] == '1000':
            print('DISC mode activated, sending reply.')
            global localstatus
            localstatus = '0001'




    UDPSock.close()

    os._exit(0)



dest = ('<broadcast>')
port = 13000
addr = (dest, port)
BSock = socket(AF_INET, SOCK_DGRAM)
BSock.setsockopt(SOL_SOCKET,SO_BROADCAST, 1)

#UDPSock.sendto(bytes(name, "utf-8"), addr)
def checking():
    while True:
        if localstatus == '0001':
            statuscode = '0001'
            msg = base + statuscode
            sending(msg)


def sending(msg):

    BSock.sendto(bytes(msg, "utf-8"), addr)
    print('done.')

    BSock.close()
    os._exit(0)


threads = []

t1 = threading.Thread(target=receive)

t2 = threading.Thread(target=checking)
t1.start()
sleep(2)
t2.start()



