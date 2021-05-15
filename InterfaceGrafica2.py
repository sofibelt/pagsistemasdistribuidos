from Tkinter import *
from threading import Thread
import socket



class Sala:
    def __init__(self,root,socket):
        self.socket=socket

        #---------------------------------------------------------------------
        #Establecer la ventana
        self.miFrame=Frame(root, width=500, height=400)#ventana medidas
        self.miFrame.pack()#ventana
        self.miLabel=Label(self.miFrame ,text="Cliente chat")#ventana

        self.textarea = Text(self.miFrame, height=20, width=40)#ventana
        self.scroll = Scrollbar(self.miFrame, command=self.textarea.yview)#ventana
        self.textarea.configure(yscrollcommand=self.scroll.set)#ventana
        #---------------------------------------------------------------------------------

        #Variables de control
        #Las variables de control son objetos especiales que se asocian a los widgets para almacenar sus valores y
        #facilitar su disponibilidad en otras partes del programa. Pueden ser de tipo numerico, de cadena y booleano.

        self.texto_enviar = StringVar()#Variable de  control
        self.text_ent = Entry(self.miFrame, textvariable=self.texto_enviar)#Toma la variable que ha escrito

        self.btn_enviar = Button(self.miFrame, text="Enviar", command=self.enviar)#configura el boton de enviar
        #el comando lo q hace es utilizar la funcion enviar, para enviarle al socket
        #el texto adquirido en la variable text_ent
        #---------------------------------------------------------------------------------
        #configuracion parte de texto y botones
        self.miFrame.grid()
        self.miLabel.grid(row=0, column=0, columnspan=3)
        self.textarea.grid(row=1, column=0, columnspan=2)
        self.scroll.grid(row=1, column=2, sticky=N+S)
        self.text_ent.grid(row=2, column=0, columnspan=2, sticky=W+E)
        self.btn_enviar.grid(row=3, column=0)


    def enviar(self):
        self.socket.send(self.text_ent.get())
        self.text_ent.delete(0, END)
    def escribir(self,texto):
        self.textarea.insert(END, texto)
    def cambiarventana(self,nombre):
        self.miLabel['text'] = nombre



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
                #ventana.miFrame.quit()
                #self.conn.send('END')
                #self.parar()
                ventana.cambiarventana(self.mensaje[4::])
                ventana.escribir('ha cambiado a una nueva sala \n')
            else:
                ventana.escribir(self.mensaje+'\n')
        self.conn.close()

    def parar(self):
        self.stop = True




def crear():
    root2=Tk()
    root2.title("pagina 1")
    root2.geometry('500x500')
    root2.configure(background='blue')
    root2.mainloop()

soc = socket.socket()#creamos el socket
soc.connect(("localhost", 8001))#conectamos el socket
lee=leer(soc)
lee.start()
root2 = Tk()#ventana
ventana=Sala(root2,soc)
root2.mainloop()
