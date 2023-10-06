class Node:
	def __init__(self, x):
		self.data = x
		self.left = None
		self.right = None
def allTraversal(root):
	pre = []
	post = []
	inn = []
	s = []
	s.append([root, 1])
	while (len(s) > 0):
		p = s[-1]
		if (p[1] == 1):
			s[-1][1] += 1
			pre.append(p[0].data)
			if (p[0].left):
				s.append([p[0].left, 1])
		elif (p[1] == 2):
			s[-1][1] += 1
			inn.append(p[0].data);
			if (p[0].right):
				s.append([p[0].right, 1])
		else:
			post.append(p[0].data);
			del s[-1]
	print("Preorder Traversal: ",end=" ")
	for i in pre:
		print(i,end=" ")
	print()
	print("Inorder Traversal: ",end=" ")
	for i in inn:
		print(i,end=" ")
	print()
	print("Postorder Traversal: ",end=" ")
	for i in post:
		print(i,end=" ")
	print()
if __name__ == '__main__':
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)
	root.right.left = Node(6)
	root.right.right = Node(7)
	allTraversal(root)
