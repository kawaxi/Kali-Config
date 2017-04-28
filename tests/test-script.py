#! /bin/python


#--- script to replace an specific line a file 

with open('/root/.config/hexchat/prueba.conf', 'r') as iFile:
    x = iFile.read().splitlines()

x[451] = 'HOLA SOY UN CHINGON \n segundalinea\n\n'

with open('/root/.config/hexchat/new-config.conf', 'w') as oFile:
    for i in x:
        oFile.write(i + '\n')
