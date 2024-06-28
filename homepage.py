from tkinter import *
from PIL import Image,ImageTk
from tkinter import filedialog
import os

def browser():
    filename = filedialog.askopenfilename(initialdir="Desktop",
                                          title="Select")

    file = open("temp.txt","a")
    file.write(filename)
    file.close()
    root.destroy()
    
# Creating Window
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

# Body - Canvas
body = Canvas(root, bg= "white", height= 800, width= 900, highlightthickness=0, relief='ridge')
body.create_text(450,350, text= "Or", fill="#157bcf", font=('Calibri 18'), )
body.create_oval(-550, 1100, 1500, 400, fill="#157bcf", width=0)
body.create_text(453, 440, text = "Drop file here", fill="white", font=('Calibri 18'))
body.create_text(90, 20, text="Simple. Easy to Use.", fill="grey", font=('Calibri 15'))
text = "Select a English Video file to insert Kannada subtitles.\n      (For best results try clips of length 2 - 5 mins)"
body.create_text(455, 220, text=text, fill="grey", font=('Calibri 10'))
# End of Body
body.pack()

# button created from image
browse_button = Button(root, command= browser,height=60, width= 155, highlightthickness=0, relief='ridge', bd=0)
button_image = ImageTk.PhotoImage(Image.open("assets/button.png").resize((155,60), Image.Resampling.LANCZOS))
browse_button.config(image=button_image)
browse_button.place(x= 375, y= 400)

root.resizable(False,False)
root.mainloop()