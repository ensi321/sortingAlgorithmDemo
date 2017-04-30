import main

class quickSort:

	def __init__(self, lst, trace_mode):
		self.lst = lst
		self.trace_mode = trace_mode


	def sort(self):
		return self.execute(self.lst)

	def execute(self, lst):
		# Determine if we still need to sort this
		if (len(lst) <= 1 or (len(lst) == 2 and lst[1] >= lst[0])):
			main.display_list(lst)
			return lst


		# First choose a pivot, here we choose the rightmost element
		pivot_idx = len(lst) - 1
		left, right, pivot = self.divide(lst, pivot_idx)

		if (self.trace_mode):
			self.display_list(left, right, pivot)

		# Run execute for left and right, then concatenate them along with pivot to get result
		left_result = self.execute(left)
		right_result = self.execute(right)

		result = left_result
		result.append(pivot)
		result += right_result

		return result


	def divide(self, lst, pivot_idx):
		pivot = lst[pivot_idx]
		# Then we divide by rearranging the array
		left_idx = 0
		# We first move all the element smaller than the pivot to the left. Left_idx keeps track for the position to be added
		for i, elm in enumerate(lst):
			if elm < pivot:
				# Swap position by setting lst[left_idx] = elm and lst[i] = lst[left_idx]
				lst[i] = lst[left_idx]
				lst[left_idx] = elm
				# Advance the left_idx
				left_idx += 1
		# Then move pivot to left_idx
		lst[pivot_idx] = lst[left_idx]
		lst[left_idx] = pivot
		# Return left array, and right array and pivot
		left = lst[0: left_idx]
		right = lst[left_idx + 1 : ]

		return left, right, pivot


	def display_list(self, left, right, pivot):
		output = '|'
		for i in left:
			output = output + ' ' + str(i) + ' |'

		output = output + ' ' + str(pivot) + '*' + ' |'
		
		for i in right:
			output = output + ' ' + str(i) + ' |'		

		print(output)
		raw_input("Press Enter to continue...")