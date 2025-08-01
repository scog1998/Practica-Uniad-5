from tkinter import *

class Ventana(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.msg = Label(self, text="Hola Mundo")
        self.msg.pack()
        self.bye = Button(self, text="Cerrar", command=self.quit)
        self.bye.pack()
        self.pack()

app = Ventana()
mainloop()
