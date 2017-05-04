<<<<<<< HEAD
from socket import *


dest = ('<broadcast>')
port = 13000
addr = (dest, port)
BSock = socket(AF_INET, SOCK_DGRAM)
BSock.setsockopt(SOL_SOCKET,SO_BROADCAST, 1)

BSock.sendto(bytes("second message", "utf-8"), addr)
=======
from socket import *


dest = ('<broadcast>')
port = 13000
addr = (dest, port)
BSock = socket(AF_INET, SOCK_DGRAM)
BSock.setsockopt(SOL_SOCKET,SO_BROADCAST, 1)

BSock.sendto(bytes("second message", "utf-8"), addr)
>>>>>>> ba00ef1077f809dd7ebea03a214d112bf8826bb6
