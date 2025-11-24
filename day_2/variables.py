# Day 2: 30 Days of python programming
# Exercises: Level 1
# Questions 3 --> 13
first_name = 'Loay'
last_name  = 'Heleel'
full_name  =  first_name+ ' '+ last_name
country    = 'Egypt'
city       = 'Alexandria'
age        =  23
is_married, is_true, is_lights_on = False , True , False
# Exercises: Level 2
# Questions 1 --> 3
print(type(first_name)) 
print(type(last_name))
print(type(full_name))  
print(type(country))    
print(type(city))      
print(type(age))       
print(type(is_married)) 
print(type(is_true))
print(type(is_lights_on))
length_first = len(first_name) 
length_last  = len(last_name)
difference= ((length_first-length_last)**(2))**(0.5) # Both exponentials used inorder to obtain the absolute value of the difference (Excluding negative results)
diff_characters = int(difference)           
print('My first name has ',length_first,'characters')
print('My last name has ',length_last,'characters')
print('There is ',diff_characters,'characters difference between my first and last name')
# Questions 4 --> 11
num_one = 5 
num_two = 4
total= num_one + num_two
diff =num_two - num_one
product= num_two * num_one
division= num_one / num_two
remainder= num_one % num_two
exp= num_one ** num_two
floor_division= num_one // num_two
# Question 12
radius            = 30
pi                = 3.141592653589793
area_of_circle    = pi * (radius ** 2)
circum_of_circle  = 2 * pi * radius
print('the area of the circle is',area_of_circle,'meters squared')
print('the circumference of the circle is',circum_of_circle,'meters')
r_input=input('Enter the radius of the circle')
r=float(r_input)
area              = pi * (r ** 2)
print('the area of the circle is',area,'meters squared')
first_name_input   = input('What is your first name')
last_name_input    = input('What is your last name')
country_input      = input('Where are you from') 
age_input          = input('How old are you')
# Question 13
help('keywords') 
