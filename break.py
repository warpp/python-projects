from Tkinter import *
import tkMessageBox
import time
import webbrowser

#create the window
root = Tk()
root.title("Take a break!")
root.geometry("200x200")

def takeabreak():
    breaks = 3
    count = 0
    tkMessageBox.showinfo("Break", "Timer started on " + time.ctime())
    while (count < breaks):
        time.sleep(7200)
        webbrowser.open("http://youtu.be/WsOoCu1_PVE")
        count += 1

button = Button(root, text="Take A Break!", command = takeabreak)
button.pack(expand=TRUE)
root.mainloop()



