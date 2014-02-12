#!/usr/bin/python
# -*- coding: utf-8 -*-

# gotoclass.py
from fjarmal import *
import wx

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
		insloanhbox1.Add((58,1))
		insloanhbox1.Add(insloanname, proportion=1)

		insloantext2 = wx.StaticText(self, label='Höfuðstóll:'.decode('utf-8'))
		insloanamount = wx.TextCtrl(self)
		insloanhbox2.Add(insloantext2, flag=wx.RIGHT, border=8)
		insloanhbox2.Add((29,1))
		insloanhbox2.Add(insloanamount, proportion=1)

		insloantext3 = wx.StaticText(self, label='Vextir:'.decode('utf-8'))
		insloaninterest = wx.TextCtrl(self)
		insloanhbox3.Add(insloantext3, flag=wx.RIGHT, border=8)
		insloanhbox3.Add((56,1))
		insloanhbox3.Add(insloaninterest, proportion=1)

		insloantext4 = wx.StaticText(self, label='Fjöldi greiðslna:'.decode('utf-8'))
		insloannop = wx.TextCtrl(self)
		insloanhbox4.Add(insloantext4, flag=wx.RIGHT, border=8)
		insloanhbox4.Add((5,1))
		insloanhbox4.Add(insloannop, proportion=1)

 		insloaninfl = wx.CheckBox(self, label='Verðtrygging'.decode('utf-8'))
		insloanhbox5.Add(insloaninfl)

		insloansubmit = wx.Button(self, label='Bæta við'.decode('utf-8'), size=(70, 30))
		# Event listener for button
		insloansubmit.Bind(wx.EVT_BUTTON, lambda event: makeLoan(insloannop, insloaninfl, insloanname, insloanamount, insloaninterest, loans,insloanlisti) )
		insloanhbox6.Add(insloansubmit)

		insloanlisti = wx.ListCtrl(self, -1, style=wx.LC_REPORT)
		insloanlisti.InsertColumn(0, 'Nafn')
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

		insacctext1 = wx.StaticText(self, label='Nafn:'.decode('utf-8'))
		insaccname = wx.TextCtrl(self)
		insacchbox1.Add(insacctext1, flag=wx.RIGHT, border=8)
		insacchbox1.Add((58,1))
		insacchbox1.Add(insaccname, proportion=1)

		insacctext2 = wx.StaticText(self, label='Höfuðstóll:'.decode('utf-8'))
		insaccamount = wx.TextCtrl(self)
		insacchbox2.Add(insacctext2, flag=wx.RIGHT, border=8)
		insacchbox2.Add((29,1))
		insacchbox2.Add(insaccamount, proportion=1)

		insacctext3 = wx.StaticText(self, label='Vextir:'.decode('utf-8'))
		insaccinterest = wx.TextCtrl(self)
		insacchbox3.Add(insacctext3, flag=wx.RIGHT, border=8)
		insacchbox3.Add((56,1))
		insacchbox3.Add(insaccinterest, proportion=1)

		insacctext4 = wx.StaticText(self, label='Binditími:'.decode('utf-8'))
		insaccreq = wx.TextCtrl(self)
		insacchbox4.Add(insacctext4, flag=wx.RIGHT, border=8)
		insacchbox4.Add((37,1))
		insacchbox4.Add(insaccreq, proportion=1)

 		insaccinfl = wx.CheckBox(self, label='Verðtrygging'.decode('utf-8'))
		insacchbox5.Add(insaccinfl)

		insaccsubmit = wx.Button(self, label='Bæta við'.decode('utf-8'), size=(70, 30))
		# Event listener for button
		insaccsubmit.Bind(wx.EVT_BUTTON, lambda event: makeLoan(insacreq, insaccinfl, insaccname, insaccamount, insaccinterest, loans) )
		insacchbox6.Add(insaccsubmit)

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
		insacchbox7.Add(insacclisti, 1, wx.EXPAND | wx.ALL, 3)

		insaccanswer = wx.StaticText(self, label='Fylltu út í reitina og ýttu á bæta við'.decode('utf-8'))
		insacchbox8.Add(insaccanswer)

		vbox.Add(insacchbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		vbox.Add(insacchbox2, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		vbox.Add(insacchbox3, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		vbox.Add(insacchbox4, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		vbox.Add(insacchbox5, flag=wx.LEFT, border=10)
		vbox.Add(insacchbox6, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		vbox.Add(insacchbox8, flag=wx.ALIGN_LEFT|wx.LEFT, border=10)
		vbox.Add((-1, 10))
		vbox.Add(insacchbox7, flag=wx.ALIGN_LEFT|wx.LEFT, border=10)

		self.SetSizer(vbox)


class PageThree(wx.Panel):
    def __init__(self, parent):
		wx.Panel.__init__(self, parent)

		vbox = wx.BoxSizer(wx.VERTICAL)

		calcloanhbox1 = wx.BoxSizer(wx.HORIZONTAL)
		calcloanhbox2 = wx.BoxSizer(wx.HORIZONTAL)
		calcloanhbox3 = wx.BoxSizer(wx.HORIZONTAL)
		calcloanhbox4 = wx.BoxSizer(wx.HORIZONTAL)
		calcloanhbox5 = wx.BoxSizer(wx.HORIZONTAL)

		calcloantext1 = wx.StaticText(self, label='Mánaðarleg greiðsla:'.decode('utf-8'))
		calcloanpayment = wx.TextCtrl(self)
		calcloanhbox1.Add(calcloantext1, flag=wx.RIGHT, border=8)
		calcloanhbox1.Add(calcloanpayment, proportion=1)
		
		calcloantext2 = wx.StaticText(self, label='Hversu lengi:'.decode('utf-8'))
		calcloantime = wx.TextCtrl(self)
		calcloanhbox2.Add(calcloantext2, flag=wx.RIGHT, border=8)
		calcloanhbox2.Add((40,1))
		calcloanhbox2.Add(calcloantime, proportion=1)

		calcloantext3 = wx.StaticText(self, label='Verðbólgu tímabil:'.decode('utf-8'))
		calcloaninfltime = wx.ComboBox(self, style = wx.CB_READONLY, choices= ["Síðasta mánuð".decode('utf-8'),"Síðustu 2 mánuði".decode('utf-8'),"Síðasta hálfa árið".decode('utf-8'),"Síðasta árið".decode('utf-8'), "Síðustu 2 ár".decode('utf-8')])
		calcloaninfltime.SetSelection(1)
		calcloanhbox3.Add(calcloantext3, flag=wx.RIGHT, border=8)
		calcloanhbox3.Add(calcloaninfltime, proportion=1)

		calcloansubmit = wx.Button(self, label='Reikna', size=(70, 30))
		calcloansubmit.Bind(wx.EVT_BUTTON, lambda event: calcBestWayToPayLoan( calcloanpayment, calcloantime, calcloaninfltime ) )
		calcloanhbox4.Add(calcloansubmit, flag=wx.LEFT|wx.BOTTOM, border=5)

		calcloananswer = wx.StaticText(self, label='Fylltu út í reitina og ýttu á reikna'.decode('utf-8'))
		calcloanhbox5.Add(calcloananswer)

		vbox.Add(calcloanhbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		vbox.Add(calcloanhbox2, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		vbox.Add(calcloanhbox3, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		vbox.Add((-1, 10))
		vbox.Add(calcloanhbox4, flag=wx.ALIGN_RIGHT|wx.RIGHT, border=10)
		vbox.Add(calcloanhbox5, flag=wx.ALIGN_RIGHT|wx.RIGHT, border=10)

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

		calcacc1text1 = wx.StaticText(self, label='Mánaðarleg greiðsla:'.decode('utf-8'))
		calcacc1payment = wx.TextCtrl(self)
		calcacc1hbox1.Add(calcacc1text1, flag=wx.RIGHT, border=8)
		calcacc1hbox1.Add((11,1))
		calcacc1hbox1.Add(calcacc1payment, proportion=1)

		calcacc1text2 = wx.StaticText(self, label='Hvað viltu spara mikið:'.decode('utf-8'))
		calcacc1amount = wx.TextCtrl(self)
		calcacc1hbox2.Add(calcacc1text2, flag=wx.RIGHT, border=8)
		calcacc1hbox2.Add(calcacc1amount, proportion=1)

		calcacc1text3 = wx.StaticText(self, label='Verðbólgu tímabil:'.decode('utf-8'))
		calcacc1infltime = wx.ComboBox(self, style = wx.CB_READONLY, choices= ["Síðasta mánuð".decode('utf-8'),"Síðustu 2 mánuði".decode('utf-8'),"Síðasta hálfa árið".decode('utf-8'),"Síðasta árið".decode('utf-8'), "Síðustu 2 ár".decode('utf-8')])
		calcacc1infltime.SetSelection(1)
		calcacc1hbox3.Add(calcacc1text3, flag=wx.RIGHT, border=8)
		calcacc1hbox3.Add(calcacc1infltime, proportion=1)

		calcacc1submit = wx.Button(self, label='Reikna', size=(70, 30))
		calcacc1submit.Bind(wx.EVT_BUTTON, lambda event: calcBestWayToPayacc1( calcacc1payment, calcacc1time, calcacc1infltime ) )
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

		calcacc2text1 = wx.StaticText(self, label='Mánaðarleg greiðsla:'.decode('utf-8'))
		calcacc2payment = wx.TextCtrl(self)
		calcacc2hbox1.Add(calcacc2text1, flag=wx.RIGHT, border=8)
		calcacc2hbox1.Add((7,1))
		calcacc2hbox1.Add(calcacc2payment, proportion=1)

		calcacc2text2 = wx.StaticText(self, label='Hvað viltu spara lengi:'.decode('utf-8'))
		calcacc2time = wx.TextCtrl(self)
		calcacc2hbox2.Add(calcacc2text2, flag=wx.RIGHT, border=8)
		calcacc2hbox2.Add(calcacc2time, proportion=1)

		calcacc2text3 = wx.StaticText(self, label='Verðbólgu tímabil:'.decode('utf-8'))
		calcacc2infltime = wx.ComboBox(self, style = wx.CB_READONLY, choices= ["Síðasta mánuð".decode('utf-8'),"Síðustu 2 mánuði".decode('utf-8'),"Síðasta hálfa árið".decode('utf-8'),"Síðasta árið".decode('utf-8'), "Síðustu 2 ár".decode('utf-8')])
		calcacc2infltime.SetSelection(1)
		calcacc2hbox3.Add(calcacc2text3, flag=wx.RIGHT, border=8)
		calcacc2hbox3.Add(calcacc2infltime, proportion=1)

		calcacc2submit = wx.Button(self, label='Reikna', size=(70, 30))
		calcacc2submit.Bind(wx.EVT_BUTTON, lambda event: calcBestWayToPayLoan( payment, time, infltime ) )
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

		nb.AddPage(page1, "Bæta við lánum".decode('utf-8'))
		nb.AddPage(page2, "Bæta við reikningum".decode('utf-8'))
		nb.AddPage(page3, "Reikna Lán".decode('utf-8'))
		nb.AddPage(page4, "Reikna Sparnað 1".decode('utf-8'))
		nb.AddPage(page5, "Reikna Sparnað 2".decode('utf-8'))

		sizer = wx.BoxSizer()
		sizer.Add(nb, 1, wx.EXPAND)
		mainPanel.SetSizer(sizer)

#if __name__ == '__main__':
#    app = wx.App()
#    MainFrame().Show()
#    app.MainLoop()

def initGui():
	app = wx.App()
	MainFrame().Show()
	app.MainLoop()
	
