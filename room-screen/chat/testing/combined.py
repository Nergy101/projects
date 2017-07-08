<<<<<<< HEAD
#---it's a chat application! complete with names!
#---to be used in the room-screem project, this program allows for 2 way text communication between 2 users.
#---(more might be possible, testing needed)
from time import *
from socket import *
import random, string
import threading



def receive():


    host = ""
    port = 13001
    buf = 1024
    addr = (host, port)
    UDPSock = socket(AF_INET, SOCK_DGRAM)
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
        if data[6:11] == 'name:':
            name = data[12:-1]
            data = data[6:]

            userlist.update({userid:name})
            logon = 1
        if data[6:-1] == 'Error 404':
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

    receive.close()

    os._exit(0)

name = input("what's your name? ")


host = "192.168.178.34" # set to IP address of target computer
port = 13000
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)

#UDPSock.sendto(bytes(name, "utf-8"), addr)
#---creates id---#
s = string.ascii_lowercase + string.digits
userid = ''.join(random.sample(s,4))
leavemsg = userid + "Error 404"

name = userid + "name: " + name
UDPSock.sendto(bytes(name, "utf-8"), addr)
def sending():

    while True:
        try:
            data = input("type: ")

            data = userid + data

            UDPSock.sendto(bytes(data, "utf-8"), addr)
        except KeyboardInterrupt:
            UDPSock.sendto(bytes(leavemsg, "utf-8"), addr)
            break
    UDPSock.close()
    os._exit(0)


threads = []

t1 = threading.Thread(target=receive)

t2 = threading.Thread(target=sending)
t1.start()
sleep(.2)
t2.start()
=======
#---it's a chat application! complete with names!
#---to be used in the room-screem project, this program allows for 2 way text communication between 2 users.
#---(more might be possible, testing needed)
from time import *
from socket import *
import random, string
import threading



def receive():


    host = ""
    port = 13001
    buf = 1024
    addr = (host, port)
    UDPSock = socket(AF_INET, SOCK_DGRAM)
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
        if data[6:11] == 'name:':
            name = data[12:-1]
            data = data[6:]

            userlist.update({userid:name})
            logon = 1
        if data[6:-1] == 'Error 404':
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

    receive.close()

    os._exit(0)

name = input("what's your name? ")


host = "192.168.178.34" # set to IP address of target computer
port = 13000
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)

#UDPSock.sendto(bytes(name, "utf-8"), addr)
#---creates id---#
s = string.ascii_lowercase + string.digits
userid = ''.join(random.sample(s,4))
leavemsg = userid + "Error 404"

name = userid + "name: " + name
UDPSock.sendto(bytes(name, "utf-8"), addr)
def sending():

    while True:
        try:
            data = input("type: ")

            data = userid + data

            UDPSock.sendto(bytes(data, "utf-8"), addr)
        except KeyboardInterrupt:
            UDPSock.sendto(bytes(leavemsg, "utf-8"), addr)
            break
    UDPSock.close()
    os._exit(0)


threads = []

t1 = threading.Thread(target=receive)

t2 = threading.Thread(target=sending)
t1.start()
sleep(.2)
t2.start()
>>>>>>> ba00ef1077f809dd7ebea03a214d112bf8826bb6
