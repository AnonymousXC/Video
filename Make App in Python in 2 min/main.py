from tkinter import *



def window():
    win = Tk()
    win.title("My First Python App")
    win.geometry("500x500")
    widgets(win)
    win.mainloop()


def widgets(window):
    lab1 = Label(text="Hello World")
    lab1.pack()


if __name__ == "__main__":
    window()