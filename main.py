# def greet():
#   return "Hello Odala"

#=====================
#functions with parameters

# def greet(name):
  
#   '''
#   Greet a person passed in as as argument
#   name: a name of a person to greet
#   '''
#   return f"Hello {name}, Good Morning"

# print(greet("Felix"))
# print(greet("Bob"))
# print(greet("Adriana"))

#help(greet)

'''
Arbitrary parameters
'''

# def fruits(*names):
#   '''
#   Accepts unknown number of fruit names and prints each of them
#   name: list of fruits
#   '''
#   for fruit in names:
#     print(fruit)

# fruits("Oranges", "Bananas", "Apples", "Grapes")

# '''
# keyword parameters

# '''
# def greet(name, msg):
#   '''
#   Function Greets a person with a given message
  
#   name: name of person to greet
#   msg:message to gret the person with

#   '''

#   return f"Hello {name}, {msg}"
# #print(greet("Odala", "Good Morning"))
# #print(greet("Good Morning", "Odala"))

# print(greet(name="Odala", msg="Good Morning"))

# print(greet(msg="Good Morning", name="Bob"))

# '''
# Arbitrary keyword parameters
# '''

# def person(**student):
#   # print(type(student))
#   # print(student)
#   for key in student:
#     print(student[key])


# person(fname="Odala", lname="Regas", subject="Python")


# '''
# Default parameter variables
# '''

# def greet(name='David'):
#   return f"Hello, {name}"

# print(greet('Dayana'))


# '''
# pass statement
# '''

# def greet():
#   pass

# '''
# recursion
# '''

# def factorial_recursive(n):
#   '''
#   Multiply a gien by every number (n) less than it down to 1 in a factorial way. n ois the highest starting number
#   '''
#   if n==1:
#     return True

#   else:
#     return n * factorial_recursive(n-1)

# print(factorial_recursive(5))


if 7>5: print('yes it si')