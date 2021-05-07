from Tkinter import *
from threading import Thread
import socket

def enviar():
    #conn.send(text_ent.get())
    #print(text_ent.get())
    s.send(text_ent.get())
    #print(s.recv(1024))
	#text_ent.delete(0, END)
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
            escribir(self.mensaje+'\n')
	    #self.conn.close()
    def parar(self):
        self.stop = True


root = Tk()
miFrame=Frame(root, width=500, height=400)
miFrame.pack()
miLabel=Label(miFrame ,text="Cliente chat")
textarea = Text(miFrame, height=20, width=40)
scroll = Scrollbar(miFrame, command=textarea.yview)
textarea.configure(yscrollcommand=scroll.set)
texto_enviar = StringVar()
text_ent = Entry(miFrame, textvariable=texto_enviar)

btn_enviar = Button(miFrame, text="Enviar", command=enviar)

miFrame.grid()
miLabel.grid(row=0, column=0, columnspan=3)
textarea.grid(row=1, column=0, columnspan=2)
scroll.grid(row=1, column=2, sticky=N+S)
text_ent.grid(row=2, column=0, columnspan=2, sticky=W+E)
btn_enviar.grid(row=3, column=0)


s = socket.socket()
s.connect(("localhost", 8001))

lee=leer(s)
lee.start()


root.mainloop()
