from Tkinter import *
from threading import Thread
import socket

def enviar():
    s.send(text_ent.get())
def escribir(texto):
	textarea.insert(END, texto)

class Sala:
    def __init__(self,root,socket):
        self.socket=socket

        #---------------------------------------------------------------------
        #Establecer la ventana
        self.miFrame=Frame(root, width=500, height=400)#ventana medidas
        self.miFrame.pack()#ventana
        self.miLabel=Label(self.miFrame ,text="Cliente chat")#ventana

        textarea = Text(miFrame, height=20, width=40)#ventana
        scroll = Scrollbar(miFrame, command=textarea.yview)#ventana
        textarea.configure(yscrollcommand=scroll.set)#ventana
        #---------------------------------------------------------------------------------

        #Variables de control
        #Las variables de control son objetos especiales que se asocian a los widgets para almacenar sus valores y
        #facilitar su disponibilidad en otras partes del programa. Pueden ser de tipo numerico, de cadena y booleano.

        texto_enviar = StringVar()#Variable de  control
        text_ent = Entry(miFrame, textvariable=texto_enviar)#Toma la variable que ha escrito

        btn_enviar = Button(miFrame, text="Enviar", command=enviar)#configura el boton de enviar
        #el comando lo q hace es utilizar la funcion enviar, para enviarle al socket
        #el texto adquirido en la variable text_ent
        #---------------------------------------------------------------------------------
        #configuracion parte de texto y botones
        miFrame.grid()
        miLabel.grid(row=0, column=0, columnspan=3)
        textarea.grid(row=1, column=0, columnspan=2)
        scroll.grid(row=1, column=2, sticky=N+S)
        text_ent.grid(row=2, column=0, columnspan=2, sticky=W+E)
        btn_enviar.grid(row=3, column=0)

    def enviar():
        self.socket.send(text_ent.get())
        self.text_ent.delete(0, END)
    def escribir(texto):
    	textarea.insert(END, texto)


class leer(Thread):
    def __init__(self, socket):
        Thread.__init__(self)
        self.mensaje = ''
        self.conn = socket
        self.stop = False
    def run(self):
        while (self.stop == False):
            self.mensaje = self.conn.recv( 1024 )
            if self.mensaje[0]=='#' and self.mensaje[1]=='c' and self.mensaje[2]=='R':
                soc = socket.socket()#creamos el socket
                soc.connect(("localhost", 8002))#conectamos el socket
                root2 = Tk()#ventana
                ventana=Sala(root2,soc)
                root2.mainloop()
            else:
                #print(self.mensaje)
                escribir(self.mensaje+'\n')
	    #self.conn.close()
    def parar(self):
        self.stop = True

#---------------------------------------------------------------------------------
#Establecer la ventana
root = Tk()#ventana
miFrame=Frame(root, width=500, height=400)#ventana medidas
miFrame.pack()#ventana
miLabel=Label(miFrame ,text="Cliente chat")#ventana
textarea = Text(miFrame, height=20, width=40)#ventana
scroll = Scrollbar(miFrame, command=textarea.yview)#ventana
textarea.configure(yscrollcommand=scroll.set)#ventana
#---------------------------------------------------------------------------------

#Variables de control
#Las variables de control son objetos especiales que se asocian a los widgets para almacenar sus valores y
#facilitar su disponibilidad en otras partes del programa. Pueden ser de tipo numerico, de cadena y booleano.

texto_enviar = StringVar()#Variable de  control
text_ent = Entry(miFrame, textvariable=texto_enviar)#Toma la variable que ha escrito

btn_enviar = Button(miFrame, text="Enviar", command=enviar)#configura el boton de enviar
#el comando lo q hace es utilizar la funcion enviar, para enviarle al socket
#el texto adquirido en la variable text_ent

#-------------------------------------------------------------------------------------
#configuracion parte de texto y botones
miFrame.grid()
miLabel.grid(row=0, column=0, columnspan=3)
textarea.grid(row=1, column=0, columnspan=2)
scroll.grid(row=1, column=2, sticky=N+S)
text_ent.grid(row=2, column=0, columnspan=2, sticky=W+E)
btn_enviar.grid(row=3, column=0)
#------------------------------------------------------------------------------

s = socket.socket()#creamos el socket
s.connect(("localhost", 8001))#conectamos el socket

lee=leer(s)#se crea un objeto de la clase leer
lee.start()


root.mainloop()
