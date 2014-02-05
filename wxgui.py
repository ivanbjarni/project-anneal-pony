#!/usr/bin/python
# -*- coding: utf-8 -*-

# gotoclass.py
from fjarmal import *
import wx

class Example(wx.Frame):
  
	def __init__(self, parent, title):
		super(Example, self).__init__(parent, title=title, size=(600, 450))
		self.InitUI()
		self.Centre()
		self.Show()     
        
	def InitUI(self):
    
		panel = wx.Panel(self)

		font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
		font.SetPointSize(9)

		vbox = wx.BoxSizer(wx.VERTICAL)

		hbox1 = wx.BoxSizer(wx.HORIZONTAL)
		st1 = wx.StaticText(panel, label='Mánaðarleg greiðsla:'.decode('utf-8'))
		st1.SetFont(font)
		hbox1.Add(st1, flag=wx.RIGHT, border=8)
		payment = wx.TextCtrl(panel)
		hbox1.Add(payment, proportion=1)
		vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

		vbox.Add((-1, 10))

		hbox11 = wx.BoxSizer(wx.HORIZONTAL)
		calcbtn = wx.Button(panel, label='Reikna', size=(70, 30))
		hbox11.Add(calcbtn, flag=wx.LEFT|wx.BOTTOM, border=5)
		vbox.Add(hbox11, flag=wx.ALIGN_RIGHT|wx.RIGHT, border=10)

		vbox.Add((-1, 50))

		hbox2 = wx.BoxSizer(wx.HORIZONTAL)
		st2 = wx.StaticText(panel, label='Lán:'.decode('utf-8'))
		st2.SetFont(font)
		hbox2.Add(st2, flag=wx.RIGHT, border=8)
		vbox.Add(hbox2, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

		hbox21 = wx.BoxSizer(wx.HORIZONTAL)
		st21 = wx.StaticText(panel, label='Nafn'.decode('utf-8'))
		st21.SetFont(font)
		hbox21.Add(st21, flag=wx.RIGHT, border=8)
		loanname = wx.TextCtrl(panel)
		hbox21.Add(loanname, proportion=1)
		vbox.Add(hbox21, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

		hbox3 = wx.BoxSizer(wx.HORIZONTAL)
		st3 = wx.StaticText(panel, label='Upphæð'.decode('utf-8'))
		st3.SetFont(font)
		hbox3.Add(st3, flag=wx.RIGHT, border=8)
		loanamount = wx.TextCtrl(panel)
		hbox3.Add(loanamount, proportion=1)
		vbox.Add(hbox3, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

		hbox4 = wx.BoxSizer(wx.HORIZONTAL)
		st4 = wx.StaticText(panel, label='Vextir'.decode('utf-8'))
		st4.SetFont(font)
		hbox4.Add(st4, flag=wx.RIGHT, border=8)
		loaninterest = wx.TextCtrl(panel)
		hbox4.Add(loaninterest, proportion=1)
		vbox.Add(hbox4, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

		hbox5 = wx.BoxSizer(wx.HORIZONTAL)
		st5 = wx.StaticText(panel, label='fjöldi greiðsla'.decode('utf-8'))
		st5.SetFont(font)
		hbox5.Add(st5, flag=wx.RIGHT, border=8)
		loannop = wx.TextCtrl(panel)
		hbox5.Add(loannop, proportion=1)
		vbox.Add(hbox5, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		#png = wx.StaticBitmap(self, -1, wx.Bitmap("demo_line_chart.png", wx.BITMAP_TYPE_ANY))
		#hbox2.Add(png, flag=wx.RIGHT, border=8)
		
		vbox.Add((-1, 10))

		hbox4 = wx.BoxSizer(wx.HORIZONTAL)
 		loaninfl = wx.CheckBox(panel, label='Verðbólga'.decode('utf-8'))
		loaninfl.SetFont(font)
		hbox4.Add(loaninfl)
		vbox.Add(hbox4, flag=wx.LEFT, border=10)

		hbox5 = wx.BoxSizer(wx.HORIZONTAL)
		addloanbtn = wx.Button(panel, label='Bæta við'.decode('utf-8'), size=(70, 30))
		hbox5.Add(addloanbtn)
		vbox.Add(hbox5, flag=wx.ALIGN_RIGHT|wx.RIGHT, border=10)
		# Event listener for button
		addloanbtn.Bind(wx.EVT_BUTTON, lambda event: makeLoan(loannop, loaninfl, loanname, loanamount, loaninterest, loans) )

		hbox6 = wx.BoxSizer(wx.HORIZONTAL)
		st6 = wx.StaticText(panel, label='Núverandi Lán:'.decode('utf-8'))
		st6.SetFont(font)
		hbox6.Add(st6, flag=wx.RIGHT, border=8)
		loans = wx.ComboBox(panel)
		hbox6.Add(loans)
		vbox.Add(hbox6, flag=wx.ALIGN_LEFT|wx.LEFT, border=10)

		panel.SetSizer(vbox)

if __name__ == '__main__':
  
    app = wx.App()
    Example(None, title='Moneyspender 3000')
    app.MainLoop()