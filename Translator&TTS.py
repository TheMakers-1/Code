import googletrans
from gtts import gTTS 
from tkinter import *
import clipboard

language1 = "en"
count = 1

translator = googletrans.Translator()

trans = Tk()
trans.title("Translator")
trans.geometry("1000x500")



def counting():
    global count
    global language1
    count += 1

    if count % 5 == 1:
        language1 = "en"
        label.config(text="English")

    elif count % 5 == 2:
        language1 = "ko"
        label.config(text="Korean")

    elif count % 5 == 3:
        language1 = "ja"
        label.config(text="Japanese")

    elif count % 5 == 4:
        language1 = "de"
        label.config(text="German")

    else:
        language1 = "zh-cn"
        label.config(text="Chinese")

def tran():
    ent = inputen.get()
    com = translator.translate(ent, dest=language1)
    global pl
    pl = com.text
    pl = str(pl)
    clipboard.copy(pl)

def mp3saveing():
    tts = gTTS(text=pl, lang=language1)
    tts.save("tts.mp3")

inputen = Entry(trans)

bten = Button(trans, text="Trans", command=tran)
language = Button(trans, text="Change Language", command=counting)
label = Label(trans, text="English")
mp3save = Button(trans, text=".mp3 save", command=mp3saveing)

inputen.pack()
bten.pack()
label.pack()
language.pack()
mp3save.pack()

trans.mainloop()
