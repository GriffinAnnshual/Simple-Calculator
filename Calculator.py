import tkinter
from tkinter import *
import tkinter.font as font

window = Tk()
window.geometry('400x400')

window.title("My Calculator")
window['bg']='DarkSeaGreen1'

#Add widgets
e = Entry(window,font = font.Font(size= 20), width = 80 , borderwidth=5 )
e.place(x = 0,y = 0,height = 50)



def function(a):
    while '/' in a:
        T = a.index('/')
        firstno =float(a[T-1])
        secondno =float(a[T+1])
        result = firstno / secondno
        a[T]=str(result)
        a.pop(T-1)
        a.pop(T)
   
    while 'x' in a:
        T = a.index('x')
        firstno = float(a[T-1])
        secondno =float(a[T+1])
        result = firstno * secondno
        a[T]=str(result)
        a.pop(T-1)
        a.pop(T)
    
    while '-' in a:
        T = a.index('-')
        firstno = float(a[T-1])
        secondno =float(a[T+1])
        result = firstno - secondno
        a[T]=str(result)
        a.pop(T-1)
        a.pop(T)
    
    while '+' in a:
        T = a.index('+')
        firstno = float(a[T-1])
        secondno =float(a[T+1])
        result = firstno + secondno
        a[T]=str(result)
        a.pop(T-1)
        a.pop(T)
    G = (float(a[0]))
    return G



def createNewWindow():
    window2 = Tk()
    window2.geometry('350x150')
    window2.title("press Exit to close")
    window2['bg']='pale green'
    label = Label(window2,text = "THANKS FOR USING \n MY CALCULATOR",font =('Comic Sans MS',20),fg = 'IndianRed2',bg = 'pale green')
    label.place()
    label.pack()
    label2= Label(window2,text = "Purely programmed using python by s Griffin Annshual",font =('Comic Sans MS',10),fg = 'IndianRed2',bg = 'pale green')
    label2.place(x=10,y=75)
    label2= Label(window2,text = "Please send your Feedbacks @Whatsapp-8903396562",font =('Comic Sans MS',10),fg = 'IndianRed2',bg = 'pale green')
    label2.place(x=10,y=125)
    
    x = Button(window2,text ='EXIT',width = '10',bg ='tomato',fg='white',command=window2.destroy)
    x.place(x=125,y=100)

    
    
List = []
b = ''
def btclick(num):
    if num not in ['+','-','/','x','Ans','CLEAR']:
        global b
        b = str(b) + num
    if num not in ['+','-','/','x','Ans','CLEAR']:
        current = e.get()
        e.delete(0,END)
        e.insert(0,str(current)+str(num))
        
    if num in ['+','-','/','x']:
        Acurrent = e.get()
        e.delete(0,END)
        e.insert(0,str(Acurrent)+str(num))
        List.append(b)
        b = ''
        List.append(num)
    
    if num == 'CLEAR':
        e.delete(0,END)
        List.clear()
        b = ''
    if num == "Ans":
        List.append(b)
        Res = function(List)
        e.delete(0,END)
        e.insert(0,Res)
    
        
        
#BUTTONS
myFont = font.Font(size=12)
        
c = Button(window,font= myFont,text ='1',width =12,command=lambda:btclick('1'),bg ='pale green')

c.place(x=10,y =60)


c = Button(window,font=myFont,text ='2',width =12,command=lambda:btclick('2'),bg ='pale green')
c.place(x=140,y =60)


c = Button(window,font=myFont,text ='3',width =12,command=lambda:btclick('3'),bg ='pale green')
c.place(x=270,y =60)


c = Button(window,font=myFont,text ='4',width =12,command=lambda:btclick('4'),bg ='pale green')
c.place(x=10,y =120)


c = Button(window,font=myFont,text ='5',width =12,command=lambda:btclick('5'),bg ='pale green')
c.place(x=140,y =120)


c = Button(window,font=myFont,text ='6',width =12,command=lambda:btclick('6'),bg ='pale green')
c.place(x=270,y =120)


c = Button(window,font=myFont,text ='7',width =12,command=lambda:btclick('7'),bg ='pale green')
c.place(x=10,y =180)


c = Button(window,font=myFont,text ='8',width =12,command=lambda:btclick('8'),bg ='pale green')
c.place(x=140,y =180)

c = Button(window,font=myFont,text ='9',width =12,command=lambda:btclick('9'),bg ='pale green')
c.place(x=270,y =180)

c = Button(window,font=myFont,text ='+',width =12,command=lambda:btclick('+'),bg ='green yellow')
c.place(x=10,y =240)

c = Button(window,font=myFont,text ='0 ',width =12,command=lambda:btclick('0'),bg ='pale green')
c.place(x=140,y =240)

c = Button(window,font=myFont,text ='-',width =12,command=lambda:btclick('-'),bg ='green yellow')
c.place(x=270,y =240)



c = Button(window,text ='x',font=myFont,width =12,command=lambda:btclick('x'),bg ='green yellow')
c.place(x=10,y =300)

c = Button(window,text ='/',font=myFont,width =12,command=lambda:btclick('/'),bg ='green yellow')
c.place(x=140,y =300)

c = Button(window,text ='CLEAR',font=myFont,width =12,command=lambda:btclick('CLEAR'),bg ='green yellow')
c.place(x=270,y =300)


c = Button(window,font=myFont,text ='Ans',width =12,command=lambda:btclick('Ans'),bg ='green yellow')
c.place(x=140,y =350)

c = Button(window,font=myFont,text ='Click Me!',width =12,command=lambda:[createNewWindow(),window.destroy()],bg ='tomato',fg= 'white')
c.place(x=270,y =350)


#mainloop
window.mainloop()
a
