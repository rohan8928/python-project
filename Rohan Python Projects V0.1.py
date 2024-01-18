#!/usr/bin/env python
# coding: utf-8

# In[45]:


def welcome_bot():
    #Welcome User
    print('Welcome to NetTech')
    #Asking user its name
    name=input('Enter user name')
    #Saying hello to user
    print('Hello',name)
    user_input=input('Are you interested in technology?')

    if user_input=='yes':

        #Asking number
        number=input('Enter user mobile number')
        print('Thank you for giving your number',number)
        #Asking Email Id
        email_id=input('Enter user Email Id')
        print('Thank you for giving your Email Id',email_id)
        #Cource interested
        course=input('please enter course name')
        print('Thank you for giving your Course Details',course)
        #Asking location
        location=input('Enter location Where you are interested')
        print('Thank you for giving your Location Details',location)
    else:
        print('thank you for visiting')

def chai_reccommandation():
    #mumbai based chai recommandation bot
    #welcome user to mumbai
    print('Welcome to mumbai')
    #ask user it name
    name=input('please enter your good name:')
    #greeting user
    print('hello',name.title())
    #ask user its budget
    budget=int(input('please enter your budget here :'))
    #500--taj hote
    if budget<=500:
        print('please go to taj hotel')
       #100-500---starbuks
    elif budget>=100 and budget<500:
         print('please go to starbuks')
        #50-100----udipi
    elif budget>=50 and budget<100: 
        print('please go to udapi')
        #10-50----- tapari
    elif budget>=10 and budget<50:
        print('please go to tapari')
        #<10------ no restarunt available thanks for visit
    else:
        print('no restarant available thank you')




def wankhede_crickestadium():
    #welcome to wankhede cricket stadium
    #welcome user
    print('wankhede cricket stadium (Mumbai)')
    #ask user its name
    user_name=input('please enter your name here:')
    #greet user
    print('hello',user_name.title())
    #ask user its budget
    budget=int(input('please enter your budget here:'))
    #15000> front row seat
    if budget>=15000:
        print('front row seat')
    #10000-15000 middle row
    elif budget>=12000 and budget<=15000:
        print('middle row seat')
    #7000-10000 back row
    elif budget>=7000 and budget<=10000:
        print('back row')
    #7000 ticket not available in this ammount
    else:
        print('sorry not available')





def Quiz_game():
    # WELCOME TO THE USER
    print('Welcome To The Quiz Competion Game')
    questaion1=input('How many days do we have in a week?:')
    score=0
    if questaion1=='7': 
        print('Your Ans Is Right')
        score=score+10
    else:
        print('Your Ans Is Wrong')

    print('*'*30)

    questaion2=input('How many days are there in a normal year?:')

    if questaion2=='365': 
        print('Your Ans Is Right')
        score=score+10
    else:
        print('Your Ans Is Wrong')

    print('*'*30)    

    questaion3=input('How many colors are there in a rainbow?:')

    if questaion3=='7': 
        print('Your Ans Is Right')
        score=score+10
    else:
        print('Your Ans Is Wrong')
    print('*'*30)   

    questaion4=input('How many letters are there in the English alphabet?:')

    if questaion4=='26': 
        print('Your Ans Is Right')
        score=score+10
    else:
        print('Your Ans Is Wrong')

    print('Your total Score:',score)    






def heads_and_tails():
    #head and tails
    #welcome in gme
    print('Welcome in Head and Tails Game')
    #user input
    user_input=input('please choose Head or Tails')
    #absdisplay user choose
    print('you choose :',user_input.title())
    #coin toss
    import random
    if random.choice('ht')=='h':
        coin_toss='Head'
    else:
         coin_toss='Tails'

    #display coin result
    print('coin result',coin_toss)
    #if user input== coin toss you win
    if user_input.lower()==coin_toss.lower():
        print('you won')
    # else you loss    
    else:
        print('you loss')
    # else you loss


def dice_game():
    #welcome to Dice game
    #user welcome
    print('welcome to the dice game!')
    #ask user to roll dice
    user_roll=int(input('please enter the number'))
    if user_roll>=1 and user_roll<=6:
        #display user roll
        print('you have choose',user_roll)
        #dice rolled
        import random
        dice_rolled=int(random.choice('123456'))
        #display result
        print('dice result',dice_rolled)
        if user_roll==dice_rolled:
            print('you win!')
        else:
            print('you loose!')
    else:
        print('invalid input')

def dice_game2():
    #welcome to Dice game
    #user welcome
    print('welcome to the dice game!')
    #ask user to roll dice
    user_roll=int(input('please enter the number'))
    if user_roll>=2 and user_roll<=12:
        #display user roll
        print('you have choose',user_roll)
        #dice rolled 
        import random
        dice_rolled=int(random.randrange(2,13))
        #display result
        print('dice result',dice_rolled)
        if user_roll==dice_rolled:
            print('you win! ')
        else:
            print('you loose!')
    else:
        print('invalid input')

def multiplication_table():
    #multipication table
    #welcome user
    print('welcome to the world of multiplication!')
    #take 1 number as input from user
    num=int(input('please enter a number here:'))
    #display multiplication table
    for i in range(1,11):
        print(num,'x',i,'=',num*i)

def cube_table():
    #cube 
    #welcome user
    print('welcome to the cube')
    #take 1 number from user
    num=int(input('please enter a number here'))
    #display cube
    for i in range(1,num+1):
        print('cube of',i,'=',i**3)


def factorial():
    #factorial
    #welcome user
    print('welcome to the factorial')
    #take a number from user
    num=int(input('please enter a number here'))
    #display factorial
    n=1
    for i in range(1,num+1):
        n=n*i

    #display factorial of number
    print(n)


def fibonacii():
    #welcome to fibonacii series
    #welcome user
    print('welcome to the fibonacii series')
    #take a 1number from user
    user_input=int(input('enter your number here:'))
    x=0
    y=1
    for i in range(10,50):
        z=x+y
        print(z)
        x=y
        y=z
    

def password():
    #welcome to the password generator
    #welcome user
    print("welcome to password generator")
    #ask user to have many characters of password is want
    num=int(input("please enter your number here:"))
    if num>=8:
        print("you choose:",)
        import random
        import string
        password=''
        #display password
        for i in range(num):
            password=password+random.choice(string.ascii_letters+string.digits+string.punctuation)
        print(password) 
    else:
        print("sorry you should type at least 8 characters of password")





def countdown():
    #countdown_timer():
    from countdown import countdown
    user_input_minutes=int(input("please enter minutes:"))
    user_input_seconds=int(input("please enter seconds:"))
    #create a countdown of minutes ans seconds
    countdown(mins=user_input_minutes,secs=user_input_seconds)

def mind_game():
    #mind game
    #welcome user
    print('welcome to the mind game')
    #predict a number between 1-5000
    print('predict a number between 1-5000')
    import time
    time.sleep(3)
    #multiply that number with 2
    print('multiply that number with 2')
    time.sleep(3)
    #add 50 in that number
    print('add 50 in that number')
    time.sleep(3)
    #divide that number by 2
    print('divide that number by 2')
    time.sleep(3)
    #now minus guess number from current number
    print('now minus guess number from current number')
    time.sleep(5)
    #now you will get 25 answer
    print('now you will get 25 answer')



import tkinter

#importing tkinter library
import tkinter as tk

#creating a main window
window=tk.Tk()

#change title
window.title('Rohan Bansode')

#size
window.geometry('750x500')


#label
tk.Label(window,text='Python Projects',font=('Helvetica',21)).place(x=270,y=30)


#button
tk.Button(window,text='Multiplication Table',command=multiplication_table).place(x=50,y=130,width=200,height=40)
tk.Button(window,text='mind game',command=mind_game).place(x=280,y=130,width=200,height=40)
tk.Button(window,text='factorial',command=factorial).place(x=500,y=130,width=200,height=40)
tk.Button(window,text='cube table',command=cube_table).place(x=50,y=180,width=200,height=40)
tk.Button(window,text='Countdown',command=countdown).place(x=280,y=180,width=200,height=40)
tk.Button(window,text='password',command=password).place(x=500,y=180,width=200,height=40)
tk.Button(window,text='fibonacii',command=fibonacii).place(x=50,y=230,width=200,height=40)
tk.Button(window,text='dice game',command=dice_game).place(x=280,y=230,width=200,height=40)
tk.Button(window,text='dice_game2',command=dice_game2).place(x=500,y=230,width=200,height=40)
tk.Button(window,text='wankhede_crickestadium',command=wankhede_crickestadium).place(x=50,y=280,width=200,height=40)
tk.Button(window,text='chai_reccommandation',command=chai_reccommandation).place(x=280,y=280,width=200,height=40)
tk.Button(window,text='welcome_bot',command=welcome_bot).place(x=500,y=280,width=200,height=40)



window.mainloop()





# In[ ]:





# In[ ]:





# In[ ]:




