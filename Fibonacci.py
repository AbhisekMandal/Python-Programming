num = int(input("Enter the range."))
a, b = 0, 1
print(a,b, end=" ")
for i in range(num):
    sum = a+b
    print(sum, end=(" "))
    a = b
    b = sum

