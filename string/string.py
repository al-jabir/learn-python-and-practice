str = 'I love coding for Software Development'
print(str)

lens = len(str)
print(lens)

my_str = 'I i\'ll be kill you'
print(my_str)

# loop check for strings

country = 'England'
for c in country:
    print(c)
    
up = country.upper()
print(up)

import turtle

name = turtle.textinput("name", "What is your name?")
name = name.lower()
if name.startswith("mr"):
    print("Hello Sir, how are you?")
elif name.startswith("mrs") or name.startswith("miss") or name.startswith("ms"):
    print("Hello Madam, how are you?")
else:
    name = name.capitalize()
    str = "Hi " + name + "! How are you?"
    print(str)

turtle.exitonclick()