import tkinter as tk
from tkinter import ttk
from tkinter import *
from pygame import mixer
from threading import *
import os, csv, random, webbrowser, sys

import customtkinter
from customtkinter import *
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


mixer.init()
root = customtkinter.CTk()
root.title("Xokas Sounds Desktop")
if sys.platform.startswith('win'):
    root.geometry('1130x700"')
else:
    root.geometry("1100x900")
root['background']='#856ff8'

imgbutton = [tk.PhotoImage(file="media/elxokasimage_128.png"), tk.PhotoImage(file="media/xokas-streamer-internet.png"), tk.PhotoImage(file="media/XokasMillonTwitch.png"), tk.PhotoImage(file="media/Xokas_noticia_normal.png"), tk.PhotoImage(file="media/elxokas-655x368.png")]

if sys.platform.startswith('win'):
	alto=900
	ancho=1400
else:
	alto=900
	ancho=1100

anchoalto="1100x900"
# Create A Main Frame
main_frame = customtkinter.CTkFrame(master=root,width=ancho,height=alto,corner_radius=10, border_color='light_color')
main_frame.place(x=0,y=0)
# Create A Canvas
my_canvas = Canvas(main_frame, width=ancho, height=alto)
my_canvas.place(x=0,y=0)
# Add A Scrollbar To The Canvas
my_scrollbar =  ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.place(x=ancho -15,y=0,height=alto)
# Configure The Canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
def _on_mouse_wheel(event):
    my_canvas.yview_scroll(-1 * int((event.delta / 120)), "units")
my_canvas.bind_all("<MouseWheel>", _on_mouse_wheel)
# Create ANOTHER Frame INSIDE the Canvas
second_frame = customtkinter.CTkFrame(my_canvas,width=ancho,height=alto)
second_frame.place(x=0,y=0)
# Add that New frame To a Window In The Canvas
my_canvas.create_window((0,0), window=second_frame, anchor="nw")

if sys.platform.startswith('win'):
    titleProgram = customtkinter.CTkLabel(second_frame, text = "Xokas Sounds Desktop", fg_color=("red", "#e3203d"), corner_radius=8, width=1100, height=60, text_font =("Helvetica", 22), text_color='#005213')

else:
    titleProgram = customtkinter.CTkLabel(second_frame, text = "Xokas Sounds Desktop", fg_color=("red", "#e3203d"), corner_radius=8, width=1075, height=60, text_font =("Helvetica", 22), text_color='#005213')

titleProgram.place(x = 5, y= 5)

icon = tk.PhotoImage(file="media/KStudios.png")
root.iconphoto(True, icon)

class XokasSoundC:
	def __init__(self, foto, Lx,Ly, labelText, Bx, By, labelWidth, sound):
		self.foto = foto
		self.labelText = labelText
		self.Lx = Lx
		self.Ly = Ly
		self.Bx = Bx
		self.By = By
		dir = os.getcwd()
		path = "media/elxokasimage_128.png"
		self.labelWidth = labelWidth
		self.sound = sound

		global second_frame
		global imgbutton
		colorsBorder = ['dark green','dark blue','#5c0099','#201e24','#541010']
		tmpB = colorsBorder
		random.shuffle(tmpB)
		colorsBorder = tmpB

		def soundsXokas(sound):
			dir = os.getcwd()
			mixer.music.load(dir+'/media/'+sound)
			mixer.music.play()

		def threading(work,sound):
			t1=Thread(target=work, args=(sound,))
			t1.start()

		def checkLetterSize(length):
			if length <15:
				return ('Helvetica', 14)
			if length < 20:
				return ('Helvetica', 12)
			else:
				return ('Helvetica',10)
		
		my_button = None
		randomNum = random.randint(0,4)
		my_button = customtkinter.CTkButton(master=second_frame, image=imgbutton[randomNum],command=lambda: threading(soundsXokas,self.sound), border_width=4, border_color=colorsBorder[randomNum], corner_radius=8, text= self.labelText, hover=True, hover_color='white', text_color='grey', compound='top', text_font=checkLetterSize(len(self.labelText)))
		my_button.place(x=self.Bx, y=self.By)


csv_file = "media/fileName-name.csv"
list_of_rows = []
with open(csv_file, 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = csv.reader(read_obj, delimiter=';')
    # Pass reader object to list() to get a list of lists
    list_of_rows = list(csv_reader)

list_of_XokasSoundC = []

def checkPos(x, length):
	pos = 0
	if length <20:
		pos = x
	else: 
		pos = x - 9/8*length
	return pos

def checkWidth(length):
	totalWidth = 0
	if length <20:
		totalWidth = 17
	if length >= 20:
		totalWidth = length
	return totalWidth

i_counter = 0

if sys.platform.startswith('win'):
	for y in range(90, 3900, 200):
		for x in range(35, 1000, 210):
			try:
				a = len(str(list_of_rows[i_counter][1]))
				posX = checkPos(x, a)
				totalWidth = checkWidth(a)
				instance = XokasSoundC("elxokasimage_128.png", posX,y+140, list_of_rows[i_counter][1], x, y, totalWidth, list_of_rows[i_counter][0])
				list_of_XokasSoundC.append(instance)
				i_counter += 1
			except Exception as e:
				alto=y
				second_frame.configure(height=y)
				break
    
else:
	for y in range(90, 3900, 200):
		for x in range(25, 1000, 200):
			try:
				a = len(str(list_of_rows[i_counter][1]))
				posX = checkPos(x, a)
				totalWidth = checkWidth(a)
				instance = XokasSoundC("elxokasimage_128.png", posX,y+140, list_of_rows[i_counter][1], x, y, totalWidth, list_of_rows[i_counter][0])
				list_of_XokasSoundC.append(instance)
				i_counter += 1
			except Exception as e:
				alto=y
				second_frame.configure(height=y)
				break

def callback(url):
   webbrowser.open_new_tab(url)
link1 = Label(second_frame, text="👉Página de mi GitHub",font=('Helveticabold', 15), fg='light blue', bg='grey', cursor="hand2")
link1.bind("<Button-1>", lambda e: callback("https://github.com/Kripta-Studios/"))

if sys.platform.startswith('win'):
    link1.place(x=0, y=alto+912)
else:
    link1.place(x=0, y=alto-29)


link2 = Label(second_frame, text="Página del Concepto original👈",font=('Helveticabold', 15), fg='light blue', bg='grey', cursor="hand2")
link2.bind("<Button-1>", lambda e: callback("https://github.com/Xatpy/SoundsTable/tree/master/ElXokas"))
if sys.platform.startswith('win'):
    link2.place(x=ancho-370, y=alto+912)
else:
    link2.place(x=ancho-327, y=alto-29)


root.resizable(False, False)
root.mainloop()
