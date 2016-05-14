#!/usr/bin/python2

'''
Huffman codes to make writing require less bits of info'
Base of code from: http://stackoverflow.com/questions/11587044/how-can-i-create-a-tree-for-huffman-encoding-and-decoding
'''


class _HuffmanNode(object):
	def __init__(self,left=None,right=None,root=None):
		self.left = left
		self.right = right
		self.root = root
	def children(self):
		return (self.left,self.right)
	def preorder(self):
		end = []
		if self.left is not None:
			if isinstance(self.left, _HuffmanNode):
				end += self.left.preorder()
			else:
				end.append(self.left)
		if self.right is not None:
			if isinstance(self.right, _HuffmanNode):
				end += self.right.preorder()
			else:
				end.append(self.right)
		return end
	def __str__(self):
		l = self.preorder()
		return ', '.join(l)

class HuffmanTree(_HuffmanNode):
	def __init__(self):
		# TODO: Build a frequency list so that it is easy to learn/ write
		freq = [
			(8.167, 'a'), (1.492, 'b'), (2.782, 'c'), (4.253, 'd'),
			(12.702, 'e'),(2.228, 'f'), (2.015, 'g'), (6.094, 'h'),
			(6.966, 'i'), (0.153, 'j'), (0.747, 'k'), (4.025, 'l'),
			(2.406, 'm'), (6.749, 'n'), (7.507, 'o'), (1.929, 'p'), 
			(0.095, 'q'), (5.987, 'r'), (6.327, 's'), (9.056, 't'), 
			(2.758, 'u'), (1.037, 'v'), (2.365, 'w'), (0.150, 'x'),
			(1.974, 'y'), (0.074, 'z'), (20.00, ' ') ]
		self.BuildTree(freq)
	def BuildTree(self,frequencies):
		p = []
		for item in frequencies:
			p.append(item)
		p.sort(key = lambda x:-x[0])
		while len(p) > 1:
			left,right = p.pop(),p.pop()
			node = _HuffmanNode(left[1],right[1])
			p.append((left[0]+right[0],node))
			p.sort(key = lambda x:-x[0])
		self.root = p.pop()[1]
	def preorder(self):
		return self.root.preorder()

if __name__=="__main__":
	tree = HuffmanTree()
	for line in tree.preorder():
		print(line)
