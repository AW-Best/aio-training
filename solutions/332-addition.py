import sys
sys.setrecursionlimit(1000000000)

#
# Solution Template for Addition
#
# This file is provided to assist with reading of input and writing of output
# for the problem. You may modify this file however you wish, or
# you may choose not to use this file at all.
#

a = 0
b = 0

# Read the input of a and b.
a, b = map(int, input().strip().split())

# TODO: This is where you should add the numbers. Store the sum into the
# variable answer.

answer = a + b

# Write the answer.
print(answer)
