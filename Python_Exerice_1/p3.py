# A  Program to Calculate the sum of all numbers from 1 to a given number

# Take Input From User 
unum = input("Enter Any Number : ")

# Convert User Input To INTEGER
unum = int(unum)

i=1
count=0

# For Loop Start

for i in range(1,unum+1) :
    count+=i
       
#For Loop Over
    

#Print  The Output    
print("Sum Of All Numbers From 1 Is  : ",count)
