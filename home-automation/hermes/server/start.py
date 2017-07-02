from components.server import probe
from components.tcpserver import receive


menu  = input('what do you want to do? ')
if menu == '1':
    receive().receive()

if menu == '2' or menu == 'probe':
    devices = input('how many nodes are there?')
    if eval(devices) > 0:
        probe().start(devices)
    else:
        print('sorry, that would break the system. ')
