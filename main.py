import tkinter as tk
from tkinter import ttk
import os

window = tk.Tk()

window.title('GameBox')
window.geometry('600x560')

gamename = tk.StringVar()
l = tk.Label(window, textvariable=gamename, font=('等线', 20), width=40, height=3)
l.place(x=0,y=0,anchor='nw')
canvas = tk.Canvas(window,bg='gray', height=500, width=600)
gamename.set('GameBox')

image_file_plane = tk.PhotoImage(file='plane.gif')
image_plane = canvas.create_image(0, 0, anchor='nw',image=image_file_plane)
image_file_chess = tk.PhotoImage(file='chess.gif')
image_chess = canvas.create_image(0, 100, anchor='nw',image=image_file_chess)  
image_file_snake = tk.PhotoImage(file='snake.gif')
image_snake = canvas.create_image(0, 200, anchor='nw',image=image_file_snake) 
image_file_sweep = tk.PhotoImage(file='minesweep.gif')
image_sweep = canvas.create_image(0, 300, anchor='nw',image=image_file_sweep)   
image_file_exit = tk.PhotoImage(file='exit.gif')
image_exit = canvas.create_image(0, 400, anchor='nw',image=image_file_exit)  
canvas.place(x=0,y=60)

def click_button1():
    gamename.set('正在运行游戏：飞机大战')
    os.system('python plane.py')
button_1 = tk.Button(window,bd=5,fg='purple',activebackground='gray',bg='white', text='飞机大战', font=('等线', 15), width=8, height=4, command=click_button1)
button_1.place(x=500,y=60)

def click_button2():
    gamename.set('正在运行游戏：五子棋')
    os.system('python chess.py')
button_2 = tk.Button(window,bd=5,fg='purple',activebackground='gray',bg='white', text='五子棋', font=('等线', 15), width=8, height=4, command=click_button2)
button_2.place(x=500,y=160)

def click_button3():
    gamename.set('正在运行游戏：贪吃蛇')
    os.system('python snake.py')
button_3 = tk.Button(window,bd=5,fg='purple',activebackground='gray',bg='white', text='贪吃蛇', font=('等线', 15), width=8, height=4, command=click_button3)
button_3.place(x=500,y=260)

def click_button4():
    gamename.set('正在运行游戏：扫雷')
    os.system('python minesweep.py')
button_4 = tk.Button(window,bd=5,fg='purple',activebackground='gray',bg='white', text='扫雷', font=('等线', 15), width=8, height=4, command=click_button4)
button_4.place(x=500,y=360)
button_5 = tk.Button(window,bd=5,fg='purple',activebackground='gray',bg='white', text='退出游戏盒', font=('等线', 15), width=8, height=4, command=window.quit)
button_5.place(x=500,y=460)

window.mainloop()
