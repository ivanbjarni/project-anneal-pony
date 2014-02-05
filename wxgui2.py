#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx

class PageOne(wx.Panel):
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
		st12 = wx.StaticText(self, label='Tími:'.decode('utf-8'))
		st12.SetFont(font)
		hbox12.Add(st12, flag=wx.RIGHT, border=8)
		time = wx.TextCtrl(self)
		hbox12.Add(time, proportion=1)
		vbox.Add(hbox12, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

		vbox.Add((-1, 10))

		hbox11 = wx.BoxSizer(wx.HORIZONTAL)
		calcbtn = wx.Button(self, label='Reikna', size=(70, 30))
		hbox11.Add(calcbtn, flag=wx.LEFT|wx.BOTTOM, border=5)
		vbox.Add(hbox11, flag=wx.ALIGN_RIGHT|wx.RIGHT, border=10)
		calcbtn.Bind(wx.EVT_BUTTON, lambda event: calcBestWayToPayLoan( payment, time ) )


		vbox.Add((-1, 50))

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
		st3 = wx.StaticText(self, label='Upphæð'.decode('utf-8'))
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
		st5 = wx.StaticText(self, label='fjöldi greiðsla'.decode('utf-8'))
		st5.SetFont(font)
		hbox5.Add(st5, flag=wx.RIGHT, border=8)
		loannop = wx.TextCtrl(self)
		hbox5.Add(loannop, proportion=1)
		vbox.Add(hbox5, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		#png = wx.StaticBitmap(self, -1, wx.Bitmap("demo_line_chart.png", wx.BITMAP_TYPE_ANY))
		#hbox2.Add(png, flag=wx.RIGHT, border=8)
		
		vbox.Add((-1, 10))

		hbox4 = wx.BoxSizer(wx.HORIZONTAL)
 		loaninfl = wx.CheckBox(self, label='Verðbólga'.decode('utf-8'))
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
		loans = wx.ComboBox(self)
		hbox6.Add(loans)
		vbox.Add(hbox6, flag=wx.ALIGN_LEFT|wx.LEFT, border=10)

		self.SetSizer(vbox)


#class PageTwo(wx.Panel):
#	def __init__(self, parent):


class MainFrame(wx.Frame):
    def __init__(self):
		wx.Frame.__init__(self, None, title="Moneyspender 3000", size=(600, 450))

		mainPanel = wx.Panel(self)
		nb = wx.Notebook(mainPanel)

		page1 = PageOne(nb)
		#page2 = PageTwo(nb)

		nb.AddPage(page1, "Loan Stuff")
		#nb.AddPage(page2, "MegaLoan Stuff")

		sizer = wx.BoxSizer()
		sizer.Add(nb, 1, wx.EXPAND)
		mainPanel.SetSizer(sizer)

if __name__ == '__main__':
    app = wx.App()
    MainFrame().Show()
    app.MainLoop()