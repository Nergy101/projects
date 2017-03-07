
#---it's a chat application! complete with names!
#---to be used in the room-screem project, this program allows for 2 way text communication between users.

#-montarion-3/3/2017-it now does broadcasting, which has a limit of 32 users at a time.(per port i think, cant test.)
from time import *
from socket import *
import random, string
import threading
import os


s = string.ascii_lowercase + string.digits
ownuserid = ''.join(random.sample(s,4))


def receive():


    host = ""
    port = 13000
    buf = 1024
    addr = (host, port)
    UDPSock = socket(AF_INET, SOCK_DGRAM)
    UDPSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    UDPSock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    UDPSock.bind(addr)


    print("Chatroom is open.")
    userlist = {}
    name = 'Anonymous'
    userid = '0000'


    while True:
        (data, addr) = UDPSock.recvfrom(buf)
        data = str(data)
        logon = 0


        userid = data[2:6]
        if userid == ownuserid:
            logon = 3

        if logon == 3 and data[6:-1] == 'EXIT':
            print("You have left the chat.")
            break
        if data[6:11] == 'name:':
            name = data[12:-1]
            data = data[6:]

            userlist.update({userid:name})
            logon = 1
        if data[6:-1] == 'EXIT':
            logon = 2

        if logon == 0:
            try:
                print(userlist[userid] + ":",data[6:-1])
            except:
                print(name + ":",data[6:-1])

        if logon == 1:
            try:
                print(userlist[userid],"has joined the chat")
            except:
                print(name,"has joined the chat")

        if logon == 2:
            try:
                print(userlist[userid],"has left the chat")
            except:
                print(name,"has left the chat")
        if logon == 3:
            pass

    UDPSock.close()

    os._exit(0)

name = input("what's your name? ")

dest = ('<broadcast>')
port = 13000
addr = (dest, port)
BSock = socket(AF_INET, SOCK_DGRAM)
BSock.setsockopt(SOL_SOCKET,SO_BROADCAST, 1)

#UDPSock.sendto(bytes(name, "utf-8"), addr)
#---creates id---#

leavemsg = ownuserid + "EXIT"

name = ownuserid + "name: " + name
BSock.sendto(bytes(name, "utf-8"), addr)
def sending():

    while True:
        try:
            data = input("type: ")
            #---commands---#
            if data == '!exit':
                BSock.sendto(bytes(leavemsg, "utf-8"), addr)
                break

            data = ownuserid + data


            BSock.sendto(bytes(data, "utf-8"), addr)
        except KeyboardInterrupt:
            BSock.sendto(bytes(leavemsg, "utf-8"), addr)
            break
    BSock.close()
    os._exit(0)


threads = []

t1 = threading.Thread(target=receive)

t2 = threading.Thread(target=sending)
t1.start()
sleep(.2)
t2.start()
