
n = int(input("Enter a number: "))
rsum = 0
while n != 0:
    r = n % 10
    rsum = rsum * 10 + r
    n = n // 10
print(rsum)
