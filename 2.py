from tkinter import *
from gtts import gTTS

root=Tk()
root.geometry("600x200")
root.title("Google's Speech Application")
root.config(background='powder blue')

lab1=Label(root,text='Text To Speech',bg='powder blue',fg='black',font=('arial 25 bold')).pack()
lab2=Label(root,text='Enter text',font=('arial 10'),bg='powder blue',fg='black').pack()

mytext=StringVar()
def speech():
    sound=gTTS(text=mytext.get(),lang="en")
    sound.save('Voice.mp3')


ent=Entry(root,text=mytext,font=('arial 30'))
ent.pack()

but=Button(root,text='Convert',bg='brown',fg='white',command=speech)
but.pack()

root.mainloop()

          
