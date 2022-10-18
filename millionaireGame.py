import os
import sys
import random 

def clearing():   
    clear=lambda:os.system("cls")
    clear()

def exiting():
    print(exit) 
    sys.exit(0)

def testTheScore(z):
    if z>=0 and  z<=4 :
        return "your score is 0$"
    elif z==5 or z==6 :
        return "your score is 1000$"
    elif z==7 or z==8:
        return "your score is 5000$"
    elif z==9:
        return "your score is 250000$"

print ("Welcome to the show -Millionaire Game-")
print ("1- Adan Jbareen")
print ("2- fatima badran")
play=str(input("To go on write- s "))
while not play =='s' or play=='S':
    play=str(input("To go on write- s "))
if play=='s' or play=='S':
    clearing()
    print ("Let's start the game, There will be 10 questions \n\
that are Simplier questions in python \n\
go first and are worth less \n\
The game consists of a screen that displays a question each time and 4 possible answers. About the user \n\
Choose one answer from their sons by absorbing the answer number that seems right to them")        
    print("the beginning-   1) 100$      ")
    print("                 2) 200$      ")
    print("                 3) 300$      ")
    print("                 4) 500$      ")
    print("                 5) 1000$     ")
    print("                   -----      ")
    print("                 6) 2000$     ")
    print("                 7) 5000$     ")
    print("                   -----      ")
    print("                 8) 10,000$   ")
    print("                 9) 250,000$  ")
    print("                   -----      ")
    print("the end-         10)1,000,000$")
    print("The game has 10 questions. If the user is mistaken, the game is over and the user is notified \n\
and the amount accumulated in the game")                                                     
    print("you have 2 options to get one time help")                                                                                                                                                     
    print("1-Contact with a friends , that can help to find the answer ")                                                                                                
    print("2- delete 2 of the answers  that mean delete the wrong    ")                                       
    print("**you always can quite before go to the next question** ")                                                                   
    print("So, let's get started!")
    start=str(input("To start the game write s- "))
    while not start=='s' or start=='S':
        start=str(input("To start the game write s- "))
    if start=='s' or start=='S':
        clearing()
        question=['1-print("Good"+"Day"+"):','2-what is String: (example)','3-price+=5:','4-sign- // :','5-what is end: ','6-ord() :','7-pow(10,2) :','8-abs(-123) :','9-math.sqrt(100) :','10-range(7,10) :']
        Answer=['a','b','a','a','d','b','c','d','b','d']
        choices=['a=Good Day','b=goodday','c=null','d=no answers','a=a,b,c,...','b=good','c=1,2,3,...','d=no answers','a= price=price+5','b= price+5','c= price=5','d= no answers','a= division','b= note','c= exponentiation','d= rest','a= comma','b= the end of the line','c= new line','d= space','a= receives a number and return code ascii','b= receives a char and return code ascii','c= receives a string and return code ascii','d=no answer','a= 20','b= 8','c= 100','d= 12','a= 3','b= -120','c= 1 2 3','d= 123','a= 10^2','b= 10','c= 100','d= -100','a= 7 8 9 10','b= 8 9','c= 8 9 10','d= 7 8 9']
        Help50=['a=Good Day','b=goodday','a=a,b,c,...','b=good','a= price=price+5','b= price+5','a= division','b= note','a= comma','d= space','a= receives a number and return code ascii','b= receives a char and return code ascii','b= 8','c= 100','c= 1 2 3','d= 123','a= 10^2','b= 10','a= 7 8 9 10','d= 7 8 9']
        score = ['100$','200$','300$','500$','1000$','2000$','5000$','10000$','250000$','1000000$']
        i=0 
        j=0
        count50=0
        countF=0
        for z in range(0,10):
            print(question[z])
            j+=4
            for  i in range(i,j):
                print(choices[i])
            i+=1
            print("")
            continu=str(input ("if you want to continue the questions y \ n: "))
            while not ( continu=='n' or continu=='N' or continu=='y' or continu=='Y'):
               continu=str(input ("if you want to continue the questions y \ n: "))
            if continu=='n' or continu=='N':
                if z==0:
                    clearing()
                    print("now you exit the game")
                    print("0$")
                else:
                    clearing()
                    print("now you exit the game")
                    print(score[z-1])
                exiting()
            elif continu=='y' or continu=='Y':
                print("")
                print("if you want to delete to option press 1")
                print("if you want help from your friend press 2")
                x=int(input ("if you want to continue with out help press 3\n"))
                while not (x==1 or x==2 or x==3):
                     x=int(input ("press 1 or 2 or 3 "))
                if x==3 :
                    print("")
                    y=str(input("enter the correct answer (use a small letter a/b/c/d): "))
                    while not (y=='a' or y=='b' or y=='c' or y=='d'):
                        y=str(input("enter the correct answer (use a small letter a/b/c/d): "))
                    if(y==Answer[z]):
                        clearing()
                        if z>=0 and z<9:
                            print("your answer is correct so your score is:",score[z])
                            print("")
                        else:
                            print("you completed all the questions and the all is correct so your win:",score[z])
                            print("Congratulations, you deserve it")
                    else:
                        clearing()
                        print("your answer is un correct so :")
                        print(testTheScore(z))
                        exiting()
                elif x==2 and countF==0:            
                    countF+=1 
                    abcd=random.choice("abcd")
                    print("friend answer:",abcd)
                    y=str(input("enter the correct answer (use a small letter a/b/c/d): "))  
                    if(y==Answer[z]):
                        clearing()
                        print("your answer is correct so your score is:",score[z])
                    else:
                        clearing()
                        print("your answer is un correct so you exit the game \n")
                        print(testTheScore(z))
                        exiting()
                elif countF ==1 and count50==0:
                        print("this option is used")
                        help = int(input ("choose option 2 (Enter 1): "))
                        if help==1:
                            count50+=1 
                            print(Help50[z*2])
                            print(Help50[z*2+1])
                            y=str(input("enter the correct answer (use a small letter a/b/c/d): "))  
                            if(y==Answer[z]):
                                clearing()
                                print("your answer is correct so your score is:",score[z])
                            else:
                                clearing()
                                print("your answer is un correct:")
                                print(testTheScore(z))
                                exiting()
                elif count50==1 and countF ==0  :
                        print("this option is used")
                        help = int(input ("choose option 2 (Enter 2): "))
                        if help==2:
                            countF+=1 
                            abcd=random.choice("abcd")
                            print("friend answer:",abcd)
                            y=str(input("enter the correct answer (use a small letter a/b/c/d): "))  
                            if(y==Answer[z]):
                                clearing()
                                print("your answer is correct so your score is:",score[z])
                            else:
                                clearing()
                                print("your answer is un correct :")
                                print(testTheScore(z))
                                exiting()
                elif x ==1 and count50==0:
                    count50+=1 
                    print(Help50[z*2])
                    print(Help50[z*2+1])
                    y=str(input("enter the correct answer (use a small letter a/b/c/d): "))
                    if(y==Answer[z]):
                        clearing()
                        print("your answer is correct so your score is:",score[z])
                    else:
                        clearing()
                        print("your answer is un correct ")
                        print(testTheScore(z))
                        exiting()
                elif count50 == 1 and countF==1:
                        clearing()
                        print("two option are used ")
                        print("your are exit the game ")
                        print(testTheScore(z))
                        exiting()