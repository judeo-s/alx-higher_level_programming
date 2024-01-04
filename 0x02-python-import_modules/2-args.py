#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
	size = len(argv[1:])

	print(f"{size} argument{'s' if size == 0 or size > 1 else ''}", end="")

	if not size:
		print(".")
		exit()

	print(":")
	for i in range(1, size + 1):
		print(f"{i}: {argv[i]}")
	
