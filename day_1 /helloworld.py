# Exercise : Level 2
# Question 1 : Python Version
import sys
print('Python version')
print(sys.version)

# Question 2 : Operations
print(3+4)  # Addition
print(3-4)  # Subtraction
print(3*4)  # Multiplication
print(3%4)  # Modulus
print(3/4)  # Division
print(3**4) # Exponential
print(3//4) # Floor Division

# Question 3 : Strings
print('Loay')
print('Heleel')
print('Egypt')
print('I am enjoying 30 days of python')

# Question 4 : Data Types
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4j))
print(type(['Loay','Heleel','Egypt']))

# Exercise : Level 3
# Question 1 : Examples on Data Types
print(-10)                                                          # Integer
print(7.15)                                                         # Float
print(2+7j)                                                         # Complex
print('Learning Python is easy')                                    # String
print(True)                                                         # Boolean
print(['Blue','Red','Black'])                                       # List
print((2,4,6,8,10,12))                                              # Tuple
print({2,4,6,8,10,12})                                              # Set
print({'FirstName' :'Loay','LastName':'Heleel','Country':'Egypt'})  # Dictionary

# Question 2 : Euclidian distance between 2 points 
# Point 1 (2,3)
# Point 2 (10,8)
x_1 = 2
x_2 = 10
y_1 = 3
y_2 = 8

Distance = (((x_2-x_1)**(2))+((y_2-y_1)**(2)))**(0.5)
print('The Euclidean Distance between points 1 and 2 is',Distance)
