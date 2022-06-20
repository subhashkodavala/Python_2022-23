"""

Write a program to count the total number of digits in a number using a while loop.
For example, the number is 75869, so the output should be 5.

"""


n=int(input("Enter Number:"))
count=0
while(n>0):
    count+=1
    n=n//10
    
print("The number of digits in the number are:",count)
