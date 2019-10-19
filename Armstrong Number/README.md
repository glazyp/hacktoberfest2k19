# Armstrong Number
Armstrong number:  A number is called Armstrong number if it is equal to the sum of the cubes of its own digits.
Write a program to generate and check if a number is an Armstrong number.

num= input("Enter a number:")
length= len(num)
num= int(num)
num_int= num
summation=0
while num_int>0:
    digit=num_int%10
    num_int=num_int//10
    summation+=(digit) ** (length)
if summation==num:
    print(num, "is an Armstrong number")
else:
    print(num,"is not an Armstrong number") 



Built by [Vamsi Krishna][lk]

[lk]:https://github.com/vamshikrishna10
