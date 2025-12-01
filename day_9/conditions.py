# Day 8: 30 Days of python programming
# Exercises : Level 1
# Question 1 
age=int(input('Please enter your age \n'))
diff=18-age
if diff!=1: # To determine whether the text 'year' is plural or singular
   text='years'
else:
   text='year'
if age >= 18:
   print('You are old enough to learn to drive')
else: 
   print('You need',18-age ,'more',text,'to learn to drive ')
# Question 2   
my_age   = int(23)
your_age = int(input('Enter your age\n'))
diff_age= abs(my_age-your_age)
if diff_age!=1:
   text_2='years'
else:
   text_2='year'
if my_age > your_age:
   print('I am',diff_age,text_2,'older than you')
elif my_age < your_age:
   print('You are',diff_age,text_2,'older than me')
else:
   print('Wow, We are both',my_age,'years old')
# Question 3
a=float(input('Please input the first number\n'))
b=float(input('Please input the second number\n'))
if a>b:
   print('a is greater than b')
elif a<b:
   print('a is smaller than b')
else:
   print('a is equal to b')
# Exercises : Level 2
# Question 1
grade=float(input('Please enter the score of the student\n'))
if grade>=90 and grade<=100:
   print('The grade of the student is A')
elif grade>=70 and grade<=89:
   print('The grade of the student is B')
elif grade>=60 and grade<=69:
   print('The grade of the student is C')
elif grade>=50 and grade<=59:
   print('The grade of the student is D')
elif grade>=0 and grade<=49:
   print('The grade of the student is F')
else:
   print('Invalid Score, please enter a score between 0 and 100')
# Question 2
month=input('Please input the month\n')
tuple_1=('September','October','November','september','october','november') # In case the user didnt write the month in captial letters
tuple_2=('December','January','February','december','january','february')
tuple_3=('March','April','May','march','april','may')
tuple_4=('June','July','August','june','july','august')
if month in tuple_1   :
   print('The season is Autumn')
elif month in tuple_2 :
   print('The season is Winter')
elif month in tuple_3 :
   print('The season is Spring')
elif month in tuple_4 :
   print('The season is Summer')
# Question 3
fruits = ['banana', 'orange', 'mango', 'lemon']
print('The fruit list is',fruits)
input_fruit=input('Please input a fruit\n')
if input_fruit in fruits:
   print('The fruit is already present in the list')
else:
   fruits.append(input_fruit)
   print('The new list will be',fruits)
# Exercises: Level 3
person={
    'first_name': 'Asabenah',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
if 'skills' in person:
   print('The middle skill is',person['skills'][2])
   verdict_1='Python' in person['skills']
   print('Can the person use Python?',verdict_1)
if 'Javascript' in person['skills'] and 'React' in person['skills'] and len(person['skills'])==2 :
   print('He is a front end developer')
elif 'Node'in person['skills'] and 'Python'in person['skills'] and 'MongoDB'in person['skills'] and len(person['skills'])==3 :
   print('He is a back end developer')
elif 'Node'in person['skills'] and 'React'in person['skills'] and 'MongoDB'in person['skills'] :
   print('He is a full stack developer')
else:
   print('unknown title')
if person['is_married']==True and person['country']=='Finland':
   text_4='is'
   print(person['first_name'],person['last_name'],'lives in', person['country'],'.', 'He',text_4 ,'married.')
       


