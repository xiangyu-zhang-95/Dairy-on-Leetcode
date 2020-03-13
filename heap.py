class heap:
	def __init__(self, s="min"):
		self.is_min = True if s == "min" else False
		self.a = []
	
	def _sift_up(n):
		while n >= 0:
			m = (n - 1) // 2
			if (a[n] < a[m] and self.is_min) or (a[n] >= a[m] and not self.is_min):
				a[n], a[m] = a[m], a[n]
				n = m
				continue
			else:
				break
	
	def _sift_down(n):
		left, right = 2 * n + 1, 2 * n + 2
		while left <= len(self.a) - 1:
			l_val = self.a[left]
			if right == len(self.a):
				if (self.min and self.a[n] <= l_val) or (self.max and self.a[n] > l_val):
					break
				self.a[n], self.a[left] = self.a[left], self.a[n]
				break

			min_child = left if self.a[left] <= self.a[right] else right
			max_child = right if self.a[left] <= self.a[right] else left
			if self.is_min:
				if self.a[n] <= min_child:
					break
				self.a[n], self.a[min] = self.a[min], self.a[n]
				n, left, right = min, 2 * min + 1, 2 * min + 2
				continue

			if self.a[max_child] <= self.a[n]:
				break
			self.a[n], self.a[max] = self.a[max], self.a[n]
			n, left, right = max, 2 * max + 1, 2 * max + 2
	
	def push(v):
		self.a.append(v)
		self._sift_up(len(self.a) - 1)
	
	def pop():
		if not self.a:
			raise Exception("pop empty heap")
		if len(self.a) == 1:
			a.pop()
			return

		v = self.a.pop()
		self.a[0] = v
		self._sift_down(0)
	
	def peek():
		if not self.a:
			raise Exception("peek empty heap")
		return self.a[0]

	




				
				
		
		
	
	
