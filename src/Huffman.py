#!/usr/bin/python2

'''
Huffman codes to make writing require less bits of info'
Base of code from: http://stackoverflow.com/questions/11587044/how-can-i-create-a-tree-for-huffman-encoding-and-decoding
'''


class _HuffmanNode(object):
	def __init__(self,left=None,right=None,name=None):
		self.left = left
		self.right = right
		self.name = name
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
	def replaceSpecial(self,c):
		dic = {
			" ":"<space>",
			"\d":"<delete>"
		}
		if c in dic:
			return dic[c]
		return c
	def __str__(self):
		if self.name is not None:
			return self.name
		l = self.preorder()
		replaced = map(self.replaceSpecial,l)
		return ', '.join(replaced)

class HuffmanTree(_HuffmanNode):
	def __init__(self):
		# Its not really a huffman tree anymore, but it follows the idea of it.
		f = [
			([[["a","e"],[['i','o'],['u','y']]],[" ","\d"]],"Vowels and special Characters"),
			([
				[
					[['b',['c','d']],['f','g']],
					[['h',['j','k']],['l','m']]
				],[
					[['n',['p','q']],['r','s']],
					['t',[['v','w'],['x','z']]]
				]
			],"Consonants")
		]
		self.root = self.BuildTree(f)

	def BuildTree(self,f):
		if isinstance(f,tuple):
			node = self.BuildTree(f[0])
			node.name = f[1]
			return node
		if isinstance(f,str):
			return f
		left = self.BuildTree(f[0])
		right= self.BuildTree(f[1])
		return _HuffmanNode(left,right)
	def preorder(self):
		return self.root.preorder()

if __name__=="__main__":
	tree = HuffmanTree()
	for line in tree.preorder():
		print(line)
