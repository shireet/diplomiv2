from tkinter import *
from tkinter import ttk
from find import searcher


def Butt_comm(): #function that calls the function
    global yrs  #getting the values
    first_name = f.get()
    middle_name = m.get()
    last_name = l.get()
    day = d.get()
    month = mo.get()
    yearofbirth = y.get()
    type = nn.get()
    if type == "цветной":
        type = "color"
    if type == "чёрно-белый":
        type = "white"
    all = all_years.get()
    splits = all.split()

    value = searcher(splits, last_name, first_name, middle_name, day, month, yearofbirth, type)
    Label(root, text="Всё!", font=("Arial, 30")).place(x=230, y=400)
    if value == "error":
        Label(root, text="Произошла ошибка, убедитесь, что правильно ввели свои данные").place(x=100, y=300)


root = Tk()
root.geometry("600x500")

canvas = Canvas(root, width = 450, height = 500) #ну это картинка)
canvas.pack()
img = PhotoImage(file="pic.png")
canvas.create_image(20,1, anchor=NW, image=img)

#text
Label(root, text="Чтобы получить дипломы, введите свои данные").place(x=100, y=20)
Label(root, text="Фамилия").place(x=30, y=60)
Label(root, text="Имя").place(x=30, y=90)
Label(root, text="Отчество").place(x=30, y=120)
Label(root, text="Дата рождения ").place(x=30, y=150)
Label(root, text="(день/месяц/год)", font=("Arial",10)).place(x=30, y=170)
Label(root, text="Диплом").place(x=30, y=190)
Label(root, text="Год диплома").place(x=30, y=220)
Label(root, text="Введите все годы через пробел", font=("Arial", 10)).place(x=150, y=250)


#user input

f = Entry(root, width=15)
l = Entry(root, width=15)
m = Entry(root, width=15)
d = Entry(root, width=3)
mo = Entry(root, width=3)
y = Entry(root, width=6)

f.place(x=150, y=90)
m.place(x=150, y=120)
l.place(x=150, y=60)
d.place(x=150, y=150)
mo.place(x=190, y=150)
y.place(x=230, y=150)

#type
nn = StringVar()
tp = ttk.Combobox(root, width=10, textvariable=nn)
tp['values'] = ('цветной','чёрно-белый')
tp.place(x=150, y=190)
tp.current()

all_years = Entry(root, width=15)
all_years.place(x=150, y=220)

#execute button
Buttnstrt = Button(root, text="Найти", padx=40, command=Butt_comm).place(x=200, y=350)


root.mainloop()


