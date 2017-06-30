
from time import *
from socket import *
import random, string
import threading
import os
global localstatus, statuscode
localstatus = '0000'
statuscode = '0000'
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
        print('while loop, waiting for data')
        (data, addr) = UDPSock.recvfrom(buf)
        data = str(data)
        addr = str(addr)
        print(data)

        #--commands--#
        if statuscode == '9999':
            break
        if data[-5:-1] == '1000':
            print('DISC mode activated, sending reply.')
            localstatus = '0001'
            print(localstatus)

        print('waiting for next')


def checking():
    print('checking started')
    while True:
        if localstatus == '0001' and statuscode != '9999':
            statuscode = '0001'
            msg = base + statuscode
            sending(msg)


def sending(msg):
    dest = ('<broadcast>')
    port = 13000
    addr = (dest, port)
    BSock = socket(AF_INET, SOCK_DGRAM)
    BSock.setsockopt(SOL_SOCKET,SO_BROADCAST, 1)
    BSock.sendto(bytes(msg, "utf-8"), addr)
    statuscode = '9999'
    print('done, status code is,' + statuscode)

    BSock.close()
    #os._exit(0)


threads = []

t1 = threading.Thread(target=receive)

t2 = threading.Thread(target=checking)
t2.start()
sleep(2)
t1.start()



