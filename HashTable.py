import time
class HashTable:
	"""Implementation of hash table. Initialized with a given static number of hash buckets.
		Consists of keys (strings) and values (any type)."""
	def __init__(self, numBuckets):
		self.numBuckets = numBuckets
		self.table = [[] for bucket in xrange(self.numBuckets)]
		self.size = 0

	def _hash(self, key):
		"""Given a key, hashes it and returns the bucket the value resides in."""
		ascii_val = sum([ord(char) for char in key])
		bucket = (ascii_val * 73) % self.numBuckets
		return bucket

	def _add(self, key, value):
		"""Adds a value to the hash table."""
		bucket = self._hash(key)
		self.table[bucket].append((key, value))
		self.size += 1

	def _val(self, key):
		"""Given a key, returns the associated value."""
		if type(key) != str:
			raise TypeError('Key must be a string.')
		bucket = self._hash(key)
		for entry in self.table[bucket]:
			if entry[0] == key:
				return entry[1]
		raise KeyError('Key-Value pair not found.')

	def _assignVal(self, key, new_value):
		"""Re-assigns the value of an existing key."""
		if type(key) != str:
			raise TypeError('Key must be a string.')
		bucket = self._hash(key)
		thisBucket = self.table[bucket]
		self.table[bucket] = [(key, new_value) for entry in thisBucket if entry[0] == key]
		print "Key %s now assigned to value" % key, new_value

	def val(self, key, val=None):
		"""Method-wrap for previous three helper-functions."""
		if val == None:
			return self._val(key)
		else:
			try:
				curent_value = self._val(key)
				self._assignVal(key, val)
			except:
				self._add(key, val)

	def remove(self, key):
		"""Deletes the key and its associated value from the dictionary."""
		bucket = self._hash(key)
		thisBucket = self.table[bucket]
		origLength = len(thisBucket)
		[thisBucket.remove(entry) for entry in thisBucket if entry[0] == key]
		if origLength != len(thisBucket):
			self.size -= 1
		else:
			raise KeyError('Key-Value pair not found.')

def testHashTable():
	h = HashTable(100)
	h.add('a', 3)
	h.add('b', 4)
	h.add('c', 5)
	h.add('cake', 42)
	h.add('jeebusallmighty', 1)
	assert h.size == 5
	h.remove('a')
	h.remove('b')
	h.remove('c')
	h.remove('cake')
	h.remove('jeebusallmighty')
	assert h.size == 0