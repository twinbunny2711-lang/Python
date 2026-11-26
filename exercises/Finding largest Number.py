a = int(input("Enter First number"))
b = int(input("Enter second Number"))
c = int(input("Enter third Number"))
if a>= b and a>=c:
    print("A is the largest number. ", a)
elif b>=a and b>=c:
    print("B is the largest number. ", b)
else:
    print("C is the largest number. ", c)