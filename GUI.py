from tkinter import*
from tkinter import filedialog
from PIL import ImageTk, Image
import os

root = Tk()
root.geometry("600x400")

def Line4():
	os.system('python Indicator.py --model Line4.tflite')

def NG():
	program = filedialog.askopenfilename()
	label.config(text=program)
	os.system('"%s"' % program)

def Camera():
	os.system('python AdjustCamera.py')
	
	
	
button = Button(root,text = 'Line4 model', command=Line4)
button.pack(pady=20)

button2 = Button(root, text = 'Latest NG', command=NG)
button2.pack(pady=20)

button3 = Button(root, text = 'Adjust Camera', command=Camera)
button3.pack(pady=20)

label = Label(root, text="")
label.pack(pady=20)

root.mainloop()
