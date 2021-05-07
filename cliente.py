#ANA SOFIA BELTRAN RIOS 1004716847
import socket

s = socket.socket()
s.connect(("localhost", 8001))
while True:
    mensaje=input('>')
    if mensaje:
        s.send(mensaje)
        print(s.recv(1024))
#s.close()
'''
Bienvenido: Cesar Jaramillo
tu ip es: 127.0.0.1
tu puerto es: 56789
te conectaste a las: 5:26
el dia: 25/03/2021
'''
