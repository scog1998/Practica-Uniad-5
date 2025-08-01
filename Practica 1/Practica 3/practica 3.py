from tkinter import *

class Ventana(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.msg = Label(self, text="")
        self.msg.pack()
        self.bye = Button(self, text="Cerrar", command=self.quit)
        self.bye.pack()
        self.pack()
top = Tk()
rotulo = Label(top, text="Rotulo ejemplo", foreground="blue")
rotulo.pack()
rotulo.configure(relief="ridge", font="Arial 24 bold", border=5, background="yellow")

a = Label(top, text="A"); a.pack(side="left")
b = Label(top, text="B"); b.pack(side="bottom")
c = Label(top, text="C"); c.pack(side="right")
d = Label(top, text="D"); d.pack(side="top")

app = Ventana(master=top)
app.pack()
top.mainloop()
