#!/usr/bin/python2
try:
	import wx
except ImportError:
	raise ImportError,"The wxPython module is required to run this program"
import thread

class MyText(wx.Button):
	def __init__(self,par,*args):
		wx.Button.__init__(self,par,-1,label = "Words",style=wx.ST_NO_AUTORESIZE,*args)
	def SetSize(self,width,height):
		wx.Button.SetSize(self,(int(width),int(height)))
	def SetPos(self,width,height):
		wx.Button.SetPosition(self,(int(width),int(height)))


class EditBox(MyText):
	def __init__(self,par):
		MyText.__init__(self,par)
		
class ListBox(MyText):
	def __init__(self,par):
		MyText.__init__(self,par)
		
class Button(MyText):
	def __init__(self,par):
		MyText.__init__(self,par)


class MyFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self,None,wx.ID_ANY,"George's App")
		
		"""
		self.eBody			.
		self.lAutoComplete	.
		self.lMode			.
		self.bAction		.
		self.bClear			.
		"""
		
		self.eBody = EditBox(self)
		self.lAutoComplete = ListBox(self)
		self.lMode = ListBox(self)
		self.bAction = Button(self)
		self.bClear = Button(self)
		
		self.ApplyToAll(lambda x:x.Bind(wx.EVT_KEY_DOWN,self.KeyPress))
		
		self.Bind(wx.EVT_KEY_DOWN,self.KeyPress)
		
		self.Bind(wx.EVT_SIZE,self.Resize)
		self.setLabels()
		self.Show(True)
	def ApplyToAll(self, method):
		# for args and odd ones make method be a lambda
		fields = [self.eBody, self.lAutoComplete, self.lMode,self.bAction,self.bClear]
		for member in fields:
			method(member)
		
	def KeyPress(self,event):
		keyCode = event.GetKeyCode()
		specials = {
			wx.WXK_BACK :"WXK_BACK ",
                        wx.WXK_EXECUTE :"WXK_EXECUTE ",
                        wx.WXK_F1 :"WXK_F1 ",
                        wx.WXK_NUMPAD_SPACE :"WXK_NUMPAD_SPACE ",
                        wx.WXK_WINDOWS_LEFT:"WXK_WINDOWS_LEFT",
                        wx.WXK_TAB :"WXK_TAB ",
                        wx.WXK_SNAPSHOT :"WXK_SNAPSHOT ",
                        wx.WXK_F2 :"WXK_F2 ",
                        wx.WXK_NUMPAD_TAB :"WXK_NUMPAD_TAB ",
                        wx.WXK_WINDOWS_RIGHT:"WXK_WINDOWS_RIGHT",
                        wx.WXK_RETURN :"WXK_RETURN ",
                        wx.WXK_INSERT :"WXK_INSERT ",
                        wx.WXK_F3 :"WXK_F3 ",
                        wx.WXK_NUMPAD_ENTER :"WXK_NUMPAD_ENTER ",
                        wx.WXK_WINDOWS_MENU:"WXK_WINDOWS_MENU",
                        wx.WXK_ESCAPE :"WXK_ESCAPE ",
                        wx.WXK_HELP :"WXK_HELP ",
                        wx.WXK_F4 :"WXK_F4 ",
                        wx.WXK_NUMPAD_F1 :"WXK_NUMPAD_F1 ",
                        wx.WXK_SPECIAL1:"WXK_SPECIAL1",
                        wx.WXK_SPACE :"WXK_SPACE ",
                        wx.WXK_NUMPAD0 :"WXK_NUMPAD0 ",
                        wx.WXK_F5 :"WXK_F5 ",
                        wx.WXK_NUMPAD_F2 :"WXK_NUMPAD_F2 ",
                        wx.WXK_SPECIAL2:"WXK_SPECIAL2",
                        wx.WXK_DELETE :"WXK_DELETE ",
                        wx.WXK_NUMPAD1 :"WXK_NUMPAD1 ",
                        wx.WXK_F6 :"WXK_F6 ",
                        wx.WXK_NUMPAD_F3 :"WXK_NUMPAD_F3 ",
                        wx.WXK_SPECIAL3:"WXK_SPECIAL3",
                        wx.WXK_LBUTTON :"WXK_LBUTTON ",
                        wx.WXK_NUMPAD2 :"WXK_NUMPAD2 ",
                        wx.WXK_F7 :"WXK_F7 ",
                        wx.WXK_NUMPAD_F4 :"WXK_NUMPAD_F4 ",
                        wx.WXK_SPECIAL4:"WXK_SPECIAL4",
                        wx.WXK_RBUTTON :"WXK_RBUTTON ",
                        wx.WXK_NUMPAD3 :"WXK_NUMPAD3 ",
                        wx.WXK_F8 :"WXK_F8 ",
                        wx.WXK_NUMPAD_HOME :"WXK_NUMPAD_HOME ",
                        wx.WXK_SPECIAL5:"WXK_SPECIAL5",
                        wx.WXK_CANCEL :"WXK_CANCEL ",
                        wx.WXK_NUMPAD4 :"WXK_NUMPAD4 ",
                        wx.WXK_F9 :"WXK_F9 ",
                        wx.WXK_NUMPAD_LEFT :"WXK_NUMPAD_LEFT ",
                        wx.WXK_SPECIAL6:"WXK_SPECIAL6",
                        wx.WXK_MBUTTON :"WXK_MBUTTON ",
                        wx.WXK_NUMPAD5 :"WXK_NUMPAD5 ",
                        wx.WXK_F10 :"WXK_F10 ",
                        wx.WXK_NUMPAD_UP :"WXK_NUMPAD_UP ",
                        wx.WXK_SPECIAL7:"WXK_SPECIAL7",
                        wx.WXK_CLEAR :"WXK_CLEAR ",
                        wx.WXK_NUMPAD6 :"WXK_NUMPAD6 ",
                        wx.WXK_F11 :"WXK_F11 ",
                        wx.WXK_NUMPAD_RIGHT :"WXK_NUMPAD_RIGHT ",
                        wx.WXK_SPECIAL8:"WXK_SPECIAL8",
                        wx.WXK_SHIFT :"WXK_SHIFT ",
                        wx.WXK_NUMPAD7 :"WXK_NUMPAD7 ",
                        wx.WXK_F12 :"WXK_F12 ",
                        wx.WXK_NUMPAD_DOWN :"WXK_NUMPAD_DOWN ",
                        wx.WXK_SPECIAL9:"WXK_SPECIAL9",
                        wx.WXK_ALT :"WXK_ALT ",
                        wx.WXK_NUMPAD8 :"WXK_NUMPAD8 ",
                        wx.WXK_F13 :"WXK_F13 ",
                        wx.WXK_NUMPAD_PRIOR :"WXK_NUMPAD_PRIOR ",
                        wx.WXK_SPECIAL10:"WXK_SPECIAL10",
                        wx.WXK_CONTROL :"WXK_CONTROL ",
                        wx.WXK_NUMPAD9 :"WXK_NUMPAD9 ",
                        wx.WXK_F14 :"WXK_F14 ",
                        wx.WXK_NUMPAD_PAGEUP :"WXK_NUMPAD_PAGEUP ",
                        wx.WXK_SPECIAL11:"WXK_SPECIAL11",
                        wx.WXK_MENU :"WXK_MENU ",
                        wx.WXK_MULTIPLY :"WXK_MULTIPLY ",
                        wx.WXK_F15 :"WXK_F15 ",
                        wx.WXK_NUMPAD_NEXT :"WXK_NUMPAD_NEXT ",
                        wx.WXK_SPECIAL12:"WXK_SPECIAL12",
                        wx.WXK_PAUSE :"WXK_PAUSE ",
                        wx.WXK_ADD :"WXK_ADD ",
                        wx.WXK_F16 :"WXK_F16 ",
                        wx.WXK_NUMPAD_PAGEDOWN :"WXK_NUMPAD_PAGEDOWN ",
                        wx.WXK_SPECIAL13:"WXK_SPECIAL13",
                        wx.WXK_CAPITAL :"WXK_CAPITAL ",
                        wx.WXK_SEPARATOR :"WXK_SEPARATOR ",
                        wx.WXK_F17 :"WXK_F17 ",
                        wx.WXK_NUMPAD_END :"WXK_NUMPAD_END ",
                        wx.WXK_SPECIAL14:"WXK_SPECIAL14",
                        wx.WXK_PRIOR :"WXK_PRIOR ",
                        wx.WXK_SUBTRACT :"WXK_SUBTRACT ",
                        wx.WXK_F18 :"WXK_F18 ",
                        wx.WXK_NUMPAD_BEGIN :"WXK_NUMPAD_BEGIN ",
                        wx.WXK_SPECIAL15:"WXK_SPECIAL15",
                        wx.WXK_NEXT :"WXK_NEXT ",
                        wx.WXK_DECIMAL :"WXK_DECIMAL ",
                        wx.WXK_F19 :"WXK_F19 ",
                        wx.WXK_NUMPAD_INSERT :"WXK_NUMPAD_INSERT ",
                        wx.WXK_SPECIAL16:"WXK_SPECIAL16",
                        wx.WXK_END :"WXK_END ",
                        wx.WXK_DIVIDE :"WXK_DIVIDE ",
                        wx.WXK_F20 :"WXK_F20 ",
                        wx.WXK_NUMPAD_DELETE :"WXK_NUMPAD_DELETE ",
                        wx.WXK_SPECIAL17:"WXK_SPECIAL17",
                        wx.WXK_HOME :"WXK_HOME ",
                        wx.WXK_NUMLOCK :"WXK_NUMLOCK ",
                        wx.WXK_F21 :"WXK_F21 ",
                        wx.WXK_NUMPAD_EQUAL :"WXK_NUMPAD_EQUAL ",
                        wx.WXK_SPECIAL18:"WXK_SPECIAL18",
                        wx.WXK_LEFT :"WXK_LEFT ",
                        wx.WXK_SCROLL :"WXK_SCROLL ",
                        wx.WXK_F22 :"WXK_F22 ",
                        wx.WXK_NUMPAD_MULTIPLY :"WXK_NUMPAD_MULTIPLY ",
                        wx.WXK_SPECIAL19:"WXK_SPECIAL19",
                        wx.WXK_UP :"WXK_UP ",
                        wx.WXK_PAGEUP :"WXK_PAGEUP ",
                        wx.WXK_F23 :"WXK_F23 ",
                        wx.WXK_NUMPAD_ADD :"WXK_NUMPAD_ADD ",
                        wx.WXK_SPECIAL20:"WXK_SPECIAL20",
                        wx.WXK_RIGHT :"WXK_RIGHT ",
                        wx.WXK_PAGEDOWN :"WXK_PAGEDOWN ",
                        wx.WXK_F24 :"WXK_F24 ",
                        wx.WXK_NUMPAD_SEPARATOR :"WXK_NUMPAD_SEPARATOR ",
                        wx.WXK_DOWN :"WXK_DOWN ",
                        wx.WXK_NUMPAD_SUBTRACT:"WXK_NUMPAD_SUBTRACT",
                        wx.WXK_SELECT:"WXK_SELECT",
                        wx.WXK_NUMPAD_DECIMAL:"WXK_NUMPAD_DECIMAL",
                        wx.WXK_PRINT:"WXK_PRINT",
                        wx.WXK_NUMPAD_DIVIDE:"WXK_NUMPAD_DIVIDE"
		}
		if(keyCode in specials):
			print(specials[keyCode])
		else:
			print("{:c}".format(keyCode))
	def setLabels(self):
		font = wx.Font(18, wx.DEFAULT, wx.NORMAL, wx.BOLD)
		
		self.eBody			.SetLabel("Message Body")
		self.lAutoComplete	.SetLabel("AutoComplete")
		self.lMode			.SetLabel("Modes")
		self.bAction		.SetLabel("Action")
		self.bClear			.SetLabel("Clear")
		
		self.ApplyToAll(lambda x:x.SetFont(font))
		
		
	def Resize(self,*args):
		w,h = self.GetVirtualSizeTuple()
		
		self.eBody			.SetSize(w*.6,h)
		self.lAutoComplete	.SetSize(w*.4,h*.6)
		self.lMode			.SetSize(w*.4,h*.2)
		self.bAction		.SetSize(w*.2,h*.2)
		self.bClear			.SetSize(w*.2,h*.2)
		
		
		self.eBody			.SetPos(w*.0,h*.0)
		self.lAutoComplete	.SetPos(w*.6,h*.0)
		self.lMode			.SetPos(w*.6,h*.6)
		self.bAction		.SetPos(w*.6,h*.8)
		self.bClear			.SetPos(w*.8,h*.8)
		
		
class MyApp(wx.App):
	def __init__(self):
		wx.App.__init__(self)
		self.frame = MyFrame();
# Run the program
if __name__ == "__main__":
	app = MyApp()
	app.MainLoop()
