#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
	size = len(argv[1:])

	if not size:
		exit()

	sum = 0
	for i in range(1, size + 1):
		try:
			sum += int(argv[i])
		except ValueError:
			print("Not and integer")
			exit()
	print(sum)
