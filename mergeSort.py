import math

class mergeSort:
	def __init__(self, lst, trace_mode):
		self.lst = lst
		self.trace_mode = trace_mode

	def sort(self):
		return self.execute(self.lst)

	def execute(self, lst):
		if (len(lst) == 1):
			return lst

		# Split the array into 2
		left = lst[: int(math.ceil(len(lst) / 2))]
		right = lst[int(math.ceil(len(lst) / 2)) : ]

		if (self.trace_mode):
			self.print_split_message(lst, left, right)

		left = self.execute(left)
		right = self.execute(right)

		return self.merge(left, right)

	def merge(self, left, right):
		if (self.trace_mode):
			self.print_merge_message_1(left, right)

		# This is an array we want to return
		result = []

		# While left and right still have elements
		while (len(left) != 0 and len(right) != 0):
			# Append either first elm of left or first elm of right whichever is smaller
			if (left[0] < right[0]):
				result.append(left[0])
				del left[0]
			else:
				result.append(right[0])
				del right[0]

		# Deal with case where right is empty but left still have couple elms
		while (len(left) != 0):
			result.append(left[0])
			del left[0]
		# Deal with case where left is empty but right is non empty
		while (len(right) != 0):
			result.append(right[0])
			del right[0]

		if (self.trace_mode):
			self.print_merge_message_2(result)

		return result

	def print_split_message(self, lst, left, right):
		print('Splitting ' + str(lst) + ' to ' + str(left) + ', ' + str(right))
		raw_input("Press Enter to continue...")
		print('===========')

	def print_merge_message_1(self, left, right):
		print('Merging ' + str(left) + ', ' + str(right))

	def print_merge_message_2(self, result):
		print('Result from merging: ' + str(result))
		raw_input("Press Enter to continue...")
		print('===========')