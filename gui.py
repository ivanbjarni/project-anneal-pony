import math
from PIL import Image, ImageTk
from ttk import Frame, Style
from Tkinter import *
import Image

def goforthmygui():
	window = Tk()
	initui(window) 
	window.mainloop()

def initui(w):
	w.configure(background="#333333")
	w.wm_title("moneyspender gui")

	#------------------------------------------------------------------------------------------
	
	#setjum upp panels
	toppane = PanedWindow(w,bg="#444444")
	toppane.pack(side = TOP, fill=BOTH)
	bottompane = PanedWindow(w,bg="#555555")
	bottompane.pack(side = BOTTOM, fill=BOTH)

	leftpane = PanedWindow(toppane,bg="#777777")
	leftpane.pack(side = LEFT, fill=BOTH)

	#------------------------------------------------------------------------------------------

	#Left panelid
	#buttons

	loanbutton = Button(leftpane,text="Create Loan", command=lambda: printchar(entry.get()))
	loanbutton.pack(side = TOP,padx=5, pady=5)

	accobutton = Button(leftpane,text="Create Account", command=lambda: printchar(entry.get()))
	accobutton.pack(side = TOP,padx=5, pady=5)

	#loans
	timetext = Label(leftpane, text="How far ahead to calculate:",bg="#333333",fg="#EEEEEE")
	timetext.pack( side = TOP,padx=5, pady=5)

	timevar = StringVar(w)
	timevar.set("1 Month") # default value

	timeoption = OptionMenu(leftpane, timevar, "1 Month", "2 Months", "9001 months")
	timeoption.pack(side = TOP, padx=5, pady=5)

	#inflation

	infltext = Label(leftpane, text="Choose inflation period:",bg="#333333",fg="#EEEEEE")
	infltext.pack( side = TOP,padx=5, pady=5)

	inflvar = StringVar(w)
	inflvar.set("Dec 2013") # default value

	infloption = OptionMenu(leftpane, inflvar, "Jan 2014", "Dec 2013", "Nov 2013", "Oct 2013", "Sept 2013", "Aug 2013", "Jun 2013", "July 2013", "Apr 2013", "Mars 2013", "Feb 2013", "Jan 2013")
	infloption.pack(side = TOP, padx=5, pady=5,fill=X)

	#------------------------------------------------------------------------------------------

	#Synismynd 
	img = ImageTk.PhotoImage(Image.open("demo_line_chart.jpg"))
	demolabel = Label(toppane, image=img)
	demolabel.image = img
	demolabel.pack( side = RIGHT,padx=5, pady=5,)

	#------------------------------------------------------------------------------------------

	#Bottom panelid
	inputtext = Label(bottompane, text="Input",bg="#333333",fg="#EEEEEE")
	inputtext.pack( side = LEFT,padx=5, pady=5)

	inputentry = Entry(bottompane, bd =5)
	inputentry.pack(side = LEFT)

	inputbutton = Button(bottompane,text="Submit", command=lambda: printchar(entry.get()))
	inputbutton.pack(side = RIGHT,padx=5, pady=5)

	#------------------------------------------------------------------------------------------




goforthmygui()