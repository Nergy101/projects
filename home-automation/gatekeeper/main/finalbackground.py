##add option to add devices to file devices.txt##

import os
from time import sleep

def homefunc():
    print('creating dictionaries')
    global dictionary, adresses
    dictionary = {}

    adresses = []
    infile = open('devices.txt')
    text = infile.readlines()
    infile.close()
    i = 0
    while i < len(text):


        addrstart = 2
        endsearch = '":'
        addrend = str(text[i]).find(endsearch)
        begin2search = ':"'
        namestart = str(text[i]).find(begin2search) + 2
        dictionary.update({text[i][addrstart:addrend]:text[i][namestart:-3]})
        ip = text[i][addrstart:addrend]
        adresses.append(ip)
        i += 1

    return dictionary


def devconnected():
    print('updating devices..')
    #os.system('sudo nmap -sn 192.168.178.1/24 > connected.txt')
    #sleep(2)
    infile = open('connected.txt')
    convert = infile.readlines()
    infile.close()
    i = 2

    connected = []
    while i < len(convert):
        thing = convert[i]

        search = thing.find('192.168') #finds the position of common part of ip address range.
        if thing[-2]==')': # gets rid of the ')' nmap puts at the end of the ip address if the device has a name
            connected.append(thing[search:-2])
        else:
            connected.append(thing[search:-1])
        i += 3
    return connected



def alert():
    while True:
        homefunc()
        test = set(devconnected()).intersection(adresses)
        if not os.path.exists('oldlist.txt'): #creates the oldlist.txt file
            outfile = open('oldlist.txt', 'w')
            outfile.close()
        if not os.path.exists('newlist.txt'): #creates the oldlist.txt file
            outfile = open('newlist.txt', 'w')
            outfile.close()
        i = 0
        #print('These are here: ')
        #creation of oldlist
        infile = open('oldlist.txt')
        oldlist = infile.read()
        #list for when a device is added
        openoldlist = str(oldlist[:-1])
        newoldlist = eval(oldlist)
        #list for when a device is removed
        remlist = newoldlist[:-1]
        print(remlist)
        oldlist = newoldlist

        #creation of newlist
        infile2 = open('newlist.txt')
        newlist = infile2.read()
        newnewlist = eval(newlist)
        newlist = newnewlist

        i = 0
        while i < len(test):
            #newlist.append(dictionary[adresses[i]])
            #print(newlist)
            #print(dictionary[adresses[i]])


            i += 1

        difference = set(oldlist) ^ set(newlist)
        #if old is bigger than new, something left and vice versa
        if len(oldlist) > len(newlist):
            if len(difference) == 1:
                print(difference, " has left.")
                x = len(difference)
                infile = open('oldlist.txt', 'w')
                infile.write(str(remlist))

        if len(oldlist) < len(newlist):
            if len(difference) == 1:
                print(difference, " has entered.")
                #delete last character to open file for new device
                infile = open('oldlist.txt', 'w')
                infile.write(openoldlist)
                infile.close()


                infile = open('oldlist.txt', 'a')
                infile.write(", " + str(difference)[1:-1] + ']')
                infile.close()


        sleep(3)
alert()
