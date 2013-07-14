from operator import itemgetter
class Heap:
	def __init__(self):
		"""Implementation of a min-heap."""
		self.heapArray = []

	def add(self, item, heapValue):
		"""Adds a value to the heap. Item is a label, heapValue is its corresponding value."""
		heapEntry = (item, heapValue)
		self.heapArray.append(heapEntry)
		self._siftUp(heapEntry)

	def pop(self):
		"""Removes the top entry in the heap (the entry with the minimum value)
		   and reorders the heap."""
		popped_value = self.heapArray[0]
		new_root = self.heapArray.pop()
		if self.getSize() == 0:
			return popped_value[0]
		self.heapArray[0] = new_root
		self._siftDown(new_root)
		return popped_value[0]

	def getSize(self):
		"""Returns the size of the heap."""
		return len(self.heapArray)

	def _siftUp(self, heapEntry):
		parent = self._parent(heapEntry)
		if parent == None or heapEntry[1] > parent[1]:
			return
		else:
			self._swap(heapEntry, parent)
			self._siftUp(heapEntry)

	def _siftDown(self, heapEntry):
		children = self._children(heapEntry)
		if children[0] == None:
			return
		elif children[1] == None:
			minChild = children[0]
		else:
			minChild = sorted(children, key = itemgetter(1))[0]
		if heapEntry[1] < minChild[1]:
			return
		else:
			self._swap(heapEntry, minChild)
			self._siftDown(heapEntry)


	def _swap(self, heapEntry1, heapEntry2):
		"""Swaps the position of two entries in the heap."""
		first_index = self.heapArray.index(heapEntry1)
		second_index = self.heapArray.index(heapEntry2)
		self.heapArray[first_index] = heapEntry2
		self.heapArray[second_index] = heapEntry1

	def _parent(self, heapEntry):
		"""Returns the parent of the given heap entry."""
		index = self.heapArray.index(heapEntry)
		if index == 0:
			return None
		parent = self.heapArray[(index - 1)/2]
		return parent

	def _children(self, heapEntry):
		"""Returns a list of the children of the given heapEntry.
			List will contain None in entries with no child present."""
		index = self.heapArray.index(heapEntry)
		childIndex = (2*index) + 1
		childList = []
		allEntries = xrange(len(self.heapArray))
		if childIndex not in allEntries:
			childList = [None, None]
			return childList
		childList.append(self.heapArray[childIndex])
		if (childIndex + 1) not in allEntries:
			childList.append(None)
			return childList
		childList.append(self.heapArray[childIndex + 1])
		return childList


def mkHeap(*arg):
	h = Heap()
	for item in arg:
		h.add(item[0], item[1])
	return h

def testHeap():
	h = Heap()
	h.add('a', 3)
	h.add('b', 9)
	h.add('c', 4)
	assert h.pop() == 'a'
	assert h.pop() == 'c'
	assert h.pop() == 'b'
	assert h.getSize() == 0