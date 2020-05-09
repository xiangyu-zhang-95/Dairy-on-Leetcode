class heap:
	def __init__(self, s="min"):
		self.is_min = True if s == "min" else False
		self.a = []
	
	def _sift_up(self,n):
		while n > 0:
			m = (n - 1) // 2
			if (self.a[n] < self.a[m] and self.is_min) or (self.a[n] >= self.a[m] and not self.is_min):
				self.a[n], self.a[m] = self.a[m], self.a[n]
				n = m
				continue
			else:
				break
	
	def _sift_down(self,n):
		left, right = 2 * n + 1, 2 * n + 2
		if self.is_min:
			while left <= len(self.a) - 1:
				if right == len(self.a):
					if self.a[n] <= self.a[left]:
						return
					self.a[n], self.a[left] = self.a[left], self.a[n]
					return

				if self.a[left] <= self.a[right]:
					min_child, max_child = left, right
				else:
					min_child, max_child = right, left

				if self.a[n] <= self.a[min_child]:
					return	
				self.a[n], self.a[min_child] = self.a[min_child], self.a[n]
				n, left, right = min_child, 2 * min_child + 1, 2 * min_child + 2
			return

		while left <= len(self.a) - 1:
			if right == len(self.a):
				if self.a[n] >= self.a[left]:
					return
				self.a[n], self.a[left] = self.a[left], self.a[n]
				return

			if self.a[left] <= self.a[right]:
				min_child, max_child = left, right
			else:
				min_child, max_child = right, left

			if self.a[n] >= self.a[max_child]:
				return	
			self.a[n], self.a[max_child] = self.a[max_child], self.a[n]
			n, left, right = max_child, 2 * max_child + 1, 2 * max_child + 2
	
	def push(self,v):
		self.a.append(v)
		self._sift_up(len(self.a) - 1)
	
	def pop(self):
		if not self.a:
			raise Exception("pop empty heap")
		if len(self.a) == 1:
			return self.a.pop()

		v, head = self.a.pop(), self.a[0]
		self.a[0] = v
		self._sift_down(0)
		return head
	
	def peek(self):
		if not self.a:
			raise Exception("peek empty heap")
		return self.a[0]
	
	def __len__(self):
		return len(self.a)
	
	def __contains__(self, key):
		return key in self.a
