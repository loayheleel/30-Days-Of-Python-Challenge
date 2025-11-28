# Day 4: 30 Days of python programming
# Question 1
first_word  = 'Thirty'
second_word = 'Days'
third_word  = 'Of'
forth_word  = 'Python'
sentence= first_word + ' ' + second_word + ' ' +third_word + ' ' +forth_word+ ' '
print(sentence)
# Question 2
first_word_2  = 'Coding'
second_word_2 = 'For'
third_word_2  = 'All'
sentence_2= first_word_2 + ' ' + second_word_2 + ' ' +third_word_2 + ' ' 
# Questions 3 ---> 34
company='Coding For All'
print(company)
print('The length of the company string is',len(company))
print('The company string in uppercase is',str.upper(company))
print('The company string in lowercase is',str.lower(company))
print('The company string capital in the first word only is',str.capitalize(company))
print('The company string in Title Case form is',str.title(company))
print('The company string after swapping cases is',str.swapcase(company))
print('The company string after removing the first word is',company.strip('Coding'))
print('Is Coding present in the company string?',company.find('Coding')) # If present, it should output the index.Other -1 is the output
print('The company string after replacing \'coding\' with \'python\' is',company.replace('Coding','Python'))
company_2='Python For Everyone'
print('The second company string after replacing \'everyone\' with \'all\' is',company_2.replace('Everyone','All'))
print('The company string after seperation is',company.split( ))
company_3="Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print('The third company string after seperation is',company_3.split(', '))
print('The character at index 0 in the company string is',company[0])
print('The character at the last index  in the company string is',company[-1])
print('The character at the index 10  in the company string is',company[10])
first_part=company_2[0:6]
print('The abbrevation of the second company string is',company_2[0]+company_2[7]+company_2[11])
print('The abbrevation of the company string is',company[0]+company[7]+company[11])
print('The position of C first occurence in the company string is',company.find('C'))
print('The position of F first occurence in the company string is',company.find('F'))
company_4= 'Coding For All People'
print('The position of l last occurence in the forth company string is',company_4.rfind('l'))
company_5= 'You cannot end a sentence with because because because is a conjunction'
print('The position of the word \'because\' first occurence in the fifth company string is',company_5.find('because'))
print('The position of the word \'because\' last occurence in the fifth company string is',company_5.rfind('because'))
print('the fifth company string after slicing out \'because because because\' is',company_5[0:30]+' '+company_5[-16:])
print('Does the company string start with a substring \'Coding\'?',company.startswith('Coding'))
print('Does the company string end with a substring \'Coding\'?',company.endswith('Coding'))
company_6='   Coding For All      '
print('The sixth company string after removing the spaces is',company_6[3:9]+' '+company_6[10:13]+' '+company_6[14:17])
first_variable ='30DaysOfPython'
second_variable='thirty_days_of_python'
verdict_1=first_variable.isidentifier()
verdict_2=second_variable.isidentifier()
print('The first one is a',verdict_1,'variable while the second one is a',verdict_2,'variable')
list_1=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined='# '.join(list_1)     
print('The list separated with spaces and hashtags is',joined)
phrase='I am enjoying this challenge.I just wonder what is next.'
phrase_sep='\nI am enjoying this challenge.\nI just wonder what is next.'
print('The phrase after seperation is',phrase_sep)
phrase='NameAgeCountryCityAsabeneh250FinlandHelsinki'
phrase_2_sep='\nName\t\tAge\t\tCountry\t\tCity\nAsabeneh\t250\t\tFinland\t\tHelsinki' #\t is added twice to adjust the table columns
print('The table after arrangement is',phrase_2_sep)
# Question 35
radius=10
pi=3.14
area=pi*radius**2
print('The area of a circle with a radius {} is {} meters squared'.format(radius,area))
x=8
y=6
print('{} + {} = {}'.format(x,y,x+y))
print('{} - {} = {}'.format(x,y,x-y))
print('{} * {} = {}'.format(x,y,x*y))
print('{} / {} = {:.2f}'.format(x,y,x/y))
print('{} % {} = {}'.format(x,y,x%y))
print('{} // {} = {}'.format(x,y,x//y))

print('{} ** {} = {}'.format(x,y,x**y))

