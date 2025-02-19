'''
Приложение состоит из двух файлов  main + ball
Использованы библиотеки - tkinter, random, math, numpy
Приложение имеет графический интерфейс и иллюстрирует одну из известных
физических задач - столкновение шаров в замкнутом объеме 

'''
import tkinter as tk
from random import *
from ball import *

checked_ball_pairs = []
balls_array = []
colors = ('red', 'green', 'blue', 'yellow', 'cyan', 'orange', 'brown', 'pink')

def click_sbutton():
    # рисуем шары
    n_balls =int(entry_N.get())   # количество
    for i in range(n_balls):
        balls_array.append(Ball(canv,
                            randint(50, 850),
                            randint(50, 550),
                            int(entry_R.get()),                  # радиус
                            randint(-5, 5),
                            randint(-5, 5),
                            choice(colors)))
   
    window.after(10, timer_cycle)

def click_cbutton():
    global balls_array, window, canv
    canv.delete("all")
    balls_array = []   

def create_window():
    global window, canv, entry_N, entry_R, s_button
    window = tk.Tk()
    window.geometry("{}x{}".format(window_width, window_height+30))
    canv = tk.Canvas(window, width=window_width, height=window_height)
    canv.pack()
    canv.create_rectangle(2, 1, window_width, window_height)
    
    label_R= tk.Label(text="                  Радиус  ")
    label_R.pack(side="left")

    entry_R = tk.Entry(window)
    entry_R.insert(0, 15)
    entry_R.pack(side="left")

    label_N= tk.Label(text="      Количество    ")
    label_N.pack(side="left")

    entry_N = tk.Entry(window)
    entry_N.insert(0, 3)
    entry_N.pack(side="left")
    
    s_button = tk.Button(window, text="  Добавить шары  " ,command=click_sbutton)
    s_button.pack(side="left")
    
    s_button = tk.Button(window, text="     Очистить     " ,command=click_cbutton)
    s_button.pack(side="left")
    
    click_sbutton()

def clear_checked_pairs():
    global checked_ball_pairs
    checked_ball_pairs = []
    

def ball_pair_checked(ball1, ball2):
    for ball_pair in checked_ball_pairs:
        if ball_pair[0] == ball1 and ball_pair[1] == ball2 or \
           ball_pair[0] == ball2 and ball_pair[1] == ball1:
            return True
        else:
            checked_ball_pairs.append((ball1, ball2))
            return False


def timer_cycle():
    global window, balls_array, entry_N, entry_R, s_button
    for ball in balls_array:
        ball.move()

        for wall in [(2, None), (window_width, None), (None, 2), (None, window_height)]:
            if ball.collide_with_wall(wall):
                ball.bounce_off_wall(wall)
                ball.check_glue_to_wall(wall)

        clear_checked_pairs()

        for ball2 in balls_array:
            if ball2 != ball and not ball_pair_checked(ball, ball2):
                if ball.collide_with_ball(ball2):
                    ball.bounce_off_ball(ball2)
    #s_button.state=["disabled"]
    #s_button.pack()
    window.after(10, timer_cycle)
    


window_width = 1000
window_height = 500

window = None
canv = None
entry_R= None   
entry_N= None   
s_button= None  
create_window()


window.mainloop()
