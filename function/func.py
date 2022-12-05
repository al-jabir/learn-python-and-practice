def add(a,b):
    return a + b
print(add(4,5) )

def min(n4,n2):
    return n4 - n2
res = min(5,10)
print(res)

def max(m,n):
    if m <= n:
        return m
    else:
        return n
res2 = max(5,15)
print(res2)

def multiply(x,y):
    return x*y
res3 = multiply(5,9)
print(res3)

def add_numbers(number):
    rest = 0
    for number in number:
        rest+= number
    return rest
rest = add_numbers([5,3,2,5,6,7,15,20])
print(rest)

import turtle


def draw_square(side_length):
    for i in range(4):
        turtle.forward(side_length)
        turtle.left(90)

counter = 0
while counter < 90:
    draw_square(100)
    turtle.right(4)
    counter += 1

turtle.exitonclick()