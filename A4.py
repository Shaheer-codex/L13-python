def sq(x):
    peri = 4*x
    return peri

def rect(l,b):
    peri = 2*(l+b)
    return peri

x = int(input("Enter the length of sides: "))
print("perimeter of square is",sq(x))

l = int(input("Enter the length: "))
b = int(input("Enter the breadth: "))
print("perimeter of rectangle is",rect(l,b))