#!/usr/bin/python2

'''
Huffman codes to make writing require less bits of info'
Base of code from: http://stackoverflow.com/questions/11587044/how-can-i-create-a-tree-for-huffman-encoding-and-decoding
'''


class HuffmanNode(object):
	def __init__(self,left=None,right=None,root=None):
		self.left = left
		self.right = right
		self.root = root
	def children(self):
		return (self.left,self.right)
	def preorder(self,path=None):
		if path is None:
			path = []
		if self.left is not None:
			if isinstance(self.left[1], HuffmanNode):
				self.left[1].preorder(path+[0])
			else:
				print(self.left,path+[0])
		if self.right is not None:
			if isinstance(self.right[1], HuffmanNode):
				self.right[1].preorder(path+[1])
			else:
				print(self.right,path+[1])

class HuffmanTree(HuffmanNode):
	def __init__(self):
		
	def BuildTree
freq = [
	(8.167, 'a'), (1.492, 'b'), (2.782, 'c'), (4.253, 'd'),
	(12.702, 'e'),(2.228, 'f'), (2.015, 'g'), (6.094, 'h'),
	(6.966, 'i'), (0.153, 'j'), (0.747, 'k'), (4.025, 'l'),
	(2.406, 'm'), (6.749, 'n'), (7.507, 'o'), (1.929, 'p'), 
	(0.095, 'q'), (5.987, 'r'), (6.327, 's'), (9.056, 't'), 
	(2.758, 'u'), (1.037, 'v'), (2.365, 'w'), (0.150, 'x'),
	(1.974, 'y'), (0.074, 'z') ]

def encode(frequencies):
	p = []
	for item in frequencies:
		p.append(item)
	p.sort(key = lambda x:-x[0])
	while len(p) > 1:
		left,right = p.pop(),p.pop()
		node = HuffmanNode(left,right)
		p.append((left[0]+right[0],node))
		p.sort(key = lambda x:-x[0])
	return p.pop()

if __name__=="__main__":
	freq = [
		(8.167, 'a'), (1.492, 'b'), (2.782, 'c'), (4.253, 'd'),
		(12.702, 'e'),(2.228, 'f'), (2.015, 'g'), (6.094, 'h'),
		(6.966, 'i'), (0.153, 'j'), (0.747, 'k'), (4.025, 'l'),
		(2.406, 'm'), (6.749, 'n'), (7.507, 'o'), (1.929, 'p'), 
		(0.095, 'q'), (5.987, 'r'), (6.327, 's'), (9.056, 't'), 
		(2.758, 'u'), (1.037, 'v'), (2.365, 'w'), (0.150, 'x'),
		(1.974, 'y'), (0.074, 'z'), (20.00, ' ') ]
	# TODO: Build a frequency list so that it is easy to learn/ write
	node = encode(freq)
	node[1].preorder()
