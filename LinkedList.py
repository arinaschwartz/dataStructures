class Node:
	"""node class for linked list. Takes an item to be stored and a pointer to the
	   next node as optional arguments."""
	def __init__(self, item = None, next = None, previous = None):
		self.item = item
		self.next = next
		self.previous = previous

class LinkedList:
	"""Linked list implementation. First-in, first-out.

		size: the size of the list
		first: the first node in the list (most recently pushed)
		last: the last node in the list (the node that would be popped)"""

	def __init__(self):
		self.size  = 0
		self.first = None
		self.last  = None

	def push(self, item = None):
		"""Pushes an item into the list containing the item given. O(1) scaling."""
		newNode = Node(item, self.first)
		if self.size == 0:
			self.last = newNode
		self.first = newNode
		if newNode.next != None:
			newNode.next.previous = newNode
		self.size += 1

	def pop(self):
		"""Pops the last item from the list. Returns the item popped. O(1) scaling."""
		popped_item = self.last.item
		if self.size == 1:
			self.first = None
			self.size -= 1
			return popped_item
		self.last = self.last.previous
		self.last.next = None
		self.size -= 1
		return popped_item

	def getFirst(self):
		return self.first.item

	def getLast(self):
		return self.last.item

	def getSize(self):
		"""Returns size of the list. O(1) scaling."""
		return self.size

def mkList(*arg):
	"""Constructs a linked list containing however many values specified in arguments.
		O(n) scaling."""
	newList = LinkedList()
	for item in reversed(arg):
		newList.push(item)
	return newList

def testList():
	newList = mkList()
	newList.push('testString1')
	newList.push('testString2')
	newList.push(5)
	newList.push(6)
	assert newList.getSize() == 4
	assert newList.pop()
	assert newList.pop()
	assert newList.pop()
	assert newList.pop()
	assert newList.getSize() == 0