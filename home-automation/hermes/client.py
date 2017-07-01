from time import *
from socket import *
import random, string
import threading
import os
global localstatus, statuscode, addr
localstatus = '0000'
statuscode = '0000'
addr = '0000'
#name = input('name?')
name = 'hawk'
base = name + ":" + "CLIENT" + ":"
def receive():
    print('recieving')

    host = ""
    port = 13000
    buf = 1024
    addr = ((host, port))
    UDPSock = socket(AF_INET, SOCK_DGRAM)
    UDPSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    UDPSock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    UDPSock.bind(addr)

    while True:
        print('discovery mode activated, waiting for data')
        (data, addr) = UDPSock.recvfrom(buf)
        data = str(data)
        addr = str(addr)
        print(data)

        #--commands--#
        if statuscode == '9999':
            break
        if data[-5:-1] == '1000':
            print('probe recieved, sending reply.')
            localstatus = '0001'
            print(localstatus)
            print('server ip adress is :', addr)
            msg = base + localstatus
            sending(msg)

            UDPSock.close()
            break
        sleep(3)

def sending(msg):
    dest = ('<broadcast>')
    port = 13000
    addr = (dest, port)
    BSock = socket(AF_INET, SOCK_DGRAM)
    BSock.setsockopt(SOL_SOCKET,SO_BROADCAST, 1)
    while True:
        BSock.sendto(bytes(msg, "utf-8"), addr)
        print('sending reply')
        sleep(2)
    statuscode = '9999'
    print('done, status code is' + statuscode)

    BSock.close()
    #os._exit(0)


threads = []

t1 = threading.Thread(target=receive)

#t2 = threading.Thread(target=checking)
#t2.start()
sleep(2)
t1.start()

