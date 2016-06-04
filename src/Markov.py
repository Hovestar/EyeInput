#!/usr/bin/python2

import random
import re
import pickle
import string

class Markov:
	def __init__(self,num=2):
		self.depth = num
		self.Map = {}
		self.ending = "@@END@@"
		self.start = ""
		self.weights = [1,.8]
	
	def addFile(self,file):
		with open(file,'r') as f:
			text = self.cleanString(f.read())
		for line in re.split("\.|\r\n|\n|\?|!",text):
			if( len(line) < 1):
				continue
			last = self.start
			for word in line.split(" "):
				self[last] = word
				last = word
			self[last] = self.ending

	def __setitem__(self, marker, value):
		# This is the same as  self[marker] = value
		try:
			self.Map[marker]
		except KeyError:
			self.Map[marker] = {}
		try:
			self.Map[marker][value] +=1
		except KeyError:
			self.Map[marker][value] = 1

	def __str__(self):
		s = "{\n"
		for key in self.Map:
			s += "'{}':{}\n".format(key, str(self.Map[key]))
		s += "}\n"
		return s

	def GetNextBest(self, num, key,part = ""):
		key = self.cleanString(key)
		part = self.cleanString(part)
		best = self._bestHelper(key)
		tmp = sorted(best, key = lambda x:-x[1])
		tmp = filter(lambda x: x[0].startswith(part),tmp)
		listOfOnes = list(map(lambda x:x[0][0],zip(tmp,range(num))))
		return listOfOnes
	def cleanString(self,s):
		table = string.maketrans("","")
		s = str(s)
		s = s.lower()
		s = s.translate(table, "#$%&\'()*+,-/:;<=>@[\\]^_`{|}~\"")
		s = s.strip()
		return s
	def _bestHelper(self,key):
		l0 = lambda x: sum([v for _,v in self.Map.get(x,{0:0}).items()])
		l1 = lambda x: self.Map.get(key,{}).get(x,0)
		myElems = (set(self.Map) | set(self.Map.get(key,{})))
		myElems.remove(self.start)
		myElems.discard(self.ending)
		scaler = 4.0/len(myElems)
		best = []
		for k in myElems:
			t0 = l0(k)
			t1 = l1(k)
			best.append((k,t0*scaler+t1))
		#best = [(k, l1(k) + *scaler) for k in myElems]
		return best

if __name__=="__main__":
	mark = Markov()
	mark.addFile("George.txt")
	print(mark.GetNextBest(4,"",""))
