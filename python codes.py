# to find whether a numbe3r is odd or not
def fun2(y):
    if y>=0:
        print("{} is a positive no".format(y))
    else:
        print("{} is a negative no".format(y))
a=int(input("enter a no: "))
fun2(a)


#to find whether a no is prime or not
num=int(input("Enter a number: "))
if num > 1:
    # Iterate from 2 to n / 2
    for i in range(2, int(num/2)+1):
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")