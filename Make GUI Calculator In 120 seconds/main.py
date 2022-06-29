from tkinter import *

def window():
    win = Tk()
    win.geometry("500x500")
    win.title("Python Calculator")
    win.resizable(width=False, height=False)
    win.configure(background="#161616")
    widgets(win)
    win.mainloop()

def widgets(window):
    lab1 = Label(text="Expression")
    lab1.configure(background="#161616", foreground="#fff", font=80)
    lab1.place(x=20, y=20)

    global inp 
    inp = Text(width=80, height=1, background="#181818", foreground="#fff", insertbackground="#FFF")
    inp.place(x=120, y=20)

    btn = Button(text="Calculate", command=calculate)
    btn.place(x=250, y=160)

    global output
    output = Label()
    output.configure(background="#161616", foreground="#fff", font=80)
    output.place(x=250, y=300)


def calculate():
    expression = inp.get(1.0, END)
    try:
        out = eval(expression)
        output.configure(text=out)
    except Exception:
        pass

if __name__ == "__main__":
    window()