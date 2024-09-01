#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
	for row in range(len(matrix)):  # iterate rows col's
		for col in range(len(matrix[row])):
			print("{:d}".format(matrix[row][col]), end="")
		print()  # newline
