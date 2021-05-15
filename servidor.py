#ANA SOFIA BELTRAN RIOS 1004716847
import socket
from threading import Thread

clientes=[[],[],[],[]]
class Cliente(Thread):
    def __init__(self,conn,addr):
        Thread.__init__(self)
        self.conn=conn
        self.addr=addr
        self.data=''
        self.sala=0
    def run(self):
        while True:
            self.data=self.conn.recv(1024)#se recibe un mensaje
            if self.data=='END':
                self.conn.send(" ")
                clientes.remove(self.conn)
                break
            elif self.data[0]!='#':
                for i in clientes[self.sala]:
                    if i != self.conn:
                        i.send(self.addr[0]+' dice: '+self.data)#se reenvia un mensaje a todos los otros usuarios
            else:
                if self.data[1]=='c' and self.data[2]=='R':
                    self.sala+=1
                    clientes[self.sala].append(self.conn)
                    self.conn.send(self.data)
        self.conn.close()

Mi_socket=socket.socket()
Mi_socket.bind(("localhost", 8001))
Mi_socket.listen(1)
print ("Soy el servido, vamos a intercambiar mensajes!!!!!")
while True:
    cli, addr=Mi_socket.accept()
    print("%s:%d se ha conectado." % addr)
    clientes[0].append(cli)
    c=Cliente(cli,addr)
    c.start()
