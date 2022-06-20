# A Program To Print Multiplication Table Of Given Number 

# Take Input From User
num = input("Enter Number To Print His Multiplication Table : ")

# Convert User Input To INTEGER
num = int(num)


mulchar = 1
count=1
res=0

# While Loop Start

while count<=10 :
    
    res= num * mulchar
    print(res)
    
    mulchar+=1
    count+=1

# While Loop Over 

