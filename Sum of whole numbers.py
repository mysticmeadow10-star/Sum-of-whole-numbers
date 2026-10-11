#Write a program to calculate the sum of whole numbers.

n = int(input("Enter a number:"))
total= 0

for i in range(n+1):
    total = total+i
    

print ("The sum is:", total)