from Tkinter import *
def enviar():
    #conn.send(text_ent.get())
    print(text_ent.get())
	#text_ent.delete(0, END)


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
root.mainloop()
