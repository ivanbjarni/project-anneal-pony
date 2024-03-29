#!/usr/bin/python
# -*- coding: utf-8 -*-

# gotoclass.py
#from numpy import arange, sin, pi
from fjarmal import *
import wx

import matplotlib
matplotlib.use('WXAgg')

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
#from matplotlib.backends.backend_wx import NavigationToolbar2Wx
from matplotlib.figure import Figure

#heldur utan um teiknipanel fyrri myndræna framsetningu
drawingPanel = None
loanInfo = []

class PageOne(wx.Panel):
    def __init__(self, parent):
		wx.Panel.__init__(self, parent)

		vbox = wx.BoxSizer(wx.VERTICAL)

		insloanhbox1 = wx.BoxSizer(wx.HORIZONTAL)
		insloanhbox2 = wx.BoxSizer(wx.HORIZONTAL)
		insloanhbox3 = wx.BoxSizer(wx.HORIZONTAL)
		insloanhbox4 = wx.BoxSizer(wx.HORIZONTAL)
		insloanhbox5 = wx.BoxSizer(wx.HORIZONTAL)
		insloanhbox6 = wx.BoxSizer(wx.HORIZONTAL)
		insloanhbox7 = wx.BoxSizer(wx.HORIZONTAL)
		insloanhbox8 = wx.BoxSizer(wx.HORIZONTAL)

		insloantext1 = wx.StaticText(self, label='Nafn:'.decode('utf-8'))
		insloanname = wx.TextCtrl(self)
		insloanhbox1.Add(insloantext1, flag=wx.RIGHT, border=8)
		insloanhbox1.Add((80,1))
		insloanhbox1.Add(insloanname, proportion=1)

		insloantext2 = wx.StaticText(self, label='Höfuðstóll(kr.):'.decode('utf-8'))
		insloanamount = wx.TextCtrl(self)
		insloanhbox2.Add(insloantext2, flag=wx.RIGHT, border=8)
		insloanhbox2.Add((29,1))
		insloanhbox2.Add(insloanamount, proportion=1)

		insloantext3 = wx.StaticText(self, label='Vextir(%):'.decode('utf-8'))
		insloaninterest = wx.TextCtrl(self)
		insloanhbox3.Add(insloantext3, flag=wx.RIGHT, border=8)
		insloanhbox3.Add((59,1))
		insloanhbox3.Add(insloaninterest, proportion=1)

		insloantext4 = wx.StaticText(self, label='Fjöldi greiðslna:'.decode('utf-8'))
		insloannop = wx.TextCtrl(self)
		insloanhbox4.Add(insloantext4, flag=wx.RIGHT, border=8)
		insloanhbox4.Add((26,1))
		insloanhbox4.Add(insloannop, proportion=1)

 		insloaninfl = wx.CheckBox(self, label='Verðtrygging'.decode('utf-8'))
		insloanhbox5.Add(insloaninfl)

		insloansubmit = wx.Button(self, label='Bæta við'.decode('utf-8'), size=(70, 30))
		# Event listener for button
		insloansubmit.Bind(wx.EVT_BUTTON, lambda event: makeLoan(insloannop, insloaninfl, insloanname, insloanamount, insloaninterest, insloananswer, insloanlisti) )
		insloanhbox6.Add(insloansubmit)

		insloanlisti = wx.ListCtrl(self, -1, style=wx.LC_REPORT)
		insloanlisti.InsertColumn(0, 'Nafn:')
		insloanlisti.InsertColumn(1, 'Höfuðstóll'.decode('utf-8'))
		insloanlisti.InsertColumn(2, 'Vextir'.decode('utf-8'))
		insloanlisti.InsertColumn(3, 'Verðtrygging'.decode('utf-8'))
		insloanlisti.InsertColumn(4, 'Greiðslu fjöldi'.decode('utf-8'))
		insloanlisti.SetColumnWidth(0, 160)
		insloanlisti.SetColumnWidth(1, 153)
		insloanlisti.SetColumnWidth(2, 75)
		insloanlisti.SetColumnWidth(3, 90)
		insloanlisti.SetColumnWidth(4, 100)
		insloanhbox7.Add(insloanlisti, 1, wx.EXPAND | wx.ALL, 3)

		insloananswer = wx.StaticText(self, label='Fylltu út í reitina og ýttu á bæta við'.decode('utf-8'))
		insloanhbox8.Add(insloananswer)

		vbox.Add(insloanhbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		vbox.Add(insloanhbox2, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		vbox.Add(insloanhbox3, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		vbox.Add(insloanhbox4, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		vbox.Add(insloanhbox5, flag=wx.LEFT, border=10)
		vbox.Add(insloanhbox6, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		vbox.Add((-1, 10))
		vbox.Add(insloanhbox8, flag=wx.ALIGN_LEFT|wx.LEFT, border=10)
		vbox.Add((-1, 10))
		vbox.Add(insloanhbox7, flag=wx.ALIGN_LEFT|wx.LEFT, border=10)

		self.SetSizer(vbox)


class PageTwo(wx.Panel):
    def __init__(self, parent):
		wx.Panel.__init__(self, parent)

		vbox = wx.BoxSizer(wx.VERTICAL)

		insacchbox1 = wx.BoxSizer(wx.HORIZONTAL)
		insacchbox2 = wx.BoxSizer(wx.HORIZONTAL)
		insacchbox3 = wx.BoxSizer(wx.HORIZONTAL)
		insacchbox4 = wx.BoxSizer(wx.HORIZONTAL)
		insacchbox5 = wx.BoxSizer(wx.HORIZONTAL)
		insacchbox6 = wx.BoxSizer(wx.HORIZONTAL)
		insacchbox7 = wx.BoxSizer(wx.HORIZONTAL)
		insacchbox8 = wx.BoxSizer(wx.HORIZONTAL)
		insacchbox9 = wx.BoxSizer(wx.HORIZONTAL)

		insacctext1 = wx.StaticText(self, label='Nafn:'.decode('utf-8'))
		insaccname = wx.TextCtrl(self)
		insacchbox1.Add(insacctext1, flag=wx.RIGHT, border=8)
		insacchbox1.Add((80,1))
		insacchbox1.Add(insaccname, proportion=1)

		insacctext2 = wx.StaticText(self, label='Höfuðstóll(kr.):'.decode('utf-8'))
		insaccamount = wx.TextCtrl(self)
		insacchbox2.Add(insacctext2, flag=wx.RIGHT, border=8)
		insacchbox2.Add((29,1))
		insacchbox2.Add(insaccamount, proportion=1)

		insacctext3 = wx.StaticText(self, label='Vextir(%):'.decode('utf-8'))
		insaccinterest = wx.TextCtrl(self)
		insacchbox3.Add(insacctext3, flag=wx.RIGHT, border=8)
		insacchbox3.Add((59,1))
		insacchbox3.Add(insaccinterest, proportion=1)

		insacctext4 = wx.StaticText(self, label='Binditími(mán.):'.decode('utf-8'))
		insaccreq = wx.TextCtrl(self)
		insacchbox4.Add(insacctext4, flag=wx.RIGHT, border=8)
		insacchbox4.Add((23,1))
		insacchbox4.Add(insaccreq, proportion=1)

 		insaccinfl = wx.CheckBox(self, label='Verðtrygging'.decode('utf-8'))
		insacchbox5.Add(insaccinfl)

		insacctext5 = wx.StaticText(self, label='Sniðmát: '.decode('utf-8'))
		acctypelist = readAccountTypes()
		accnamelist = []
		for a in acctypelist:
			accnamelist.append(a.name)
		insaccpresets = wx.ComboBox(self, style = wx.CB_READONLY, choices= accnamelist)
		insaccpresets.Bind(wx.EVT_COMBOBOX, lambda event: insfields(insaccpresets, insaccname, insaccinterest, insaccreq, insaccinfl, acctypelist) )
		insacchbox6.Add(insacctext5)
		insacchbox6.Add(insaccpresets)

		insaccsubmit = wx.Button(self, label='Bæta við'.decode('utf-8'), size=(70, 30))
		# Event listener for button
		insaccsubmit.Bind(wx.EVT_BUTTON, lambda event: makeAccount( insaccname, insaccamount, insaccinterest, insaccreq, insaccinfl, insaccanswer, insacclisti ) )
			#insacreq, insaccinfl, insaccname, insaccamount, insaccinterest, loans) )
		insacchbox7.Add(insaccsubmit)

		insacclisti = wx.ListCtrl(self, -1, style=wx.LC_REPORT)
		insacclisti.InsertColumn(0, 'Nafn')
		insacclisti.InsertColumn(1, 'Höfuðstóll'.decode('utf-8'))
		insacclisti.InsertColumn(2, 'Vextir'.decode('utf-8'))
		insacclisti.InsertColumn(3, 'Verðtrygging'.decode('utf-8'))
		insacclisti.InsertColumn(4, 'Binditími'.decode('utf-8'))
		insacclisti.SetColumnWidth(0, 160)
		insacclisti.SetColumnWidth(1, 153)
		insacclisti.SetColumnWidth(2, 75)
		insacclisti.SetColumnWidth(3, 90)
		insacclisti.SetColumnWidth(4, 100)
		insacchbox8.Add(insacclisti, 1, wx.EXPAND | wx.ALL, 3)

		insaccanswer = wx.StaticText(self, label='Fylltu út í reitina og ýttu á bæta við'.decode('utf-8'))
		insacchbox9.Add(insaccanswer)

		vbox.Add(insacchbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		vbox.Add(insacchbox2, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		vbox.Add(insacchbox3, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		vbox.Add(insacchbox4, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		vbox.Add(insacchbox5, flag=wx.LEFT, border=10)
		vbox.Add(insacchbox6, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		vbox.Add((-1, 10))
		vbox.Add(insacchbox9, flag=wx.ALIGN_LEFT|wx.LEFT, border=10)
		vbox.Add((-1, 10))
		vbox.Add(insacchbox7, flag=wx.ALIGN_LEFT|wx.LEFT, border=10)
		vbox.Add(insacchbox8, flag=wx.ALIGN_LEFT|wx.LEFT, border=10)


		self.SetSizer(vbox)


class PageThree(wx.Panel):
    def __init__(self, parent):
		wx.Panel.__init__(self, parent)

		global loanInfo

		vbox = wx.BoxSizer(wx.VERTICAL)

		calcloanhbox1 = wx.BoxSizer(wx.HORIZONTAL)
		calcloanhbox2 = wx.BoxSizer(wx.HORIZONTAL)
		calcloanhbox3 = wx.BoxSizer(wx.HORIZONTAL)
		calcloanhbox4 = wx.BoxSizer(wx.HORIZONTAL)
		calcloanhbox5 = wx.BoxSizer(wx.HORIZONTAL)

		calcloantext1 = wx.StaticText(self, label='Mánaðarleg greiðsla(kr.):'.decode('utf-8'))
		calcloanpayment = wx.TextCtrl(self)
		calcloanhbox1.Add(calcloantext1, flag=wx.RIGHT, border=8)
		calcloanhbox1.Add(calcloanpayment, proportion=1)
		
		calcloantext2 = wx.StaticText(self, label='Hversu lengi(mán.):'.decode('utf-8'))
		calcloantime = wx.TextCtrl(self)
		calcloanhbox2.Add(calcloantext2, flag=wx.RIGHT, border=8)
		calcloanhbox2.Add((27,1))
		calcloanhbox2.Add(calcloantime, proportion=1)

		calcloantext3 = wx.StaticText(self, label='Verðbólgu tímabil:'.decode('utf-8'))
		calcloantext4 = wx.StaticText(self, label='Frá:'.decode('utf-8'))
		calcloantext5 = wx.StaticText(self, label=' Til:'.decode('utf-8'))
		infllist = makeMonths()
		calcloaninfltime1 = wx.ComboBox(self, style = wx.CB_READONLY, choices= infllist)
		calcloaninfltime2 = wx.ComboBox(self, style = wx.CB_READONLY, choices= infllist)
		calcloaninfltime1.SetSelection(12)
		calcloaninfltime2.SetSelection(0)
		calcloanhbox3.Add(calcloantext3, flag=wx.RIGHT, border=8)
		calcloanhbox3.Add(calcloantext4, flag=wx.RIGHT, border=8)
		calcloanhbox3.Add(calcloaninfltime1, proportion=1)
		calcloanhbox3.Add(calcloantext5, flag=wx.RIGHT, border=8)
		calcloanhbox3.Add(calcloaninfltime2, proportion=1)

		calcloansubmit = wx.Button(self, label='Reikna', size=(70, 30))
		calcloansubmit.Bind(wx.EVT_BUTTON, lambda event: calcBestWayToPayLoan( calcloanpayment, calcloantime, calcloaninfltime1, calcloaninfltime2, drawingPanel, False, calcloananswer ) )
		calcloanhbox4.Add(calcloansubmit, flag=wx.LEFT|wx.BOTTOM, border=5)

		calcloananswer = wx.StaticText(self, label='Fylltu út í reitina og ýttu á reikna'.decode('utf-8'))
		calcloanhbox5.Add(calcloananswer)

		loanInfo.append(calcloanpayment)
		loanInfo.append(calcloantime)
		#loanInfo.append(calcloaninfltime)
		loanInfo.append(calcloananswer)

		vbox.Add(calcloanhbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		vbox.Add(calcloanhbox2, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		vbox.Add(calcloanhbox3, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		vbox.Add((-1, 10))
		vbox.Add(calcloanhbox4, flag=wx.ALIGN_RIGHT|wx.RIGHT, border=10)
		vbox.Add(calcloanhbox5, flag=wx.ALIGN_LEFT|wx.LEFT, border=10)

		self.SetSizer(vbox)

class PageFour(wx.Panel):
    def __init__(self, parent):
		wx.Panel.__init__(self, parent)

		vbox = wx.BoxSizer(wx.VERTICAL)

		calcacc1hbox1 = wx.BoxSizer(wx.HORIZONTAL)
		calcacc1hbox2 = wx.BoxSizer(wx.HORIZONTAL)
		calcacc1hbox3 = wx.BoxSizer(wx.HORIZONTAL)
		calcacc1hbox4 = wx.BoxSizer(wx.HORIZONTAL)
		calcacc1hbox5 = wx.BoxSizer(wx.HORIZONTAL)

		calcacc1text1 = wx.StaticText(self, label='Mánaðarleg greiðsla(kr.):'.decode('utf-8'))
		calcacc1payment = wx.TextCtrl(self)
		calcacc1hbox1.Add(calcacc1text1, flag=wx.RIGHT, border=8)
		calcacc1hbox1.Add((11,1))
		calcacc1hbox1.Add(calcacc1payment, proportion=1)

		calcacc1text2 = wx.StaticText(self, label='Hvað viltu spara mikið(kr.):'.decode('utf-8'))
		calcacc1amount = wx.TextCtrl(self)
		calcacc1hbox2.Add(calcacc1text2, flag=wx.RIGHT, border=8)
		calcacc1hbox2.Add(calcacc1amount, proportion=1)

		calcacc1text3 = wx.StaticText(self, label='Verðbólgu tímabil:'.decode('utf-8'))
		calcacc1text4 = wx.StaticText(self, label='Frá:'.decode('utf-8'))
		calcacc1text5 = wx.StaticText(self, label=' Til:'.decode('utf-8'))
		infllist = makeMonths()
		calcacc1infltime1 = wx.ComboBox(self, style = wx.CB_READONLY, choices= infllist)
		calcacc1infltime2 = wx.ComboBox(self, style = wx.CB_READONLY, choices= infllist)
		calcacc1infltime1.SetSelection(12)
		calcacc1infltime2.SetSelection(0)
		calcacc1hbox3.Add(calcacc1text3, flag=wx.RIGHT, border=8)
		calcacc1hbox3.Add(calcacc1text4, flag=wx.RIGHT, border=8)
		calcacc1hbox3.Add(calcacc1infltime1, proportion=1)
		calcacc1hbox3.Add(calcacc1text5, flag=wx.RIGHT, border=8)
		calcacc1hbox3.Add(calcacc1infltime2, proportion=1)

		calcacc1submit = wx.Button(self, label='Reikna', size=(70, 30))
		calcacc1submit.Bind(wx.EVT_BUTTON, lambda event: calcBestWayToPayacc1( calcacc1payment, calcacc1amount, calcacc1infltime1, calcacc1infltime2, drawingPanel, calcacc1answer ) )
		calcacc1hbox4.Add(calcacc1submit, flag=wx.LEFT|wx.BOTTOM, border=5)

		calcacc1answer = wx.StaticText(self, label='Fylltu út í reitina og ýttu á reikna'.decode('utf-8'))
		calcacc1hbox5.Add(calcacc1answer)

		vbox.Add(calcacc1hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		vbox.Add(calcacc1hbox2, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		vbox.Add(calcacc1hbox3, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		vbox.Add((-1, 10))
		vbox.Add(calcacc1hbox4, flag=wx.ALIGN_RIGHT|wx.RIGHT, border=10)
		vbox.Add(calcacc1hbox5, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

		self.SetSizer(vbox)

class PageFive(wx.Panel):
    def __init__(self, parent):
		wx.Panel.__init__(self, parent)

		vbox = wx.BoxSizer(wx.VERTICAL)

		calcacc2hbox1 = wx.BoxSizer(wx.HORIZONTAL)
		calcacc2hbox2 = wx.BoxSizer(wx.HORIZONTAL)
		calcacc2hbox3 = wx.BoxSizer(wx.HORIZONTAL)
		calcacc2hbox4 = wx.BoxSizer(wx.HORIZONTAL)
		calcacc2hbox5 = wx.BoxSizer(wx.HORIZONTAL)

		calcacc2text1 = wx.StaticText(self, label='Mánaðarleg greiðsla(kr.):'.decode('utf-8'))
		calcacc2payment = wx.TextCtrl(self)
		calcacc2hbox1.Add(calcacc2text1, flag=wx.RIGHT, border=8)
		calcacc2hbox1.Add((21,1))
		calcacc2hbox1.Add(calcacc2payment, proportion=1)

		calcacc2text2 = wx.StaticText(self, label='Hvað viltu spara lengi(mán.):'.decode('utf-8'))
		calcacc2time = wx.TextCtrl(self)
		calcacc2hbox2.Add(calcacc2text2, flag=wx.RIGHT, border=8)
		calcacc2hbox2.Add(calcacc2time, proportion=1)

		calcacc2text3 = wx.StaticText(self, label='Verðbólgu tímabil:'.decode('utf-8'))
		calcacc2text4 = wx.StaticText(self, label='Frá:'.decode('utf-8'))
		calcacc2text5 = wx.StaticText(self, label=' Til:'.decode('utf-8'))
		infllist = makeMonths()
		calcacc2infltime1 = wx.ComboBox(self, style = wx.CB_READONLY, choices= infllist)
		calcacc2infltime2 = wx.ComboBox(self, style = wx.CB_READONLY, choices= infllist)
		calcacc2infltime1.SetSelection(12)
		calcacc2infltime2.SetSelection(0)
		calcacc2hbox3.Add(calcacc2text3, flag=wx.RIGHT, border=8)
		calcacc2hbox3.Add(calcacc2text4, flag=wx.RIGHT, border=8)
		calcacc2hbox3.Add(calcacc2infltime1, proportion=1)
		calcacc2hbox3.Add(calcacc2text5, flag=wx.RIGHT, border=8)
		calcacc2hbox3.Add(calcacc2infltime2, proportion=1)

		calcacc2submit = wx.Button(self, label='Reikna', size=(70, 30))
		calcacc2submit.Bind(wx.EVT_BUTTON, lambda event: calcBestWayToPayacc2( calcacc2payment, calcacc2time, calcacc2infltime1, calcacc2infltime2, drawingPanel, calcacc2answer ) )
		calcacc2hbox4.Add(calcacc2submit, flag=wx.LEFT|wx.BOTTOM, border=5)

		calcacc2answer = wx.StaticText(self, label='Fylltu út í reitina og ýttu á reikna'.decode('utf-8'))
		calcacc2hbox5.Add(calcacc2answer)

		vbox.Add(calcacc2hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		vbox.Add(calcacc2hbox2, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		vbox.Add(calcacc2hbox3, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		vbox.Add((-1, 10))
		vbox.Add(calcacc2hbox4, flag=wx.ALIGN_RIGHT|wx.RIGHT, border=10)
		vbox.Add(calcacc2hbox5, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

		self.SetSizer(vbox)

class PageSix(wx.Panel):
	def __init__(self, parent):
		wx.Panel.__init__(self, parent)

		global loanInfo
		#vbox = wx.BoxSizer(wx.VERTICAL)

		self.figure = Figure()
		self.axes = self.figure.add_subplot(111)
		self.canvas = FigureCanvas(self, -1, self.figure)
		self.sizer = wx.BoxSizer(wx.VERTICAL)
		self.sizer.Add(self.canvas, 1, wx.LEFT | wx.TOP | wx.GROW)

#		calcloansubmit = wx.Button(self, label='Reikna', size=(70, 30))
#		calcloansubmit.Bind(wx.EVT_BUTTON, lambda event: calcBestWayToPayLoan( loanInfo[0], loanInfo[1], loanInfo[2], drawingPanel, True, loanInfo[3] ) )
#		self.sizer.Add(calcloansubmit, flag=wx.LEFT|wx.BOTTOM, border=5)

		self.SetSizer(self.sizer)
		self.Fit()

	def drawLoans(self, plotAll, minTime, maxTime, xList, yList, clear):
		if(clear):
			self.axes.clear()
		if not plotAll:
			tempX = []
			tempY = []
			for i in range(0, maxTime+1):
				try:
					tempX.append(copy.deepcopy(xList[i]))
					tempY.append(copy.deepcopy(yList[i]))
				except:
					tempX.append(copy.deepcopy(xList[len(xList)-1]))
					tempY.append(copy.deepcopy(yList[len(yList)-1]))
			xList[:] = []
			yList[:] = []
			for i in range(0, maxTime+1):
				if(i < minTime):
					try:
						xList.append(tempX[minTime] + minTime)
						yList.append(tempY[minTime])
					except:
						xList.append(0)
						yList.append(0)
				else:
					xList.append(tempX[i] + minTime)
					yList.append(tempY[i])
		self.axes.set_xlabel('Mánuðir'.decode('utf-8'))
		self.axes.set_ylabel('Höfuðstóll'.decode('utf-8'))
		self.axes.plot(xList, yList)
		self.axes.set_xlim(left=1)
		self.axes.set_ylim(bottom=0)
		self.axes.set_autoscale_on(True)
		self.canvas.draw()
		self.canvas.Refresh()

	def drawAccounts(self, xList, yList):
		self.axes.clear()
		self.axes.set_xlabel('Mánuðir'.decode('utf-8'))
		self.axes.set_ylabel('Höfuðstóll'.decode('utf-8'))
		self.axes.plot(xList, yList)
		self.axes.set_xlim(left=1)
		self.axes.set_ylim(bottom=0)
		self.axes.set_autoscale_on(True)
		self.canvas.draw()
		self.canvas.Refresh()


class MainFrame(wx.Frame):
    def __init__(self):
		wx.Frame.__init__(self, None, title="Moneyspender 3000", size=(640, 500))

		mainPanel = wx.Panel(self)
		nb = wx.Notebook(mainPanel)

		page1 = PageOne(nb)
		page2 = PageTwo(nb)
		page3 = PageThree(nb)
		page4 = PageFour(nb)
		page5 = PageFive(nb)
		global drawingPanel 
		drawingPanel = PageSix(nb)

		nb.AddPage(page1, "Bæta við lánum".decode('utf-8'))
		nb.AddPage(page2, "Bæta við reikningum".decode('utf-8'))
		nb.AddPage(page3, "Reikna Lán".decode('utf-8'))
		nb.AddPage(page4, "Reikna Sparnað 1".decode('utf-8'))
		nb.AddPage(page5, "Reikna Sparnað 2".decode('utf-8'))
		nb.AddPage(drawingPanel, "Sjá myndrænt".decode('utf-8'))

		sizer = wx.BoxSizer()
		sizer.Add(nb, 1, wx.EXPAND)
		mainPanel.SetSizer(sizer)

def initGui():
	app = wx.App()
	MainFrame().Show()
	app.MainLoop()
	
