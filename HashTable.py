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

	def add(self, key, value):
		"""Adds a value to the hash table."""
		bucket = self._hash(key)
		self.table[bucket].append((key, value))
		self.size += 1

	def val(self, key):
		"""Given a key, returns the associated value."""
		bucket = self._hash(key)
		for entry in self.table[bucket]:
			if entry[0] == key:
				return entry[1]
		print "Key-Value pair not found."
		return None

	def assignVal(self, key, new_value):
		bucket = self._hash(key)
		for entry in self.table[bucket]:
			if entry[0] == key:
				entry[1] = new_value
				print "Key %s now assigned to value " + new_value
		print "Key-Value pair not found."

	def assignVal_listComp(self, key, new_value):
		bucket = self._hash(key)
		[(key, new_value) for entry in self.table[bucket] if entry[0] == key]


	def remove(self, key):
		"""Deletes the key and its associated value from the dictionary."""
		bucket = self._hash(key)
		thisbucket = self.table[bucket]
		[thisbucket.remove(entry) for entry in thisbucket if entry[0] == key]

def testAssignFunc():
	h = HashTable(10000)
	for i in xrange(10000):
		h.add(str(i), i)
	start_time_1 = time.time()
	for i in xrange(10000):
		h.assignVal(str(i), -1)
	timing_for = time.time() - start_time_1
	start_time_2 = time.time()
	for i in xrange(10000):
		h.assignVal_listComp(str(i), 1)
	timing_listComp = time.time() - start_time_2
	print "Time for for loop: %f." % timing_for
	print "Time for list comprehension: %f." % timing_listComp
	return timing_for - timing_listComp