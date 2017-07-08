from components.server import probe
from components.tcpserver import receive
import os

if not os.path.exists('dictionary.txt'):
    menu = str(2)
else:
    menu  = input('what do you want to do? ')


if menu == '1':
    msg = 'received'
    receive().receive(msg)

if menu == '2' or menu == 'probe':
    devices = '1'             #changing this because the system can't handle more than 1 node at a time anyway
    probe().start(devices)
