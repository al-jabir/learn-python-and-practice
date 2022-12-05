for i in range(9):
    print(i,' I want to be a great programmer.')
    
arr = [3,5,6,7,8,9,10,11,12,13,14]
sum = 0
for i in range(len(arr)):
    sum+= arr[i]
    print('total sum is: ',sum)
    
import turtle

turtle.shape('turtle')
turtle.speed(1)

for i in range(4):
    turtle.forward(100)
    turtle.left(90)
    
turtle.exitonclick()


res =  0
num = 1

for j in range(50):
    res+= num
    num+=1
print(res)

res2 = 0

for nums in range(98):
    res2+= nums
    
print('The result is: ', res2)

result = 0
for num in range(100):
    if num % 5 == 0:
        print(num)
        result += num
print("Sum is:", result)

result2 = 0
for nm in range(5, 101,5):
    print(nm)
    result2 += nm
print('total sum is now:',result2)


# list of loops

saarc = ["Bangladesh", "Afghanistan", "Bhutan", "Nepal", "India", "Pakistan", "Sri Lanka"]

for country in saarc:
    print(country,' is a member of SAARC')


li = list(range(9))
print(li)

li2 = list(range(5,21,5))
print(li2)
