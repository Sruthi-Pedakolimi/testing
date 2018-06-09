num=int(input("Enter the number to check"))
def prime(n):
    count=0
    for i in range(2,n):
        if n%i==0:
            count=0
            break
        else:
            count=count+1
    return count

prime=prime(num)
if prime>0:
    print("The given number ",num," is a prime number")
else:
    print("The given number ", num, " is not a prime number")