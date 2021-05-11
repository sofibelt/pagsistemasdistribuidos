#ANA SOFIA BELTRAN RIOS 1004716847
import socket
from threading import Thread

clientes=[]
class Cliente(Thread):
    def __init__(self,conn,addr):
        Thread.__init__(self)
        self.conn=conn
        self.addr=addr
        self.data=''
    def run(self):
        while True:
            self.data=self.conn.recv(1024)#se recibe un mensaje
            #self.conn.send('hola')
            for i in clientes:
                if i != self.conn:
                    i.send(self.addr[0]+' dice: '+self.data)#se reenvia un mensaje a todos los otros usuarios
            #try:
            #    input_data=self.conn.recv(1024)
            #except error:
            #    print("[%s] Error de lectura." % self.name)
            #    break
            #else:
            #    mensaje=str(addr)+' a entrado en el chat'
            #    self.conn.send(mensaje)

Mi_socket=socket.socket()
Mi_socket.bind(("localhost", 8001))
Mi_socket.listen(1)
print ("Soy el servido, vamos a intercambiar mensajes!!!!!")
while True:
    cli, addr=Mi_socket.accept()
    print("%s:%d se ha conectado." % addr)
    clientes.append(cli)
    c=Cliente(cli,addr)
    c.start()

#recibido = cli.recv(1024)
#print("conectado: "+recibido)
#mensaje=""
#mensaje+="BIENVENIDO: "+str(recibido)+'\n'
#mensaje+="tu ip es: "+str(addr[0])+'\n'
#mensaje+="tu puerto es: "+ str(addr[1])+'\n'
#mensaje+="te conectaste a las: "+ str(time.strftime(' %H:%M:%S', time.localtime()))+'\n'
#mensaje+="el dia: "+ str(time.strftime('%Y-%m-%d ', time.localtime()))+'\n'
#cli.send(mensaje)
#cli.close()
#Mi_socket.close()
