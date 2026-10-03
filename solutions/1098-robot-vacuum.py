import sys
sys.setrecursionlimit(1000000000)

#
# Solution Template for Robot Vacuum
#
# Australian Informatics Olympiad 2021
#
# This file is provided to assist with reading of input and writing of output
# for the problem. You may modify this file however you wish, or
# you may choose not to use this file at all.
#

# K is the number of instructions.
K = 0

# instrs contains the sequence of instructions.
instrs = ""

answer = 0

# Read the value of K and the sequence of instructions.
count = {"N":0, "E":0, "S":0, "W":0}
K = int(input().strip())
instrs = input().strip()
for instr in instrs:
  count[instr] += 1
v = count["N"]-count["S"]
vi = count["W"]-count["E"]

answer = abs(v)+abs(vi)




# Write the answer.
print(answer)
