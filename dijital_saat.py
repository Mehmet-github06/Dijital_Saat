from tkinter import Label, Tk
import time

window = Tk()
window.title("Dijital Saat")
window.geometry("420x150")
window.resizable(0, 0)

Label1 = Label(window,
               font=("Boulder", 68, 'bold'),
               bg='#000000',
               fg="#ffffff",
               bd=25)
Label1.grid(row=0, column=1)

def saat():
    suankiSaat = time.strftime("%H:%M:%S")
    Label1.config(text=suankiSaat)
    window.after(200, saat)

saat()
window.mainloop()




                
