import math

class selectionSort:
	def __init__(self, lst, trace_mode):
		self.lst = lst
		self.trace_mode = trace_mode

	def sort(self):
		# The index of the beginning of the unsorted part of the array
		# At the end, lst[start_idx] will be the min of lst[start_idx : ]
		start_idx = 0
		lst = self.lst
		# Loop until no more unsorted list
		while start_idx < len(lst):
			# Assume min at the beginning of the unsorted arrray
			min_val = lst[start_idx]
			min_idx = start_idx
			# Loop through the subarray and find the min
			for i, elm in enumerate(lst[start_idx : ]):
				if elm < min_val:
					min_val = elm
					min_idx = i + start_idx


			# Swap the min of subarray with the first elm of the subarray
			lst[start_idx], lst[min_idx] = lst[min_idx], lst[start_idx]

			if (self.trace_mode):
				self.display_list(lst, start_idx, min_idx)

			start_idx += 1

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