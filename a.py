from tkinter import *
from random import randint

window  = Tk()

window.title('Strong Password Generator')
window.geometry("500x300")

def new_rand():
	#Clear the entry box
	pw_entry.delete(0,END)
	pw_length = int(my_entry.get())
	my_pasword =  ''
	for x in range(pw_length):
		my_pasword+=chr(randint(33,126))

	pw_entry.insert(0,my_pasword)
def clipper():
	window.clipboard_clear()
	window.clipboard_append(pw_entry.get())
lf  = LabelFrame(window,text= "How many characters?")
lf.pack(pady=20)
my_entry = Entry(lf, font=("Helvetica", 24))
my_entry.pack(pady=20,padx=20)

pw_entry= Entry(window,text = '',font=("Helvetica",24),bd=0)
pw_entry.pack(pady=20)

my_frame = Frame(window)
my_frame.pack(pady=20)

my_button  = Button(my_frame,text="Generate Strong Password",command=new_rand)
my_button.grid(row=0,column=0, padx=10)
DEFAULT_BG_COLOR =my_button['bg']
clip_button = Button(my_frame,text="Copy to clipboard",command=clipper)
clip_button.grid(row=0,column=1,padx=10)

window.mainloop()