import tkinter as tk
from tkinter import LEFT, Text, Button, Entry, LabelFrame, PhotoImage, Radiobutton, StringVar, ttk

root = tk.Tk()

root.title("AutoBot")
root.geometry("1000x700")
root.config(bg = "snow")

titlefarame = tk.Frame(root, width=200, height=200, bg = "snow")
titlefarame.grid(row=0, column=0, columnspan=2)
logo = tk.PhotoImage(file = "email_icon_130945 (1).png")
titlelabel = tk.Label(titlefarame,text='     AutoBot', image = logo, compound=tk.LEFT, font=('Tlwg Mono', 48, 'bold'), bg = "snow", fg = "black")
titlelabel.grid(row=0, column=0)
settinglogo = tk.PhotoImage(file = "settings5_117783.png")
tk.Button(titlefarame, image= settinglogo, bd = 0, bg = "snow", cursor = "hand2", activebackground = "snow").grid(row=0, column=1, padx=100)

choiceframe = tk.Frame(root).grid(row=1, column=0, columnspan=2)
singlevariable = StringVar()
singleradiobutton = Radiobutton(choiceframe, text = 'Single', font=('Tlwg Mono', 30, 'bold'), bg = "snow", activebackground="snow").grid(row=1,column=0, padx = 20)
multiplevariable = StringVar()
multipleradiobutton = Radiobutton(choiceframe, text = 'Multiple', font=('Tlwg Mono', 30, 'bold'), bg = "snow", activebackground="snow").grid(row=1,column=1, padx = 20)

toLabelFrame=LabelFrame(root,text='To: ',font=('Tlwg Mono',16,'bold'),bd=2,fg='black',bg='snow')
toLabelFrame.grid(row=2,column=0,padx=100, columnspan=2)
tofield = Entry(toLabelFrame, font=('Tlwg Mono',16), width = 30).grid(row=2, column=0)
browseimage = PhotoImage(file='browse.png')
browsebutton = tk.Button(toLabelFrame, text = 'Browse', font=(40), image=browseimage, compound=LEFT, bd = 0, bg = "snow", cursor='hand2', activebackground='snow').grid(row=2, column=1, padx = 5)

SubjectFrame=LabelFrame(root,text='Subject: ',font=('Tlwg Mono',16,'bold'),bd=2,fg='black',bg='snow')
SubjectFrame.grid(row=3,column=0,padx=100, columnspan=2)
Subjectfield = Entry(SubjectFrame, font=('Tlwg Mono',16), width = 30).grid(row=3, column=0)

ComposeFrame=LabelFrame(root,text='Compose: ',font=('Tlwg Mono',16,'bold'),bd=2,fg='black',bg='snow')
ComposeFrame.grid(row=4,column=0,padx=100, columnspan=2)
micimage = PhotoImage(file='mic.png')
micbutton = tk.Button(ComposeFrame, image = micimage, bd = 0, bg = "snow", activebackground = "snow", cursor = 'hand2').grid(row=4, column=0)
attachmentimage = PhotoImage(file='attachment.png')
attachmentbutton = tk.Button(ComposeFrame, image = attachmentimage, bd = 0, bg = "snow", activebackground = "snow", cursor = 'hand2').grid(row=4, column=1)
composearea = Text(ComposeFrame, height = 8).grid(row=5, column=0, columnspan=2)
sendimage = PhotoImage(file="send.png")
sendbutton = tk.Button(root, image = sendimage, bd = 0, bg = "snow", activebackground = "snow", cursor = 'hand2').place(x=490,y=540)

root.mainloop()