# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320

def factorial(x):
   if x == 0:
      return 1
   num=x
   fact=1
   while (num>0):
      fact=fact*num
      num-=1
   return fact
print(factorial(8))