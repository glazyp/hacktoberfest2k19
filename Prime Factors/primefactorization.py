num=int(input("Enter an integer:"))
print("Factors of the integer are:")
i=1
while(i<=num):
    k=0
    if(num%i==0):
        j=1
        while(j<=i):
            if(i%j==0):
                k=k+1
            j=j+1
        if(k==2):
            print(i)
    i=i+1


    
   
