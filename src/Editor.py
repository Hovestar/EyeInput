#!/usr/bin/python2
'''
Class that holds GUI and Integrates all of the parts of the EyeInput
Base from: http://sebsauvage.net/python/gui/
'''

try:
	import wx
except ImportError:
	raise ImportError,"The wxPython module is required to run this program"
import BinaryInput
import Huffman
import thread

class _my_wx_frame(wx.Frame):
	def __init__(self,parent,id,title):
		wx.Frame.__init__(self,parent,id,title)
		self.parent = parent
		self.initialize()

	def initialize(self):
		
		self.height=500
		self.width =300
		w1 = self.width
		w2 = int(self.width/2)
		h1 = int(.4*self.height)
		h2 = int(.2*self.height)
		h3 = h1+h2
		
		self.Message = 	wx.StaticText(self,-1,	label=u'This is what you have written: ',	pos=(0 ,0 ),	size=(w1,h1))
		self.Options = 	wx.StaticText(self,-1,	label=u'Middle Options, Not Yet Implemented',pos=(0 ,h1),	size=(w1,h2))
		self.Box1 = 	wx.StaticText(self,-1,	label=u'',		pos=(0 ,h3),	size=(w2,h1))
		self.Box2 = 	wx.StaticText(self,-1,	label=u'',		pos=(w2,h3),	size=(w2,h1))
		
		self.Message.Wrap(w1-10)
		self.Options.Wrap(w1-10)
		
		self.SetSizeHints(self.width,self.height,self.width,self.height)
		self.Show(True)
	
	def updateBoxText(self,right,text):
		if right:
			self.Box1.SetLabel(text)
			self.Box1.Wrap(int(self.width/2-10))
		else:
			self.Box2.SetLabel(text)
			self.Box2.Wrap(int(self.width/2-10))
	
	def updateMessage(self,text):
		mess = self.Message.GetLabel()
		self.Message.SetLabel(mess+text)
		

class EyeInputEditor(wx.App):
	def __init__(self):
		wx.App.__init__(self)
		self.Frame = _my_wx_frame(None,-1,'my application')
		
		self.Input = BinaryInput.BinaryInput()
		self.Tree = Huffman.HuffmanTree()
		self.CurrNode = self.Tree.root
		
		thread.start_new_thread(self.listener,())
		self.MainLoop()
		
	def getOptions(self,right):
		"""right is 1 for right side and 0 for left side"""
		child = self.CurrNode.children()[right]
		return str(child)
	
	def getBoxText(self,right):
		strs = {0:self.Input.zero,1:self.Input.one}
		text = self.Input.action+strs[right]+self.Input.after
		text += self.getOptions(right)
		return text
	def updateBoxes(self):
		for i in range(2):
			text = self.getBoxText(i)
			wx.CallAfter(self.Frame.updateBoxText,i,text)
	def listener(self):
		self.updateBoxes()
		while(True):
			inp = self.Input()
			if inp == 2:
				exit(0)
			child = self.CurrNode.children()[inp]
			if isinstance(child,Huffman._HuffmanNode):
				self.CurrNode = child
			else:
				wx.CallAfter(self.Frame.updateMessage,child)
				self.CurrNode = self.Tree.root
			self.updateBoxes()
		
if __name__ == "__main__":
	app = EyeInputEditor()
