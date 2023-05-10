import tkinter as tk
from random import randrange


window=tk.Tk()
window.geometry('300x250')
window.title('How smart are you?')

window.rowconfigure([0,1],weight=1,minsize=1)
window.columnconfigure([0,1],weight=1,minsize=1)


question=tk.Label(window,text='Are you stupid?')
question.grid(column=0,row=0,columnspan=2)

button_yes=tk.Button(window,text='Yes',bg='lightgreen')
button_yes.grid(column=0,row=1,columnspan=1)

button_no = tk.Button(window, text="No", bg="red")
button_no.grid(column=1,row=1,columnspan=1)

def isnotstupid(event):
    

    button_no.place(x=randrange(50,200), y=randrange(50,200))


def isstupid (event):
    button_no.destroy()
    button_yes.destroy()
    question.destroy()
    knewit=tk.Label(text='Knew it :D')
    knewit.place(relx=0.5,rely=0.5,anchor='center')

button_no.bind('<Button-1>',isnotstupid)
button_yes.bind('<Button-1>',isstupid)




window.mainloop()