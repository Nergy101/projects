from socket import *

host = "192.168.178.31"                 #will be dictionary
port = 13000                            #will be 13000 +1 for every new connection
addres = (host, port)
s = socket(AF_INET, SOCK_STREAM)
s.connect(addres)
print('connected to [' + host + ']')
data = s.recv(99999)
s.close()
print(str(data))

