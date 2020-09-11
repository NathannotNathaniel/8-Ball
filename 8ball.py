from tkinter import *

import os

import random

#Template for List extension-answers.extend(['','',''])
answers=['As I see it, yes.','Ask agin later','Better not tell you now']
answers.extend(['Cannot predict now','Concentrate and ask again',"Don't count on it"])
answers.extend(['It is certain','It is decidley so','Most likely'])
answers.extend(['My reply is no','My sources say no','Outlook not so good'])
answers.extend(['Outlook good','Reply hazy, try again','Signs point to yes'])
answers.extend(['Very doubtful','Without a doubt','Yes.'])
answers.extend(['Yes-definetly','You may rely on it','No.'])
print(answers)


def getQ():
    global user
    user=question.get()

    f=open('q1.txt','w+')
    f.write('Question: '+user+'\n')
    f.close()

def getA():
    global magic
    magic=ans.get()

    f=open('q1.txt','a+')
    f.write('Answer: '+magic)
    f.close

def answer():
    screen1=Toplevel(screen)
    screen1.title('Magic 8-Ball')
    screen1.geometry('700x600')
    screen1.configure(bg='black')
    global ans
    ans=StringVar()

    Label(screen1,text='The 8-Ball says...',bg='black',fg='purple',width='30',height='5',font=('Sans',30)).pack()
    Label(screen1,textvariable=ans,bg='black',fg='purple',width='30',height='5',font=('Sans',30)).pack()
    ans.set(random.choice(answers))
    Button(screen1,text='Back',width='20',height='2',bg='purple',fg='black',font=('Sans',15),command=mainScreen).pack()
    Button(screen1,text='Get Answers',width='20',height='2',bg='purple',fg='black',font=('Sans',15),command= getA).place(x=475,y=0)

def mainScreen():
    global screen

    screen=Tk()
    screen.geometry('700x600')
    screen.title('Magic 8-Ball')
    screen.config(bg='black')
    global question
    question=StringVar()

    Label(screen,text='Magic 8-Ball',bg='black',fg='purple',width='30',height='5',font=('verdana',40)).pack()
    q=Entry(screen, textvariable=question,bg='black',fg='purple', width='40',font=('verdana',15)).pack()
    Label(screen,text='',bg='black').pack()
    Label(screen,text='',bg='black').pack()
    Button(screen,text='Roll',width='20',height='2',bg='purple',fg='black',font=('Sans',15),command= answer).pack()
    Button(screen,text='Get Questions',width='20',height='2',bg='purple',fg='black',font=('Sans',15),command= getQ).place(x=475,y=0)

    screen.mainloop()



mainScreen()