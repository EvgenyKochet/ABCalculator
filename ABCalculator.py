# A/B калькулятор

import tkinter as tk

# Функция закрытия программы
def do_close():
    root.destroy()

def popup_window():
    window=tk.Toplevel()                                  # создание дополнительного окна
    window.geometry("280x300")                            # задание размеров окна
    window.title("A/B результат")                         # задание титульного названия окна

    # Добавление кнопки закрытия окна
    btnClosePopup=tk.Button(window,text="Закрыть", font = ('Helvetica', 10, 'bold'), command=window.destroy)          
    btnClosePopup.place(x=160, y=250, width=90, height=30)                                                     
    
# Окно главного окна
root=tk.Tk()                                  # создание окна
root.geometry("280x300")                      # задание размеров окна
root.title("A/B калькулятор")                 # задание титульного названия окна  

# Добавление метки заголовка
lblTitle = tk.Label(text="A/B калькулятор", font = ('Helvetica', 16, 'bold'), fg = '#0000cc')            # создание названия заголовка (шрифт размером 16, жирный, цвет- темносиний)
lblTitle.place(x=55, y=20)

# Добавление метки заголовка контрольной группы
lblTitle1 = tk.Label(text="Контрольная группа", font = ('Helvetica', 10, 'bold'), fg = '#0066ff')            
lblTitle1.place(x=25, y=55)

# Добавление полей ввода контрольной группы
lblVisitors1 = tk.Label(text="Посетители:", font = ('Helvetica', 10, 'bold'))            
lblVisitors1.place(x=25, y=85)

entVisitors1 = tk.Entry(font = ('Helvetica', 10, 'bold'), justify='center')            
entVisitors1.place(x=115, y=85, width=90, height=20)
entVisitors1.insert(tk.END, '0')

lblConversions1 = tk.Label(text="Конверсии:", font = ('Helvetica', 10, 'bold'))            
lblConversions1.place(x=25, y=115)

entConversions1 = tk.Entry(font = ('Helvetica', 10, 'bold'), justify='center')            
entConversions1.place(x=115, y=115, width=90, height=20)
entConversions1.insert(tk.END, '0')


# Добавление метки заголовка тестовой группы
lblTitle2 = tk.Label(text="Тестовая группа", font = ('Helvetica', 10, 'bold'), fg = '#008800')            
lblTitle2.place(x=25, y=145)

# Добавление полей ввода тестовой группы
lblVisitors2 = tk.Label(text="Посетители:", font = ('Helvetica', 10, 'bold'))            
lblVisitors2.place(x=25, y=175)

entVisitors2 = tk.Entry(font = ('Helvetica', 10, 'bold'), justify='center')            
entVisitors2.place(x=115, y=175, width=90, height=20)
entVisitors2.insert(tk.END, '0')

lblConversions2 = tk.Label(text="Конверсии:", font = ('Helvetica', 10, 'bold'))            
lblConversions2.place(x=25, y=205)

entConversions2 = tk.Entry(font = ('Helvetica', 10, 'bold'), justify='center')            
entConversions2.place(x=115, y=205, width=90, height=20)
entConversions2.insert(tk.END, '0')










# Добавление кнопки "Рассчитать"
btnProcess = tk.Button(root,text="Рассчитать", font = ('Helvetica', 10, 'bold'), command=popup_window)                   # создание кнопки "График Рассчитать"
btnProcess.place(x=25, y=250, width=90, height=30)                                                                      # определение местоположения кнопки "График 1" и размеров кнопки)                                                                              # определение местоположения заголовка 

# Добавление кнопки закрытия программы
btnClose=tk.Button(root,text="Закрыть", font = ('Helvetica', 10, 'bold'), command=do_close)         # создание кнопки "Закрыть"
btnClose.place(x=160, y=250, width=90, height=30)                                                     # определение местоположения кнопки "Закрыть" и размеров кнопки)

# Запуск цикла mainloop
root.mainloop()
