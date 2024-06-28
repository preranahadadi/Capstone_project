from tkinter import *
from PIL import Image,ImageTk
import subprocess
import os
import cv2
import vlc
import time
import moviepy.editor

def movie_duration(path):
    video = moviepy.editor.VideoFileClip(path)
    return int(video.duration) + 1

def playVideo():
    duration = movie_duration(videoPath)
    vlc_instance = vlc.Instance()
    player = vlc_instance.media_player_new()
    media = vlc_instance.media_new(videoPath)

    player.set_media(media)
    player.play()
    time.sleep(duration)
    player.stop()


def restart():
    root.destroy()
    subprocess.call('python main.py')
    #subprocess.Popen("Python main.py")

file = open("temp1.txt","r")
videoPath = file.readline()
file.close()

videoSuffix = videoPath.split('/')[-1]
print(videoSuffix)
videoSuffix = videoSuffix[:videoSuffix.index('.')]
print(videoSuffix)
 
os.remove("temp1.txt")

cam = cv2.VideoCapture(videoPath)

currframe = 0
while True:
    ret, frame = cam.read()
    if ret:
        if os.path.isfile(f'./assets/{videoSuffix}'):
            os.remove(f'./assets/{videoSuffix}')

        name = f'./assets/{videoSuffix}.png'
        cv2.imwrite(name, frame)
        break
    currframe += 1

root = Tk()
root.title("Kannada Subs Generator")
root.geometry('900x800+530+100')

# Head (Canvas)
head = Canvas(root, bg= "black", height= 150, width= 900,
              highlightthickness= 0,relief='ridge')

# Logo
logo = ImageTk.PhotoImage(Image.open("assets/logo.png").resize((200, 200), Image.Resampling.LANCZOS))
head.create_image(100, 80, image= logo)

# Text Besit logo
head.create_text(280, 115, text="GENERATOR", fill="white", font=('Aharoni 22 bold'))

# One more set of Texts
head.create_text(820, 75, text="project under guidance of", fill="white",
                 font=('Calibri 10 bold'))
head.create_text(831, 95, text="Prof. V Badri Prasad,", fill="white",
                 font=('Calibri 10 bold'))
head.create_text(820, 115, text="PES University, Bengaluru", fill="white",
                 font=('Calibri 10 bold'))

# End of Head
head.pack()

body = Canvas(root, bg= "white", height= 800, width= 900, highlightthickness=0, relief='ridge')
success = ImageTk.PhotoImage(Image.open("assets/success.png").resize((100,100), Image.Resampling.LANCZOS))
body.create_rectangle(-10, -10, 300, 650, fill="#157bcf",outline="white")
body.create_image(150, 100, image= success)
body.create_text(150, 180, text="Done!", fill="#56E300", font=('Calibri 30 bold'))
videoThumbnail = ImageTk.PhotoImage(Image.open(f"assets/{videoSuffix}.png").resize((445,250), Image.Resampling.LANCZOS))
body.create_image(600, 165, image=videoThumbnail)
body.pack()

play_button = Button(root,height=50, width= 128, highlightthickness=0, command= playVideo,
                       relief='ridge', bd=0)
play_button_image = ImageTk.PhotoImage(Image.open("assets/play.png").resize((128,50), Image.Resampling.NEAREST))
play_button.config(image=play_button_image)
play_button.place(x= 540, y= 480)

home_button = Button(root,command= restart,height=50, width= 161, highlightthickness=0,
                       relief='ridge',bd=0)
home_button_image = ImageTk.PhotoImage(Image.open("assets/home.png").resize((161,50), Image.Resampling.LANCZOS))
home_button.config(image=home_button_image)
home_button.place(x= 525, y= 560)

root.resizable(False, False)
root.mainloop()