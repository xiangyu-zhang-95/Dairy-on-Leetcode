class hashheap:
	def __init__(self, s="min"):
		self.is_min = True if s == "min" else False
		self.a = []
		self.map = {}
	
	def peek(self):
		return self.a[0]
	
	def _sift_up(self, i):
		while i > 0 and (self.a[(i - 1) // 2] < self.a[i] if self.is_min else self.a[(i - 1) // 2] > self.a[i]):
			self.a[i], self.a[(i - 1) // 2] = self.a[(i - 1) // 2], self.a[i]
			self.map[self.a[i]], self.map[self.a[(i - 1)//2]] = i, (i - 1)//2
			i = (i - 1) // 2
		return i
	
	def _sift_down(self, i):
		while 2 * i + 2 <= len(self.a) - 1 and (self.a[i] > min(self.a[2 * i + 1], self.a[2 * i + 2]) if self.is_min else self.a[i] < max(self.a[2 * i + 1], self.a[2 * i + 2])):
			if self.is_min:
				p = 2 * i + 1 if self.a[2 * i + 1] < self.a[2 * i + 2] else 2 * i + 2
			else:
				p = 2 * i + 1 if self.a[2 * i + 1] > self.a[2 * i + 2] else 2 * i + 2

			self.a[i], self.a[p] = self.a[p], self.a[i]
			self.map[a[i]], self.map[a[p]] = i, p
			i = p

		if 2 * i + 2 == len(self.a) and (self.a[i] > self.a[2 * i + 1] if self.is_min else self.a[i] < self.a[2 * i + 1]):
			self.a[i], self.a[2 * i + 1] = self.a[2 * i + 1], self.a[i]
			self.map[a[i]], self.map[a[2 * i + 1]] = i, 2 * i + 1
			i = 2 * i + 1
		return i
	
	def push(self, v):
		self.a.append(v)
		self.map[v] = len(self.a) - 1
		self._sift_up(len(self.a) - 1)
	
	def pop(self):
		returnitem = self.a[0]
		if len(self.a) == 1:
			self.a = []
			self.map = {}
			return returnitem
		del self.map[returnitem]

		self.a[0] = self.a[len(self.a) - 1]
		self.map[self.a[0]] = 0
		self.a.pop()

		self._sift_down(0)
		return returnitem
	
	def delete(self, v):
		i = self.map[v]
		if i == len(self.a) - 1:
			self.a.pop()
			del self.map[v]
			return
		
		self.a[i], self.a[len(self.a) - 1] = self.a[len(self.a) - 1], self.a[i]
		self.map[self.a[i]], self.map[self.a[len(self.a) - 1]] = i, len(self.a) - 1
		del self.map[self.a[len(self.a) - 1]]
		self.a.pop()

		i = self._sift_up(i)
		self._sift_down(i)

