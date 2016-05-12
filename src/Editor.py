#!/usr/bin/python2


try:
	import wx
except ImportError:
	raise ImportError,"The wxPython module is required to run this program"

class simpleapp_wx(wx.Frame):
	def __init__(self,parent,id,title):
		wx.Frame.__init__(self,parent,id,title)
		self.parent = parent
		self.initialize()

	def initialize(self):
		#sizer = wx.GridBagSizer()
		self.height=500
		self.width =300
		w1 = self.width
		w2 = int(self.width/2)
		h1 = int(.4*self.height)
		h2 = int(.2*self.height)
		h3 = h1+h2
		self.Message = wx.StaticText(self,-1,	label=u'Top Message',	pos=(0 ,0 ),	size=(w1,h1))
		self.Options = wx.StaticText(self,-1,	label=u'Middle Options',pos=(0 ,h1),	size=(w1,h2))
		self.Box1 = wx.StaticText(self,-1,		label=u'Options 1',		pos=(0 ,h3),	size=(w2,h1))
		self.Box2 = wx.StaticText(self,-1,		label=u'Options 2',		pos=(w2,h3),	size=(w2,h1))
		'''
		sizer.Add(self.Message,(0,0),(1,2),wx.EXPAND)
		sizer.Add(self.Options,(1,0),(2,2),wx.EXPAND)
		sizer.Add(self.Message,(2,0),(3,1),wx.EXPAND)
		sizer.Add(self.Message,(2,1),(3,2),wx.EXPAND)
		
		self.SetSizer(sizer)
		'''
		self.SetSizeHints(self.width,self.height,self.width,self.height)
		self.Show(True)



if __name__ == "__main__":
	app = wx.App()
	frame = simpleapp_wx(None,-1,'my application')
	app.MainLoop()
"""

try:
    import wx
except ImportError:
    raise ImportError,"The wxPython module is required to run this program"

class simpleapp_wx(wx.Frame):
    def __init__(self,parent,id,title):
        wx.Frame.__init__(self,parent,id,title)
        self.parent = parent
        self.initialize()

    def initialize(self):
        sizer = wx.GridBagSizer()

        self.entry = wx.TextCtrl(self,-1,value=u"Enter text here.")
        button = wx.Button(self,-1,label="Click me !")
        self.label = wx.StaticText(self,-1,label=u'Hello !')
        
        sizer.Add(self.entry,(0,0),(1,1),wx.EXPAND)
        sizer.Add(button, (0,1))
        sizer.Add( self.label, (1,0),(1,2), wx.EXPAND )


        self.Bind(wx.EVT_TEXT_ENTER, self.OnPressEnter, self.entry)
        self.Bind(wx.EVT_BUTTON, self.OnButtonClick, button)
        
        self.label.SetBackgroundColour(wx.BLUE)
        self.label.SetForegroundColour(wx.WHITE)

        sizer.AddGrowableCol(0)
        self.SetSizerAndFit(sizer)
        self.SetSizeHints(-1,self.GetSize().y,-1,self.GetSize().y );
        self.Show(True)

    def OnButtonClick(self,event):
        self.label.SetLabel( self.entry.GetValue() + " (You clicked the button)" )

    def OnPressEnter(self,event):
        self.label.SetLabel( self.entry.GetValue() + " (You pressed ENTER)" )

if __name__ == "__main__":
    app = wx.App()
    frame = simpleapp_wx(None,-1,'my application')
    app.MainLoop()
"""
'''
	def initialize(self):
		self.grid()
		self.TextMess = Tkinter.StringVar()
		self.Text1 = Tkinter.StringVar()
		self.Text2 = Tkinter.StringVar()
		self.Message = Tkinter.Message(self,textvariable=self.TextMess)
		self.Message.grid(column=0,row=0,columnspan=2,rowspan=4,sticky='EW',xsize=100,ysize=100)
		self.Options = Tkinter.Frame(self)
		self.Options.grid(column=0,columnspan=2,row=5,rowspan=2,sticky='EW',xsize=100,ysize=100)
		self.Box1 = Tkinter.Message(self,textvariable=self.Text1)
		self.Box1.grid(column=0,row=7,columnspan=1,rowspan=4,sticky='EW',xsize=100,ysize=50)
		self.Box2 = Tkinter.Message(self,textvariable=self.Text2)
		self.Box2.grid(column=1,row=7,columnspan=1,rowspan=4,sticky='EW',xsize=100,ysize=50)
		
		self.TextMess.set("Message Box")
		self.Text1.set("Options 1")
		self.Text2.set("Options 2")

if __name__ == "__main__":
	app = simpleapp_tk(None)
	app.title('my application')
	app.mainloop()
'''
