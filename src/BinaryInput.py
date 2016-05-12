#!/usr/bin/python2

class BinaryInput:
	def __init__(self):
		self.action = "Press the "
		self.zero= "q"
		self.one = "w"
		self.esc = "e"
		self.after = " button for "
		self.getter = _Getch()
	def __call__(self):
		mappint = {'q':0,'w':1,'e':2}
		while True:
			try:
				return mappint[self.getter()]
			except:
				pass

class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()

if __name__=="__main__":
	inp = BinaryInput()
	print(inp())
