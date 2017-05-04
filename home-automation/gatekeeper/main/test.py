import os
from time import sleep
def devconnected():
    print('updating devices..')
    os.system('nmap -sn 192.168.178.1/24 > connected.txt')
    sleep(3)
    infile = open('connected.txt')
    convert = infile.readlines()
    infile.close()
    i = 4
    global connected
    connected = []
    while i < (len(convert) - 1):
        thing = convert[i]

        if thing[-17] == '(':
            connected.append(thing[-16:-2])
        else:
            connected.append(thing[-15:-1])
        i += 2
    return connected


def homefunc():
    global dictionary, adresses
    dictionary = {}

    adresses = []
    infile = open('devices.txt')
    text = infile.readlines()
    infile.close()
    i = 0
    while i < len(text):
        global name
        name = text[i][2:-20]

        adress = text[i][-17:-3]
        adresses.append(adress)
        dictionary.update({adress:name})
        adress = "'" + adress + "'"
        i += 1

    return dictionary


def alert():
    test = set(connected).intersection(adresses)

    print(test)

    i = 0
    print('These are here: ')
    while i < len(test):

        print(homefunc()[list(test)[i]])
        i += 1


homefunc()
devconnected()
print(connected)
print(adresses)
alert()

