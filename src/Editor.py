#!/usr/bin/python2
'''
Class that holds GUI and Integrates all of the parts of the EyeInput
Base from: http://sebsauvage.net/python/gui/
'''

import Tkinter as tk
from tkSimpleDialog import askstring
from tkFileDialog   import asksaveasfilename

from tkMessageBox import askokcancel
import sys
import os
import Markov

THEFONT = ('courier', 18, 'normal')

class Quitter(tk.Frame):
	def __init__(self, parent=None):
		tk.Frame.__init__(self, parent)
		self.pack()
		widget = tk.Button(self, text='Quit', command=self.quit, font = THEFONT)
		widget.pack(expand=tk.YES, fill=tk.BOTH, side=tk.LEFT)
	def quit(self):
		ans = askokcancel('Verify exit', "Really quit?")
		if ans: tk.Frame.quit(self)


class ScrolledText(tk.Frame):
	def __init__(self, parent=None, text='', file=None):
		tk.Frame.__init__(self, parent)
		self.pack(expand=tk.YES, fill=tk.BOTH)
		self.makewidgets()
		self.settext(text, file)
	def makewidgets(self):
		sbar = tk.Scrollbar(self)
		text = tk.Text(self, relief=tk.SUNKEN,wrap=tk.WORD)
		sbar.config(command=text.yview)
		text.config(yscrollcommand=sbar.set)
		sbar.pack(side=tk.RIGHT, fill=tk.Y)
		text.pack(side=tk.LEFT, expand=tk.YES, fill=tk.BOTH)
		self.text = text
	def settext(self, text='', file=None):
		if file:
			text = open(file, 'r').read()
		self.text.delete('1.0', tk.END)
		self.text.insert('1.0', text)
		self.text.mark_set(tk.INSERT, '1.0')
		self.text.focus()
	def gettext(self):
		return self.text.get('1.0', tk.END+'-1c')

class AutoCorrectBox(tk.Frame):
	def __init__(self, parent = None):
		tk.Frame.__init__(self,parent)
		self.mark = Markov.Markov()
		self.mark.addFile("George.txt")
		self.num = 15
		self.words = ["" for _ in range(self.num)]
		self.options = [tk.Button(self) for _ in range(self.num)]
		for button in self.options:
			 button.pack(side = tk.LEFT)
		self.DisplayOptions("")
		self.pack()
	def DisplayOptions(self,word,part=""):
		words = self.mark.GetNextBest(self.num,word,part)
		self.words[:len(words)] = words
		for button,word in zip(self.options,self.words):
			 button.pack(side = tk.LEFT)
			 button.config(text= word, font=THEFONT)
	def changeColor(self,action,curr):
		curr %= self.num
		for num,button in enumerate(self.options):
			if action and num == curr:
				button.config(bg = "#fff")
			else:
				button.config(bg = "#ff0")
		return curr
	def GetWord(self,curr):
		curr = curr % self.num
		return self.words[curr]

class Contacts(tk.Frame):
	def __init__(self,parent = None):
		tk.Frame.__init__(self,parent)
		self.num = 5
		self.contacts = [tk.Button(self) for _ in range(self.num)]
		for button in self.contacts:
			button.pack(side = tk.LEFT)
			button.config(text = word,for = THEFONT)
	
class SimpleEditor(ScrolledText):
	def __init__(self, parent=None, file=None):
		frm = tk.Frame(parent)
		frm.pack(fill=tk.X)
		tk.Button(frm, text='Save',  command=self.onSave, font = THEFONT).pack(side=tk.LEFT)
		tk.Button(frm, text='Copy',   command=self.onCopy, font = THEFONT).pack(side=tk.LEFT)
		tk.Button(frm, text='Paste', command=self.onPaste, font = THEFONT).pack(side=tk.LEFT)
		tk.Button(frm, text='Find',  command=self.onFind, font = THEFONT).pack(side=tk.LEFT)
		Quitter(frm).pack(side=tk.LEFT)
		self.AutoCor = AutoCorrectBox(parent)
		variable = tk.StringVar(parent)
		variable.set("one") # default value
		self.Menu = tk.OptionMenu(parent, variable, "one", "two", "three")
		self.Menu.pack()
		ScrolledText.__init__(self, parent, file=file)
		self.text.config(font=THEFONT)
		self.text.bind("<Key>",self.handleText)
		self.button = 0
		self.state = 0
		self.numberOfStates = 3
		self.ToggleState()
	def onSave(self):
		filename = asksaveasfilename()
		if filename:
			alltext = self.gettext()
			open(filename, 'w').write(alltext)
	def onCopy(self):
		text = self.text.get(tk.SEL_FIRST, tk.SEL_LAST)
		if(len(text)<1):
			text = self.text.get("1.0", tk.END)
		#self.text.delete(tk.SEL_FIRST, tk.SEL_LAST)
		self.clipboard_clear()
		self.clipboard_append(text)
	def onPaste(self):
		try:
			text = self.selection_get(selection='CLIPBOARD')
			self.text.insert(tk.INSERT, text)
		except TclError:
			pass
	def onFind(self):
		target = askstring('SimpleEditor', 'Search String?')
		if target:
			where = self.text.search(target, tk.INSERT, tk.END)
			if where:
				#print where
				pastit = where + ('+%dc' % len(target))
			   #self.text.tag_remove(SEL, '1.0', END)
				self.text.tag_add(tk.SEL, where, pastit)
				self.text.mark_set(tk.INSERT, pastit)
				self.text.see(tk.INSERT)
				self.text.focus()	
	def handleText(self,event):
		b = False
		if(event.keysym == "Control_R"):
			self.ToggleState()
			return "break"
		if self.state:
			if(event.keysym == "Left"):
				self.setButton(-1)
				b = True
			if(event.keysym == "Right"):
				self.setButton(1)
				b = True
			if(event.keysym == "Down" or event.keysym == "Up"):
				word = self.AutoCor.GetWord(self.button)
				self.text.delete("{} -1c wordstart".format(tk.INSERT), tk.INSERT)
				self.text.insert(tk.INSERT," "+word+ " ")
				b = True
		if(event.char.isalnum() or event.char == " "):
			self.text.insert(tk.INSERT,event.char)
			b = True
		last = self.text.get(
			"{} -1c wordstart -2c wordstart".format(tk.INSERT),
			"{} -1c wordstart".format(tk.INSERT))
		curr = self.text.get("{} -1c wordstart".format(tk.INSERT),"{}".format(tk.INSERT))
		#print(last,curr)
		self.AutoCor.DisplayOptions(last,curr)
		#print(event.keysym)
		if(b):
			return "break"
	def ToggleState(self):
		if self.state != 0:
			self.text.config(bg = "#ff0")
		else:
			self.text.config(bg = "#fff")
		self.state +=1 
		self.state %= self.numberOfStates
		self.setButton(0)
	def setButton(self,delta):
		self.button = self.AutoCor.changeColor(self.button==1,self.button+delta)

if __name__ == '__main__':
	os.system("xset r off")
	try:
		SimpleEditor(file=sys.argv[1]).mainloop()
	except IndexError:
		SimpleEditor().mainloop()
