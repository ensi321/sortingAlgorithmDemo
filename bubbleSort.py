class bubbleSort:

	def __init__(self, lst, trace_mode):
		self.lst = lst
		self.trace_mode = trace_mode

	def sort(self):
		sorted = False
		lst = self.lst
		# Keep repeating until sorted
		while(not sorted):
			sorted = True
			# Look for each adjacent pair and swap if neccessary
			for i in range(len(lst) - 1):
				j = i + 1
				if (lst[i] > lst[j]):
					lst[i], lst[j] = lst[j], lst[i]
					sorted = False
					
				if (self.trace_mode):
					self.display_list(lst, i, j)

		return lst


	def display_list(self, lst, i, j):
		lst = [str(k) for k in lst]
		output = '|'
		for k, elm in enumerate(lst):
			if (k == i or k == j):
				elm = elm + '*'
			output = output + ' ' + str(elm) + ' |'

		print(output)
		raw_input("Press Enter to continue...")