bn = 'Bangladesh'
bn2 = 'Bangladesh'

# true

print(bn == bn2)

bn3 = 'Belarus'

# false

print(bn3 != bn)

# false

print(bn2 ==bn3)

# str length

print(bn[:6])
print('str len of :',len(bn))

# check last length

print(bn[9])

# user result mark show of your exam

marks = input('Please enter your mark number: ')
marks = int( marks)

if marks >= 80:
    grade = 'A+'
elif marks >= 70:
    grade = 'A'
elif marks >= 60:
    grade = 'A-'
elif marks >= 50:
    grade = 'B'
else:
    grade = 'F'
    
print('Your grad is ',grade)
    
    # leap Year
year = input()
    
if year % 4 != 0:
    print("No")
else:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Yes")
        else:
            print("No")
    else:
        print("Yes")