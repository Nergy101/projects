import os
from time import sleep
def connected():
    print('updating devices..')
    os.system('nmap -sn 192.168.178.1/24 > connected.txt')
    sleep(3)
    infile = open('connected.txt')
    convert = infile.readlines()
    infile.close()
    i = 4
    home = []
    while i < (len(convert) - 1):
        thing = convert[i]

        if thing[-17] == '(':
            home.append(thing[-16:-2])
        else:
            home.append(thing[-15:-1])
        i += 2

    #print(home)
    return home

def homefunc():
    dictionary = {}
    if not os.path.exists('devices.txt'):
        infile = open('devices.txt', 'w')
    else:
        infile = open('devices.txt')
        text = infile.readlines()
        infile.close()
        i = 0
        while i < len(text):
            name = text[i][2:-20]

            adress = text[i][-17:-3]
            dictionary.update({adress:name})
            i += 1
        #print(dictionary)
    return str(dictionary)




print("devices that are home: " + str(connected()))
print("list of devices " + str(homefunc()))
