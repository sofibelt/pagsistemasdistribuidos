#ANA SOFIA BELTRAN RIOS 1004716847
import socket
from threading import Thread

clientes = {'Sala_principal':[]}
class Cliente(Thread):
    def __init__(self,conn,addr):
        Thread.__init__(self)
        self.conn=conn
        self.addr=addr
        self.data=''
        self.sala='Sala_principal'
    def run(self):
        while True:
            self.data=self.conn.recv(1024)#se recibe un mensaje
            print('ha dicho: '+self.data.decode())
            self.data=self.data.decode()
            if self.data[0]!='#':
                for i in clientes[self.sala]:
                    if i != self.conn:
                        mensaje=self.addr[0]+' dice: '+self.data
                        i.send(mensaje.encode())#se reenvia un mensaje a todos los otros usuarios
            else:
                if self.data[1]=='c' and self.data[2]=='R':
                    clientes[self.sala].remove(self.conn)
                    self.sala=self.data[4::]
                    clientes[self.sala]=[self.conn]
                    self.conn.send(self.data.encode())
                elif self.data[1]=='g' and self.data[2]=='R':
                    clientes[self.sala].remove(self.conn)
                    self.sala=self.data[4::]
                    clientes[self.sala].append(self.conn)
                    self.conn.send(self.data.encode())
                elif self.data[1]=='e' and self.data[2]=='R':
                    if 'Sala_principal'!=self.sala:
                        clientes[self.sala].remove(self.conn)
                        self.sala='Sala_principal'
                        clientes[self.sala].append(self.conn)
                        self.data+=' cambio'
                        self.conn.send(self.data.encode())
                    else:
                        self.conn.send(self.data.encode())
                elif self.data[1::]=='exit':
                    self.conn.send("#exit".encode())
                    clientes[self.sala].remove(self.conn)
                    break
                elif self.data[1]=='I' and self.data[2]=='R':
                    Info=''
                    for i in clientes:
                        Info+=str(i)
                        Info+=' , \n'
                        for j in clientes[i]:
                            Info+=str(j)
                            Info+=' , \n'
                    self.conn.send(Info.encode())

        self.conn.close()

def main():
    Mi_socket=socket.socket()
    Mi_socket.bind((https://sistemasdistribuidosserver.herokuapp.com/,80))
    Mi_socket.listen(1)
    print ("Soy el servido, vamos a intercambiar mensajes!!!!!")
    while True:
        cli, addr=Mi_socket.accept()
        print("%s:%d se ha conectado." % addr)
        clientes['Sala_principal'].append(cli)
        c=Cliente(cli,addr)
        c.start()




if __name__ == "__main__":
    main()
