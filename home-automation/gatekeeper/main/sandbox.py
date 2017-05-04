infile = open('connected.txt')
convert = infile.readlines()
infile.close()
i = 2
conlist = []
while i < len(convert):
    thing = convert[i]

    search = thing.find('192.168') #finds the position of common part of ip address range.
    if thing[-2]==')': # gets rid of the ')' nmap puts at the end of the ip address if the device has a name
        conlist.append(thing[search:-2])
    else:
        conlist.append(thing[search:-1])
    i += 3
print(conlist)
