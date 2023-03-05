from tkinter import *
import tkinter.messagebox as messagebox
from PIL import Image, ImageTk
import speech_recognition
import text_processing_pipeline
from tkvideo import tkvideo
import emoji
from video_processing import text_to_video

"""
I hate this job. I was not expecting customers today. I hate you. I am happy you are here. 
"""

# set up
root = Tk() 
root.geometry('1200x900')
bg_col = "#040f2e"
root.configure(bg=bg_col)
root.title("Speech to ASL")
                    
Label(root, text='\narticulator', font =('Times New Roman', '30'), bg = bg_col, fg = 'white').pack(padx=20, anchor='w') # title
def emoji_display(sentiment):
    # ['anger', 'fear', 'sadness', 'joy', 'love', 'surprise']
   if (sentiment == 'anger'):
      Label(root, text=emoji.emojize(":enraged_face:"), font =('Times New Roman', '30'), bg = bg_col, fg = 'white').place(x = 200, y = 600)
   if (sentiment == 'fear'):
      Label(root, text=emoji.emojize(":fearful_face:"), font =('Times New Roman', '30'), bg = bg_col, fg = 'white').place(x = 200, y = 600)
   if (sentiment == 'sadness'):
      Label(root, text=emoji.emojize(":sad_but_relieved_face:"), font =('Times New Roman', '30'), bg = bg_col, fg = 'white').place(x = 200, y = 600)
   if (sentiment == 'joy'):
      Label(root, text=emoji.emojize(":grinning_face_with_big_eyes:"), font =('Times New Roman', '30'), bg = bg_col, fg = 'white').place(x = 200, y = 600)
   if (sentiment == 'love'):
      Label(root, text=emoji.emojize(":smiling_face_with_hearts:"), font =('Times New Roman', '30'), bg = bg_col, fg = 'white').place(x = 200, y = 600)
   if (sentiment == 'surprise'):
      Label(root, text=emoji.emojize(":anguished_face:"), font =('Times New Roman', '30'), bg = bg_col, fg = 'white').place(x = 200, y = 600)

def helloCallBack():

   Label(root, text="speak now", font =('Times New Roman', '20'), bg = bg_col, fg = 'white').place(x = 1000, y = 555)

   recognized_text = speech_recognition.recognize_from_microphone()
   text_arr, sentiment = text_processing_pipeline.process_text(recognized_text)
#    messagebox.showinfo( "Processed Text", "Processed text: " + ". ".join(text_arr) + "\nSentiment: " + sentiment)
   caption = ". ".join(text_arr) + "\nSentiment: " + sentiment
   Label(root, text=caption, font =('Times New Roman', '20'), bg = bg_col, fg = 'white').place(x = 300, y = 600)
   emoji_display(sentiment)
   my_label = Label(root)
   my_label.pack(anchor='w', padx=50)
   video = text_to_video(recognized_text)
   # player = tkvideo("videos/interested.mp4", my_label, loop = 1, size = (850,450))
   player = tkvideo(video, my_label, loop = 1, size = (850,450))
   player.play()

image = Image.open("images/microphone.png") # Load microphone image
img = image.resize((150, 150))
mic = ImageTk.PhotoImage(img) # convert img
record_btn = mic
img_label= Label(image = record_btn)
button= Button(root, image=mic,command= helloCallBack, borderwidth=0)
# button.pack(padx=50,pady=30)
button.place(x=1000, y=400) 

image = Image.open('images/switch.png')
img = image.resize((150, 150))
switch = ImageTk.PhotoImage(img) # convert img
img_label= Label(image = switch)
img_label.place(x=1000, y=100) 

root.mainloop()