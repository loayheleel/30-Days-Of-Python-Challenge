# Day 7: 30 Days of python programming
# Exercise: Level 1
# Questions 1 ---> 5
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print('The length of the IT Companies set is',len(it_companies))
it_companies.add('Twitter')
print('After adding a company the set will be',it_companies)
new_it_companies= {'Samsung','Lenovo','ASUS','HP'}
it_companies.update(new_it_companies)
print('After adding more companies the set will be',it_companies)
it_companies.remove('Facebook')
print('After removing a company the set will be',it_companies)
print('\'remove\' outputs an error if the item needed to be removed is not present')
print('While \'discard\'  does not output an error if the item needed to be removed is not present')
# Exercise: Level 2
# Questions 1 ---> 7
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
C=A.union(B)
print('The new set of numbers will be ',C)
set_1= A.intersection(B)
print('The intersection between sets A and B is',set_1)
verdict_1=A.issubset(B)
verdict_2=A.isdisjoint(B)
print('Is set A subset of set B?',verdict_1)
print('Are sets A and B disjoint sets?',verdict_2)
D=B.union(A)
E=C       # Since joing A with is done already in Question 1
print('After joining A and B the result will be\n',E,'\nand after joining B and A the result will be\n',D) 
print('Both results are equal so the order in union doesnt matter')
del A
del B
del C
del D
del E
# Exercise: Level 3
# Question 1
age = [22, 19, 24, 25, 26, 24, 25, 24]
age_set=set(age)
L_1=len(age)
L_2= len(age_set)
difference=abs(L_1-L_2)
verdict_A=L_2>L_1
verdict_B=L_2<L_1
print('The length of the list is',L_1)
print('The length of the set is',L_2)
print('Is the length of the set greater than the length of the list',verdict_A)
print('Is the length of the set less than the length of the list',verdict_B)
print('The difference between both lengths is',difference)
# Question 2
print('Strings are a sequence of characters enclosed in a single/double/triple quotes')
print('List are a collection of different types of data that is ordered , can be modified and allows the presence of duplicates ')
print('Tuples are a collection of different types of data that is ordered ,cannot be modified and allows the presence of duplicates')
print('Sets are un-indexed collection of different types of data that is unordered, unchangeable, disallows the presence of duplicates')
# Question 3
sentence='I am a teacher and I love to inspire and teach people'
print(sentence)
sentence_list=sentence.split()
sentence_set=set(sentence_list)
length=len(sentence_set)
print('The number of unique words in the sentence  is',length)
