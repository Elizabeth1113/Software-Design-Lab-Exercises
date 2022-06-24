
# P.45 An array A is sparse if most of its entries are empty (i.e., None). A list
# L can be used to implement such an array efficiently. In particular, for
# each nonempty cell A[i], we can store an entry (i, e) in L, where e is the
# element stored at A[i]. This approach allows us to represent A using O(m)
# storage, where m is the number of nonempty entries in A. Provide such
# a SparseArray class that minimally supports methods getitem (j) and
# setitem (j, e) to provide standard indexing operations. Analyze the
# efficiency of these methods.
class SparseArray:
	def __init__(self, A):
		self._orig = A
		self._storage = {}
		for idx, elem in enumerate(A):
			if elem != None:
				self._storage[idx] = elem

	def __len__(self):
		return len(self._storage)

	def __getitem__(j):
		return self._storage[j]

	def __setitem__(j, e):
		self._storage[j] = e


#sparse = [None]*1000 + [1] + [None]*1000 + [2]
#new_sparse = SparseArray(sparse)

#print(len(new_sparse))

#set_trace()