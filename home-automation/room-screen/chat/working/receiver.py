# Save as server.py 
# Message Receiver
import os
from socket import *
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

UDPSock.close()
os._exit(0)
