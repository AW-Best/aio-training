import sys
sys.setrecursionlimit(1000000000)

#
# Solution Template for Sitting or Standing?
#
# This file is provided to assist with reading of input and writing of output
# for the problem. You may modify this file however you wish, or
# you may choose not to use this file at all.
#

r = 0
s = 0
num_tickets = 0

# Read the input.
r, s = map(int, input().strip().split())
num_tickets = int(input().strip())

# TODO: This is where you should compute the answers and store them into the
# variables num_sitting and num_standing.

num_sitting = r*s
num_standing = 0
if num_sitting < num_tickets:
  num_standing = num_tickets - num_sitting
elif num_sitting > num_tickets:
  num_standing = 0
  num_sitting = num_tickets
else:
  num_tickets = 0

# Write the answer.
print(num_sitting, num_standing)
