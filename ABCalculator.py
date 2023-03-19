# A/B калькулятор

import tkinter as tk

# Функция закрытия программы
def do_close():
    root.destroy()
    
# Окно главного окна
root=tk.Tk()                                  # создание окна
root.geometry("280x300")                      # задание размеров окна
root.title("A/B калькулятор")                 # задание титульного названия окна  

# Добавление метки заголовка
lblTitle = tk.Label(text="A/B калькулятор", font = ('Helvetica', 16, 'bold'), fg = '#0000cc')            # создание названия заголовка (шрифт размером 16, жирный, цвет- темносиний)
lblTitle.place(x=55, y=20)

# Добавление кнопки "Рассчитать"
btnProcess = tk.Button(root,text="Рассчитать", font = ('Helvetica', 10, 'bold'))                         # создание кнопки "График Рассчитать"
btnProcess.place(x=25, y=250, width=90, height=30)                                                       # определение местоположения кнопки "График 1" и размеров кнопки)                                                                              # определение местоположения заголовка 

# Добавление кнопки закрытия программы
btnClose=tk.Button(root,text="Закрыть", font = ('Helvetica', 10, 'bold'), command=do_close)         # создание кнопки "Закрыть"
btnClose.place(x=160, y=250, width=90, height=30)                                                     # определение местоположения кнопки "Закрыть" и размеров кнопки)

# Запуск цикла mainloop
root.mainloop()
