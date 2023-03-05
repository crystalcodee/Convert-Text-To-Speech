from tkinter import*
from gtts import gTTS
from playsound import playsound
from pydub.playback import play
import os


#Initializing window

root = Tk()
root.geometry("350x300") 
root.configure(bg='ghost white')
root.title("DataFlair - TEXT TO SPEECH")

# Create GUI 

Label(root, text="TEXT_TO_SPEECH",font="Cosmos 20 bold",bg="white smoke").pack()
Label(text ="DataFlair", font = 'Cosmos 20 bold', bg ='white smoke' , width = '20').pack(side = 'bottom')

Msg = StringVar()
Label(root,text ="Enter Text", font = 'Cosmos 20 bold', bg ='white smoke').place(x=20,y=60)

entry_field = Entry(root, textvariable= Msg,width='50')
entry_field.place(x=20,y=100)


#Function to Convert Text into Speech in Python

def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text=Message)
    speech.save("DataFlair.mp3")
    playsound("DataFlair.mp3")
    play(sound='DataFlair.mp3')
    os.remove('DataFlair.mp3')

# Function Exit

def Exit():
    root.destroy()

#Function to Reset

def Reset():
    Msg.set("")

# Define Button

Button(root, text = "PLAY", font = 'arial 15 bold' , command = Text_to_speech ,width = '4').place(x=25,y=140)

Button(root, font = 'arial 15 bold',text = 'EXIT', width = '4' , command = Exit, bg = 'OrangeRed1').place(x=100 , y = 140)

Button(root, font = 'arial 15 bold',text = 'RESET', width = '6' , command = Reset).place(x=175 , y = 140)


root.mainloop()