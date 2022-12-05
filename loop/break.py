while True:
    n = input("Please enter a number (0 to exit): ")
    n = int(n)
    if n == n:
        break
    print('Square of ',n, 'is', n*n)
    

while True:
    n = input("Please enter a positive number (0 to exit): ")
    n = int(n)
    if n < 0:
        print("We only allow positive number. Please try again.")
        continue
    if n == 0:
        break
    print("Square of", n, "is", n*n)
    
    terminate_program = False
while not terminate_program:
    number1 = input("Please enter a number: ")
    number1 = int(number1)
    number2 = input("Please enter another number: ")
    number2 = int(number2)

    while True:
        operation = input("Please enter add/sub or quit to exit: ")
        if operation == "quit":
            terminate_program = True
            break
        if operation not in ["add", "sub"]:
            print("Unknown operation!")
            continue
        if operation == "add":
            print("Result is", number1 + number2)
            break
        if operation == "sub":
            print("Result is", number1 - number2)
            break
        
        
for j in range(10):
    if j == 5:
        break
    print(j)