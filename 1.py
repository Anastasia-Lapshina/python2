maxi = -1
print("Enter a number ")
n = input()
isInt = True
try:
    n = int(n)
except ValueError:
    isInt = False
if isInt:
    n = abs(n)
    while n >= 0:
        x = n % 10
        n = n // 10
        if x % 2 == 0 and x > maxi:
            maxi = x
        if n == 0: 
            break
    if maxi >= 0:
        print("The greatest digit in the number is ", maxi)
    else:
        print("No even numbers found")
else:
    print("Invalid Data")
