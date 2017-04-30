import sys
import getopt
import argparse

import quickSort
import bubbleSort
import selectionSort
import mergeSort

class_names = {'bubble': 'bubbleSort', 'selection': 'selectionSort', 'merge': 'mergeSort', 'quick': 'quickSort'}

def display_list(lst):
	lst = [str(i) for i in lst]
	# Handle case of empty list
	if (len(lst) == 0):
		print('| |')

	else:
		output = '|'
		for i in lst:
			output = output + ' ' + i + ' |'

		print(output)

	raw_input("Press Enter to continue...")


def main(argv):
	trace_mode = False
	parser = argparse.ArgumentParser()
	parser.add_argument("input_list", nargs='+', type=int,
	                    help="List of integers separated by space")

	parser.add_argument("alg", type=str,
	                    help="bubble, selection, merge or quick")

	parser.add_argument("-t", "--trace", action="store_true",
	                    help="Print the sorting alg step-by-step")

	args = parser.parse_args()

	if (args.trace):
		trace_mode = True

	if (args.alg not in class_names.keys()):
		print('\n Invalid algorithm name')
		parser.print_help()
		return

	print('Input: ' + str(args.input_list))

	# Call the class object based on args.alg
	class_name = class_names[args.alg]
	obj = eval(class_name + '.' + class_name)
	obj = obj(args.input_list, trace_mode)

	print('Result: ' + str(obj.sort()))


if __name__ == '__main__':
  main(sys.argv[1:])