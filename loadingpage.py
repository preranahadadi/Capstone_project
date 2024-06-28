from tkinter import *
from PIL import Image,ImageTk
import os
import time

def check():
    if not os.path.isfile(r"temp.txt"):
        root.destroy()
        import successpage
    root.after(1000, check)
root = Tk()
root.title("Kannada Subs Generator")
root.geometry('900x800+530+100')

# Head (Canvas)
head = Canvas(root, bg= "black", height= 150, width= 900,
              highlightthickness= 0,relief='ridge')

# Logo
logo = ImageTk.PhotoImage(Image.open("assets/logo.png").resize((200,200), Image.Resampling.LANCZOS))
head.create_image(100,80, image= logo)

# Text Besit logo
head.create_text(280,115, text="GENERATOR", fill="white", font=('Aharoni 22 bold'))

# One more set of Texts
head.create_text(820,75, text="project under guidance of", fill="white",
                 font=('Calibri 10 bold'))
head.create_text(831,95, text="Prof. V Badri Prasad,", fill="white",
                 font=('Calibri 10 bold'))
head.create_text(820,115, text="PES University, Bengaluru", fill="white",
                 font=('Calibri 10 bold'))

# End of Head
head.pack()

body = Canvas(root, bg= "white", height= 800, width= 900, highlightthickness=0, relief='ridge')
body.pack()

body.create_text(450,280, text="Processing...", font=('Calibri 30'), fill="#157bcf")
body.create_text(450, 320, text="This will not take long :)", font=('Calibri 15'), fill="grey")

root.after(1000, check)
root.resizable(False,False)
root.mainloop()