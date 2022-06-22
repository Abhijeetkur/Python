import math
num = int(input("Enter number: "))
def prime_number(n):
    if(n==1):
        return False

    elif(n==2):
        return True

    elif(n>2 and n%2==0):
        return False

    else:
        max_div = math.floor(math.sqrt(n))
        for i in range(3,1+max_div,2):
            print(i)
            if(n%i==0):
                return False
        return True

print(prime_number(num))