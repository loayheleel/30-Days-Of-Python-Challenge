# Day 3: 30 Days of python programming
# Questions 1 --> 3
age              = 23
height           = 186.0
complex_variable = 5-10j
print('my age is',age,'and my height is',height)
# Question 4 
b     = float(input('Enter the base of the triangle'))
h     = float(input('Enter the height of the triangle'))
# The data type input by user is string. So it is needed to convert it to float to carry on the calculations

area  = 0.5*b*h
print('the area of the triangle is',area)
# Question 5
a             = float(input('Enter the first side of the triangle'))
b             = float(input('Enter the second side of the triangle'))
c             = float(input('Enter the third side of the triangle'))
perimeter     = a+b+c
print('the perimeter of the triangle is',perimeter)
# Question 6
l              = float(input('Enter the length of the rectangle'))
w              = float(input('Enter the width of the rectangle'))
area_rect      = l*w
perimeter_rect = 2*(l+w) 
print('the area of the rectangle is',area_rect)
print('the perimeter of the rectangle is',perimeter_rect)
# Question 7
r              = float(input('Enter the radius of the circle'))
circum         = 2*3.14*r
area_circle   = 3.14*(r**2)
print('The circumference of the circle is',circum)
print('The area of the circle is',area_circle)
# Question 8
# Line Equation : y= 2x-2
m=2       # Coefficient of x in the equation 
x_sub = 0 # In order to find the y-intercept of the line
y_sub = 0 # In order to find the x-intercept of the line
y_intercept= 2*(x_sub)-2
x_intercept=(y_sub+2)/2
print('The slope of the line y=2x-2 is',m)
print('The x-intercept of the line y=2x-2 is',x_intercept)
print('The y-intercept of the line y=2x-2 is',y_intercept)
# Question 9 
# Point 1 (2,2) and Point 2 (6,10)
x_1=2
x_2=6
y_1=2
y_2=10
m_2=(y_2-y_1)/(x_2-x_1)
d  =(((x_2-x_1)**2)+((y_2-y_1)**2))**0.5
print('The slope of the line is',m_2)
print('The distance between the two points is',d)
# Question 10
print('Is the slope of line 1 = the slope of line 2?',m==m_2)
print('Is the slope of line 1 greater than the slope of line 2?',m>m_2)
print('Is the slope of line 1 less than the slope of line 2?',m<m_2)
# Question 11
# Curve equation y= x^2 + 6x +9
# Since all terms in the equation have positive signs, then the value of x that makes y=0 is negative 
x_sub1    = -1
x_sub2    = -2
x_sub3    = -3
y_value_1 = ((x_sub1)**2)+6*(x_sub1)+9
y_value_2 = ((x_sub2)**2)+6*(x_sub2)+9
y_value_3 = ((x_sub3)**2)+6*(x_sub3)+9
print('The value of x that makes y=0 is',x_sub3)
# Question 12
print('The length of the word python is',len('python'))
print('The length of the word dragon is',len('dragon'))
print('Is the length of dragon greater than the length of python?)',len('dragon')>len('python') )

# Question 13
print('Is on present in both words python and dragon?',('on' in 'dragon' ) and ( 'on' in 'python') )
# Question 14
statement_1= 'jargon'in ' hope this course is not full of jargon?'
print('Is jargon present in the sentence I hope this course is not full of jargon?',statement_1 )
# Question 15
print('There is no on in both python and dragon',('on' not in 'dragon') and ('on' not in 'python'))
# Question 16
p=len('python')
f=float(p)
s=str(f)
print('The length of the word python is',p)
print('The length of the word python in float is',f)
print('The length of the word python in string form is',s)
# Question 17
number   = float(input('Please enter a number'))
remainder= number%2
statement_4 = remainder == 0.0
print('Is the number even?',statement_4)
# Question 18
First_Calc = 7//3
Second_Calc= int(2.7)
statement_2= First_Calc == Second_Calc
print('Is the floor division of 7 by 3 = the integer of the number 2.7?',statement_2)
# Question 19
type_1= 10
type_2='10'
statement_3= type(type_1) == type(type_2)
print('Is the type of',type_1,'the same as the type of',type_2,'?',statement_3)
# Question 20
print('Is the integer of 9.8 = 10?',int(9.8)==10)
# Question 21
hours         =float(input('Enter the number of work hours per week'))
rate          =float(input('Enter the amount you get paid in one hour'))
weekly_earning=hours*rate
print('You make',weekly_earning,'per week')
# Question 22
years= float(input('Enter your age'))
seconds= years*(12*30*24*60*60)
print('You have lived',seconds,'seconds')
years_max=100
seconds_max=years_max*(12*30*24*60*60)
print('You have can live upto',seconds_max,'seconds')
# Question 23
print('1 1 1 1 1')
print('2 1 2 4 8')
print('3 1 3 9 27')
print('4 1 4 16 64')
print('5 1 5 25 125')
