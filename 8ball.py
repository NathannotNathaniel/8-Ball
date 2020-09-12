#Tkinter GUI Module
from tkinter import *

#Os to write and read files
import os

#random for the random list value
import random

#To do List
    #Have user be able to view q1 file
    #Have multiple commands so you can hit roll and record question (Maybe put the buttons in the same palce using .place() instead of pack
    #Figure out how to delted a screen so that a bunch of screens don't stay on while you 
    #Try to put 8-ball image in screens

#Answers list for Magic 8 Ball answers
#Template for List extension-answers.extend(['','',''])
#.extend to add multiple list values (append is one)
answers=['As I see it, yes.','Ask agin later','Better not tell you now']
answers.extend(['Cannot predict now','Concentrate and ask again',"Don't count on it"])
answers.extend(['It is certain','It is decidley so','Most likely'])
answers.extend(['My reply is no','My sources say no','Outlook not so good'])
answers.extend(['Outlook good','Reply hazy, try again','Signs point to yes'])
answers.extend(['Very doubtful','Without a doubt','Yes.'])
answers.extend(['Yes-definetly','You may rely on it','No.'])

#Function to write the Question in the q1 file
def getQ():
    global user
    user=question.get()

    f=open('q1.txt','w+')
    f.write('Question: '+user+'\n')#Question string, plus the users question on the screen, plus a newline
    f.close()

#Function to put the random list answer into q1 txt file
def getA(): 
    global magic 
    magic=ans.get()

    f=open('q1.txt','a+')#name of the file;'a+'appends to a list doesn't overwrite it and read the file with the +
    f.write('Answer: '+magic)
    f.close

def viewQA():
    screen2=Toplevel(screen) #puts screen2 over screen
    screen2.title('Magic 8-Ball')
    #Screen size
    screen2.geometry('700x600')
    #Makes all screenspace not 
    screen2.configure(bg='black')
    
    #View the Files
    f=open('q1.txt','r')
    qa=f.read()
    #q=f.readline()
    #a= f.readline()

    Label(screen2,text=qa,bg='black',fg='purple',width='30',height='5',font=('Sans',30)).pack()
    #Label(screen2,text=a,bg='black',fg='purple',width='30',height='5',font=('Sans',30)).pack()
    #Buttom to send User back to hoem screen to ask another question
    Button(screen2,text='Back',width='20',height='2',bg='purple',fg='black',font=('Sans',15),command=mainScreen).pack()
    f.close()


def answer():
    screen1=Toplevel(screen) #puts screen1 over screen
    screen1.title('Magic 8-Ball')
    #Screen size
    screen1.geometry('700x600')
    #Makes all screenspace not 
    screen1.configure(bg='black')
    #Varible to record the random list value in a var for the file to write
    global ans
    ans=StringVar()

    Label(screen1,text='The 8-Ball says...',bg='black',fg='purple',width='30',height='5',font=('Sans',30)).pack()
    Label(screen1,textvariable=ans,bg='black',fg='purple',width='30',height='5',font=('Sans',30)).pack()
    #set means you can add the text without putting the text in the widget
    ans.set(random.choice(answers))
    #Buttom to send User back to hoem screen to ask another question
    Button(screen1,text='Back',width='20',height='2',bg='purple',fg='black',font=('Sans',15),command=mainScreen).pack()
    #Button to record random list value in q1 file
    Button(screen1,text='Get Answers',width='20',height='2',bg='purple',fg='black',font=('Sans',15),command= getA).place(x=475,y=0)

#Home screen to ask question
def mainScreen():
    global screen
    screen=Tk()
    screen.geometry('700x600')
    screen.title('Magic 8-Ball')
    screen.config(bg='black')
    global question
    question=StringVar()

    Label(screen,text='Magic 8-Ball',bg='black',fg='purple',width='30',height='5',font=('verdana',40)).pack()
    #text variable to store text in StringVar()
    Entry(screen, textvariable=question,bg='black',fg='purple', width='40',font=('verdana',15)).pack()
    #Blank space to seperate Button and Entry ( don't have to this for other formats liek .palce() or grid() )
    Label(screen,text='',bg='black').pack()
    Label(screen,text='',bg='black').pack()
    #Button to get Magic 8 Ball answer for question
    Button(screen,text='Roll',width='20',height='2',bg='purple',fg='black',font=('Sans',15),command= lambda:[getQ(),answer()]).place(x=235,y=402)
    #To view the Q and A file
    Button(screen,text='Views Questions\nand Answers',width='13',height='3',bg='purple',
                        fg='black',font=('Sans',15),command= viewQA).place(x=0,y=0)

    #Have to add in your first screen
    screen.mainloop()


#Make sure to call your homescreen function
mainScreen()