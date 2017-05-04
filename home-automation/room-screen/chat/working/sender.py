# Save as client.py
# Message Sender
#it
import os
from socket import *
import random, string


host = "192.168.178.34"#, "192.168.178.30" # set to IP address of target computer
port = 13000
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
name = input("what's your name? ")

#UDPSock.sendto(bytes(name, "utf-8"), addr)
#---creates id---#
s = string.ascii_lowercase + string.digits
userid = ''.join(random.sample(s,4))
leavemsg = userid + "Error 404"
name = userid + "name: " + name
UDPSock.sendto(bytes(name, "utf-8"), addr)
while True:
    try:
        data = input("Enter message to send: ")
        data = userid + data

        UDPSock.sendto(bytes(data, "utf-8"), addr)
    except KeyboardInterrupt:
        UDPSock.sendto(bytes(leavemsg, "utf-8"), addr)
        break
UDPSock.close()
os._exit(0)
