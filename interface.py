from tkinter import *
import tkinter.messagebox as messagebox
from PIL import Image, ImageTk
import speech_recognition
import text_processing_pipeline

# set up
root = Tk() 
root.geometry('900x900+200+0')
root.title("Speech to ASL")
                    
Label(root, text='\narticulator', font =('Times New Roman', '30')).pack(padx=20, anchor='w') # title

image = Image.open('images/microphone.png') # Load microphone image
img = image.resize((300, 250))
mic = ImageTk.PhotoImage(img) # convert img
record_btn = mic
img_label= Label(image = record_btn)


def helloCallBack():
   recognized_text = speech_recognition.recognize_from_microphone()
   text_arr, sentiment = text_processing_pipeline.process_text(recognized_text)
   messagebox.showinfo( "Processed Text", "Processed text: " + ". ".join(text_arr) + "\nSentiment: " + sentiment)


#Define the working of the button

def my_command():
   text.config(text= "You have clicked Me...")



#Let us create a dummy button and pass the image
button= Button(root, image=mic,command= my_command, borderwidth=0)
button.pack(pady=30)

text= Label(root, text= "")
text.pack(pady=30)

B = Button(root, text ="Hello", command = helloCallBack).pack()

root.mainloop()