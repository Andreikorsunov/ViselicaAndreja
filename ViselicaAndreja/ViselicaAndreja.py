from tkinter import *
from tkinter import messagebox
import random
def chel():
    global ss,ll,ss1,n,ffdata,temps,first
    first = inpp.get()
    input1.delete(0,END)
    if(n>0):
        if(first in ss):
            for i in range(ss1):
                if(ss[i] == first and ll[i] == '?'):
                    ll.pop(i)
                    ll.insert(i,ss[i])
                    xx = ''.join(ll)#join - добавляет разделители
                    ss = list(ss)
                    ss.pop(i)
                    ss.insert(i,"?")
                    wordlabel.configure(text=xx)
                    if(xx==temps):
                        ans.configure(text='Ты победил!')
                        res = messagebox.askyesno("Сообщение",'Поздравляю, ты победил!\n хочешь попробовать ещё раз?')
                        if(res==True):
                            rword()
                        else:
                            root.destroy() 
                    else:
                        break
        else:
            n -= 1
            try1.configure(text='Попыток = {}'.format(n))
    if(n<=0):
        ans.configure(text='Ты проиграл!')
        res = messagebox.askyesno("Сообщение", 'Ты проиграл!\n хочешь попробовать ещё раз?')
        if (res == True):
            rword()
        else:
            root.destroy()#будет нажата кнопка, окно уничтожится


def jj(event):
    chel()

list1 = ['женщина','мужчина','кварц','мрамор','баскетбол','магазин','юла','язва','аргумент','щавель','автобус','город','парковка','школа','яблоко','банан','человек','роща','роза','машина','победа','поражение','шишка','поле','футбол','герой']

root = Tk()
root.geometry('800x500')
root.configure(bg='yellow')
root.title('Виселица')

#На экране текст виселица
introlabel = Label(root,text='Виселица',font=('arial',35,'bold'),bg='yellow')
introlabel.place(x=300,y=0)
#На экране загаданное слово в виде вопросиков
wordlabel = Label(root,font=('arial',55,'bold'),bg='yellow')
wordlabel.place(x=240,y=150)
#На экране показано сколько у тебя осталось попыток
try1 = Label(root,font=('arial',25,'bold'),bg='yellow')
try1.place(x=575,y=75)
#Вывод в окне текст (ты выйграл) (ты проиграл)
ans = Label(root,font=('arial',25,'bold'),bg='yellow')
ans.place(x=250,y=450)


inpp = StringVar() # используется для быстрого редактирования текста 
input1 = Entry(root,font=('arial',25,'bold'),relief=RIDGE,bd=5,bg='white',justify='center',fg='black',textvariable=inpp)
input1.focus_set() #метод используется для установки фокуса на нужный виджет тогда и только тогда, когда основное окно сфокусировано
input1.place(x=210,y=250)
#textvariable - устанавливает привязку к элементу StringVar
#relief - стиль кнопки

bt1 = Button(root,text='Подтвердить',font=('arial',15,'bold'),width=15,bd=5,bg='red'
             ,command=chel)
bt1.place(x=300,y=350)
root.bind("<Return>",jj)


def rword():
    global ss,ll,ss1,n,ffdata,temps
    ss = random.choice(list1)
    ll = ["?" for i in ss]
    ss1 = len(ss)
    n = ss1
    temps = ss
    try1.configure(text='Попыток = {}'.format(n))
    ffdata = ''
    for i in ll:
        ffdata += i+' '
    wordlabel.configure(text=ffdata)
    ans.configure(text='')


rword()
root.mainloop()