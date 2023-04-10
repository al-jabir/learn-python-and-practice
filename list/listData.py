myList = [2, 5, 9, 13, 'king', 'mafia', 'gangster', 'hacker']

# check index of mylist data store
print(myList[2:6])
print(myList[:6])
print(myList[5:])

# chcke index of mylist data type

print(type(myList[2]))
print(type(myList[5]))

# update index of mylist data
myList[2] = 98.9
myList[5] = 'software development'

# check output of myList
print(myList)

# check length of myList

print(len(myList))

# add new index to myList

myList.append('devOps Engineer')
myList.insert(0, 'Cloud Engineer')
print(myList)

# again check length of myList

print(len(myList))

# another add item to myList

myList.extend(['Google', 'Microsoft', 'Meta', 'IBM'])

# check length of myList

print(len(myList))

# check out of mylist again
print(myList)


# remove item from myList

myList.remove('devOps Engineer')

print(myList)

# check mylist count

print(myList.count('software development'))

# print(myList.sort())
myList.reverse()
print(myList)
