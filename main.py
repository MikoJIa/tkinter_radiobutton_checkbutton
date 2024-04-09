from tkinter import *

window = Tk()
window.geometry('400x500+500+500')
window.title('Графическое приложение')

levels = {
    1: 'Легкий',
    2: 'Средний',
    3: 'Тяжелый'
}

choose_race = {
    1: 'Эльфов',
    2: 'Людей',
    3: 'Орков'
}


def select_level():
    level = level_var.get()
    level_text.set(f'Вы выбрали {levels[level]} уровень')


def select_rasa():
    race = rasa_var.get()
    rasa_text.set(f'Вы выбрали расу {choose_race[race]}')


level_var = IntVar()
level_text = StringVar()

rasa_var = IntVar()
rasa_text = StringVar()

for level in levels:
    Radiobutton(window, text=levels[level], variable=level_var, value=level, command=select_level,
                font=('Arial', 12, 'bold')).pack()

Label(window, textvariable=level_text, font=('Arial', 15)).pack()

for race in choose_race:
    Radiobutton(window, text=choose_race[race], variable=rasa_var, value=race, command=select_rasa, font=('Arial', 12, 'bold')).pack()

Label(window, textvariable=rasa_text, font=('Arial', 15)).pack()

majority_value = StringVar()
majority_value.set('No')
follow_value = IntVar()

def select_all():
    for check in [majority, follow]:
        check.select()


def deselect_all():
    for check in [majority, follow]:
        check.deselect()


def switch_all():
    for check in [majority, follow]:
        check.toggle()


def show():
    print('Флажок 18', majority_value.get())
    print('Флажок follow', follow_value.get())


majority = Checkbutton(window, text='Вам исполнилось 18 лет?', width=20, font=('Arial', 15),
                       variable=majority_value,
                       offvalue='No', onvalue='Yes')
majority.pack()

follow = Checkbutton(window, text='Подписатся на канал', indicatoron=0, width=20, font=('Arial', 15),
                     variable=follow_value,
                     offvalue=0, onvalue=1
                     )
follow.pack()

btn = Button(window, text='select_all', command=select_all, width=20, height=1, font=('Arial', 15))
btn.pack()

btn = Button(window, text='deselect_all', command=deselect_all, width=20, height=1, font=('Arial', 15))
btn.pack()

btn = Button(window, text='switch_all', command=switch_all, width=20, height=1, font=('Arial', 15)).pack()

btn = Button(window, text='show', command=show).pack()

window.mainloop()
