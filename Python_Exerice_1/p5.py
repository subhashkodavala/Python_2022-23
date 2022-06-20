"""
  Write a program to display only those numbers from a list that satisfy the following conditions
     
 The number must be divisible by five
 If the number is greater than 150, then skip it and move to the next number
 If the number is greater than 500, then stop the loop

"""

lst = [50,25,100,58,256,520,28,12,320,657,10,15]

for value in lst :
    if value > 500 :
        break
    elif value > 150:
        continue
    elif value % 5 == 0 :
        print(value)
