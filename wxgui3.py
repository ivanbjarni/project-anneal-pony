#!/usr/bin/python
# -*- coding: utf-8 -*-

# gotoclass.py
from fjarmal import *
import wx

class PageOne(wx.Panel):
    def __init__(self, parent):
		wx.Panel.__init__(self, parent)

		font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
		font.SetPointSize(9)

		vbox = wx.BoxSizer(wx.VERTICAL)

		hbox2 = wx.BoxSizer(wx.HORIZONTAL)
		st2 = wx.StaticText(self, label='Lán:'.decode('utf-8'))
		st2.SetFont(font)
		hbox2.Add(st2, flag=wx.RIGHT, border=8)
		vbox.Add(hbox2, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

		hbox21 = wx.BoxSizer(wx.HORIZONTAL)
		st21 = wx.StaticText(self, label='Nafn'.decode('utf-8'))
		st21.SetFont(font)
		hbox21.Add(st21, flag=wx.RIGHT, border=8)
		loanname = wx.TextCtrl(self)
		hbox21.Add(loanname, proportion=1)
		vbox.Add(hbox21, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

		hbox3 = wx.BoxSizer(wx.HORIZONTAL)
		st3 = wx.StaticText(self, label='Höfuðstóll'.decode('utf-8'))
		st3.SetFont(font)
		hbox3.Add(st3, flag=wx.RIGHT, border=8)
		loanamount = wx.TextCtrl(self)
		hbox3.Add(loanamount, proportion=1)
		vbox.Add(hbox3, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

		hbox4 = wx.BoxSizer(wx.HORIZONTAL)
		st4 = wx.StaticText(self, label='Vextir'.decode('utf-8'))
		st4.SetFont(font)
		hbox4.Add(st4, flag=wx.RIGHT, border=8)
		loaninterest = wx.TextCtrl(self)
		hbox4.Add(loaninterest, proportion=1)
		vbox.Add(hbox4, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

		hbox5 = wx.BoxSizer(wx.HORIZONTAL)
		st5 = wx.StaticText(self, label='Fjöldi greiðslna'.decode('utf-8'))
		st5.SetFont(font)
		hbox5.Add(st5, flag=wx.RIGHT, border=8)
		loannop = wx.TextCtrl(self)
		hbox5.Add(loannop, proportion=1)
		vbox.Add(hbox5, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		#png = wx.StaticBitmap(self, -1, wx.Bitmap("demo_line_chart.png", wx.BITMAP_TYPE_ANY))
		#hbox2.Add(png, flag=wx.RIGHT, border=8)
		
		vbox.Add((-1, 10))

		hbox4 = wx.BoxSizer(wx.HORIZONTAL)
 		loaninfl = wx.CheckBox(self, label='Verðtrygging'.decode('utf-8'))
		loaninfl.SetFont(font)
		hbox4.Add(loaninfl)
		vbox.Add(hbox4, flag=wx.LEFT, border=10)

		hbox5 = wx.BoxSizer(wx.HORIZONTAL)
		addloanbtn = wx.Button(self, label='Bæta við'.decode('utf-8'), size=(70, 30))
		hbox5.Add(addloanbtn)
		vbox.Add(hbox5, flag=wx.ALIGN_RIGHT|wx.RIGHT, border=10)
		# Event listener for button
		addloanbtn.Bind(wx.EVT_BUTTON, lambda event: makeLoan(loannop, loaninfl, loanname, loanamount, loaninterest, loans) )

		hbox6 = wx.BoxSizer(wx.HORIZONTAL)
		st6 = wx.StaticText(self, label='Núverandi Lán:'.decode('utf-8'))
		st6.SetFont(font)
		hbox6.Add(st6, flag=wx.RIGHT, border=8)
		loans = wx.ComboBox(self, style = wx.CB_READONLY)
		hbox6.Add(loans)
		vbox.Add(hbox6, flag=wx.ALIGN_LEFT|wx.LEFT, border=10)

		hbox7 = wx.BoxSizer(wx.HORIZONTAL)
		listi = wx.ListCtrl(self, -1, style=wx.LC_REPORT)
		listi.InsertColumn(0, 'Nafn')
		listi.InsertColumn(1, 'Höfuðstóll'.decode('utf-8'))
		listi.InsertColumn(2, 'Vextir'.decode('utf-8'))
		listi.InsertColumn(3, 'Verðtrygging'.decode('utf-8'))
		listi.InsertColumn(4, 'Greiðslu fjöldi'.decode('utf-8'))
		listi.SetColumnWidth(0, 160)
		listi.SetColumnWidth(1, 153)
		listi.SetColumnWidth(2, 75)
		listi.SetColumnWidth(3, 90)
		listi.SetColumnWidth(4, 100)
		hbox7.Add(listi, 1, wx.EXPAND | wx.ALL, 3)
		vbox.Add(hbox7, flag=wx.ALIGN_LEFT|wx.LEFT, border=10)

		self.SetSizer(vbox)


class PageTwo(wx.Panel):
    def __init__(self, parent):
		wx.Panel.__init__(self, parent)

		font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
		font.SetPointSize(9)

		vbox = wx.BoxSizer(wx.VERTICAL)

		hbox1 = wx.BoxSizer(wx.HORIZONTAL)
		st1 = wx.StaticText(self, label='Mánaðarleg greiðsla:'.decode('utf-8'))
		st1.SetFont(font)
		hbox1.Add(st1, flag=wx.RIGHT, border=8)
		payment = wx.TextCtrl(self)
		hbox1.Add(payment, proportion=1)
		vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

		hbox12 = wx.BoxSizer(wx.HORIZONTAL)
		st12 = wx.StaticText(self, label='Hversu lengi:'.decode('utf-8'))
		st12.SetFont(font)
		hbox12.Add(st12, flag=wx.RIGHT, border=8)
		time = wx.TextCtrl(self)
		hbox12.Add(time, proportion=1)
		vbox.Add(hbox12, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

		hbox13 = wx.BoxSizer(wx.HORIZONTAL)
		st13 = wx.StaticText(self, label='Verðbólgu tímabil:'.decode('utf-8'))
		st13.SetFont(font)
		hbox13.Add(st13, flag=wx.RIGHT, border=8)
		infltime = wx.ComboBox(self, style = wx.CB_READONLY, choices= ["Síðasta mánuð".decode('utf-8'),"Síðustu 2 mánuði".decode('utf-8'),"Síðasta hálfa árið".decode('utf-8'),"Síðasta árið".decode('utf-8'), "Síðustu 2 ár".decode('utf-8')])
		infltime.SetSelection(1)
		hbox13.Add(infltime, proportion=1)
		vbox.Add(hbox13, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

		vbox.Add((-1, 10))

		hbox11 = wx.BoxSizer(wx.HORIZONTAL)
		calcbtn = wx.Button(self, label='Reikna', size=(70, 30))
		hbox11.Add(calcbtn, flag=wx.LEFT|wx.BOTTOM, border=5)
		vbox.Add(hbox11, flag=wx.ALIGN_RIGHT|wx.RIGHT, border=10)
		calcbtn.Bind(wx.EVT_BUTTON, lambda event: calcBestWayToPayLoan( payment, time, infltime ) )

		self.SetSizer(vbox)

class PageThree(wx.Panel):
    def __init__(self, parent):
		wx.Panel.__init__(self, parent)

		font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
		font.SetPointSize(9)

		vbox = wx.BoxSizer(wx.VERTICAL)

		hbox2 = wx.BoxSizer(wx.HORIZONTAL)
		st2 = wx.StaticText(self, label='Reikningar:'.decode('utf-8'))
		st2.SetFont(font)
		hbox2.Add(st2, flag=wx.RIGHT, border=8)
		vbox.Add(hbox2, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

		hbox21 = wx.BoxSizer(wx.HORIZONTAL)
		st21 = wx.StaticText(self, label='Nafn'.decode('utf-8'))
		st21.SetFont(font)
		hbox21.Add(st21, flag=wx.RIGHT, border=8)
		accountname = wx.TextCtrl(self)
		hbox21.Add(accountname, proportion=1)
		vbox.Add(hbox21, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

		hbox3 = wx.BoxSizer(wx.HORIZONTAL)
		st3 = wx.StaticText(self, label='Höfuðstóll'.decode('utf-8'))
		st3.SetFont(font)
		hbox3.Add(st3, flag=wx.RIGHT, border=8)
		accountamount = wx.TextCtrl(self)
		hbox3.Add(accountamount, proportion=1)
		vbox.Add(hbox3, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

		hbox4 = wx.BoxSizer(wx.HORIZONTAL)
		st4 = wx.StaticText(self, label='Vextir'.decode('utf-8'))
		st4.SetFont(font)
		hbox4.Add(st4, flag=wx.RIGHT, border=8)
		accountinterest = wx.TextCtrl(self)
		hbox4.Add(accountinterest, proportion=1)
		vbox.Add(hbox4, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

		hbox5 = wx.BoxSizer(wx.HORIZONTAL)
		st5 = wx.StaticText(self, label='Bundin Tími'.decode('utf-8'))
		st5.SetFont(font)
		hbox5.Add(st5, flag=wx.RIGHT, border=8)
		accountnop = wx.TextCtrl(self)
		hbox5.Add(accountnop, proportion=1)
		vbox.Add(hbox5, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		#png = wx.StaticBitmap(self, -1, wx.Bitmap("demo_line_chart.png", wx.BITMAP_TYPE_ANY))
		#hbox2.Add(png, flag=wx.RIGHT, border=8)
		
		vbox.Add((-1, 10))

		hbox4 = wx.BoxSizer(wx.HORIZONTAL)
 		accountinfl = wx.CheckBox(self, label='Verðtrygging'.decode('utf-8'))
		accountinfl.SetFont(font)
		hbox4.Add(accountinfl)
		vbox.Add(hbox4, flag=wx.LEFT, border=10)

		hbox5 = wx.BoxSizer(wx.HORIZONTAL)
		addaccountbtn = wx.Button(self, label='Bæta við'.decode('utf-8'), size=(70, 30))
		hbox5.Add(addaccountbtn)
		vbox.Add(hbox5, flag=wx.ALIGN_RIGHT|wx.RIGHT, border=10)
		# Event listener for button
		addaccountbtn.Bind(wx.EVT_BUTTON, lambda event: makeaccount(accountnop, accountinfl, accountname, accountamount, accountinterest, accounts) )

		hbox6 = wx.BoxSizer(wx.HORIZONTAL)
		st6 = wx.StaticText(self, label='Núverandi Lán:'.decode('utf-8'))
		st6.SetFont(font)
		hbox6.Add(st6, flag=wx.RIGHT, border=8)
		accounts = wx.ComboBox(self, style = wx.CB_READONLY)
		hbox6.Add(accounts)
		vbox.Add(hbox6, flag=wx.ALIGN_LEFT|wx.LEFT, border=10)

		hbox7 = wx.BoxSizer(wx.HORIZONTAL)
		listi = wx.ListCtrl(self, -1, style=wx.LC_REPORT)
		listi.InsertColumn(0, 'Nafn')
		listi.InsertColumn(1, 'Höfuðstóll'.decode('utf-8'))
		listi.InsertColumn(2, 'Vextir'.decode('utf-8'))
		listi.InsertColumn(3, 'Verðtrygging'.decode('utf-8'))
		listi.InsertColumn(4, 'Bundin tími'.decode('utf-8'))
		listi.SetColumnWidth(0, 160)
		listi.SetColumnWidth(1, 153)
		listi.SetColumnWidth(2, 75)
		listi.SetColumnWidth(3, 90)
		listi.SetColumnWidth(4, 100)
		hbox7.Add(listi, 1, wx.EXPAND | wx.ALL, 3)
		vbox.Add(hbox7, flag=wx.ALIGN_LEFT|wx.LEFT, border=10)

		self.SetSizer(vbox)


class PageFour(wx.Panel):
    def __init__(self, parent):
		wx.Panel.__init__(self, parent)

		font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
		font.SetPointSize(9)

		vbox = wx.BoxSizer(wx.VERTICAL)

		hbox1 = wx.BoxSizer(wx.HORIZONTAL)
		st1 = wx.StaticText(self, label='Mánaðarleg greiðsla:'.decode('utf-8'))
		st1.SetFont(font)
		hbox1.Add(st1, flag=wx.RIGHT, border=8)
		accpayment1 = wx.TextCtrl(self)
		hbox1.Add(accpayment1, proportion=1)
		vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

		hbox12 = wx.BoxSizer(wx.HORIZONTAL)
		st12 = wx.StaticText(self, label='Hvað viltu spara mikið:'.decode('utf-8'))
		st12.SetFont(font)
		hbox12.Add(st12, flag=wx.RIGHT, border=8)
		accamount = wx.TextCtrl(self)
		hbox12.Add(accamount, proportion=1)
		vbox.Add(hbox12, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

		hbox13 = wx.BoxSizer(wx.HORIZONTAL)
		st13 = wx.StaticText(self, label='Verðbólgu tímabil:'.decode('utf-8'))
		st13.SetFont(font)
		hbox13.Add(st13, flag=wx.RIGHT, border=8)
		accinfltime = wx.ComboBox(self, style = wx.CB_READONLY, choices= ["Síðasta mánuð".decode('utf-8'),"Síðustu 2 mánuði".decode('utf-8'),"Síðasta hálfa árið".decode('utf-8'),"Síðasta árið".decode('utf-8'), "Síðustu 2 ár".decode('utf-8')])
		accinfltime.SetSelection(1)
		hbox13.Add(accinfltime, proportion=1)
		vbox.Add(hbox13, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

		vbox.Add((-1, 10))

		hbox11 = wx.BoxSizer(wx.HORIZONTAL)
		calcbtn = wx.Button(self, label='Reikna', size=(70, 30))
		hbox11.Add(calcbtn, flag=wx.LEFT|wx.BOTTOM, border=5)
		vbox.Add(hbox11, flag=wx.ALIGN_RIGHT|wx.RIGHT, border=10)
		calcbtn.Bind(wx.EVT_BUTTON, lambda event: calcBestWayToPayLoan( payment, time, infltime ) )

		self.SetSizer(vbox)

class PageFive(wx.Panel):
    def __init__(self, parent):
		wx.Panel.__init__(self, parent)

		font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
		font.SetPointSize(9)

		vbox = wx.BoxSizer(wx.VERTICAL)

		hbox1 = wx.BoxSizer(wx.HORIZONTAL)
		st1 = wx.StaticText(self, label='Mánaðarleg greiðsla:'.decode('utf-8'))
		st1.SetFont(font)
		hbox1.Add(st1, flag=wx.RIGHT, border=8)
		accpayment2 = wx.TextCtrl(self)
		hbox1.Add(accpayment2, proportion=1)
		vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

		hbox12 = wx.BoxSizer(wx.HORIZONTAL)
		st12 = wx.StaticText(self, label='Hvað viltu spara lengi:'.decode('utf-8'))
		st12.SetFont(font)
		hbox12.Add(st12, flag=wx.RIGHT, border=8)
		acctime2 = wx.TextCtrl(self)
		hbox12.Add(acctime2, proportion=1)
		vbox.Add(hbox12, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

		hbox13 = wx.BoxSizer(wx.HORIZONTAL)
		st13 = wx.StaticText(self, label='Verðbólgu tímabil:'.decode('utf-8'))
		st13.SetFont(font)
		hbox13.Add(st13, flag=wx.RIGHT, border=8)
		accinfltime2 = wx.ComboBox(self, style = wx.CB_READONLY, choices= ["Síðasta mánuð".decode('utf-8'),"Síðustu 2 mánuði".decode('utf-8'),"Síðasta hálfa árið".decode('utf-8'),"Síðasta árið".decode('utf-8'), "Síðustu 2 ár".decode('utf-8')])
		accinfltime2.SetSelection(1)
		hbox13.Add(accinfltime2, proportion=1)
		vbox.Add(hbox13, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

		vbox.Add((-1, 10))

		hbox11 = wx.BoxSizer(wx.HORIZONTAL)
		calcbtn = wx.Button(self, label='Reikna', size=(70, 30))
		hbox11.Add(calcbtn, flag=wx.LEFT|wx.BOTTOM, border=5)
		vbox.Add(hbox11, flag=wx.ALIGN_RIGHT|wx.RIGHT, border=10)
		calcbtn.Bind(wx.EVT_BUTTON, lambda event: calcBestWayToPayLoan( payment, time, infltime ) )

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
		nb.AddPage(page2, "Reikna Lán".decode('utf-8'))
		nb.AddPage(page3, "Bæta við reikningum".decode('utf-8'))
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