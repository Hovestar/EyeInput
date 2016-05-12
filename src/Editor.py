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
		
		self.Message = 	wx.StaticText(self,-1,	label=u'Top Message',	pos=(0 ,0 ),	size=(w1,h1))
		self.Options = 	wx.StaticText(self,-1,	label=u'Middle Options',pos=(0 ,h1),	size=(w1,h2))
		self.Box1 = 	wx.StaticText(self,-1,	label=u'Options 1',		pos=(0 ,h3),	size=(w2,h1))
		self.Box2 = 	wx.StaticText(self,-1,	label=u'Options 2',		pos=(w2,h3),	size=(w2,h1))
		
		self.Message.Wrap(w1-10)
		self.Options.Wrap(w1-10)
		self.Box1.Wrap(w2-10)
		self.Box2.Wrap(w2-10)
		
		self.SetSizeHints(self.width,self.height,self.width,self.height)
		self.Show(True)
		
		self.Input = BinaryInput.BinaryInput()
		self.Tree = Huffman.HuffmanTree()
		self.CurrNode = self.Tree.root
	
	def updateBoxes(self):
		text = self.Input.action+self.Input.zero+self.Input.after
		for c in self.getOptions(0):
			text += c+', '
		text = text[:-2]
		self.Box1.SetLabel(text)
		
		text = self.Input.action+self.Input.one+self.Input.after
		for c in self.getOptions(1):
			text += c+', '
		text = text[:-2]
		self.Box2.SetLabel(text)
		
	
	def getOptions(self,right):
		"""right is 1 for right side and 0 for left side"""
		child = self.currNode.children()[right]
		branches = list(map(lambda x:x[0][1],child.preorder()))
		return branches
	
	def listen(self):
		inp = self.Input()
		if inp ==2:
			return
		child = self.CurrNode.children()[inp]
		if isInstance(child,Huffman._HuffmanNode):
			self.CurrNode = child
		else:
			self.Message.SetLabel(child[1])
			self.CurrNode = self.Tree.root
		self.UpdateBoxes()
		wx.CallAfter(self.listen)
		

class EyeInputEditor(wx.App):
	def __init__(self):
		wx.App.__init__(self)
		self.Frame = _my_wx_frame(None,-1,'my application')
		self.Frame.listen()
		self.MainLoop()


if __name__ == "__main__":
	app = EyeInputEditor()
