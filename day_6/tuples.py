# Day 6: 30 Days of python programming
# Exercise: Level 1
# Questions 1 ---> 5
empty_tuple = tuple()
bros = ('Marco','Jeffrey')
sis  = ('Sophia','Tana')
print('The tuples of brothers is',bros)
print('The tuples of sisters is',sis)
siblings= bros + sis
print('The tuples of siblings is',siblings)
print('I have',len(siblings),'siblings')
siblings_list=list(siblings)         # You can modify a tuple converting it to a list, modify it , then converting it back to a tuple
siblings_list.append('Maria')
siblings_list.append('Paul')
family_members=tuple(siblings_list)
print('The tuples of the family members is',family_members)
# Exercise: Level 2
# Question 1
sib_1,sib_2,sib_3,sib_4,*Parents=family_members
print('My first sibling is',sib_1)
print('My second sibling is',sib_2)
print('My third sibling is',sib_3)
print('My fourth sibling is',sib_4)
print('My parents are',Parents)
# Questions 2 ---> 6
fruits=('Apple','Pineapple','Pear')
vegetables=('Cucumber','Cabbage','Lettuce')
animal_products=('Milk','Cheese','Yogurt')
food_stuff_tp=fruits+vegetables+animal_products
food_stuff_lt=list(food_stuff_tp)
food_stuff_lt.pop(4)
print('The new list is',food_stuff_lt)
del food_stuff_lt [-3:]
print('The new list after removing the last three items is',food_stuff_lt)
del food_stuff_lt [:3]
print('The new list after removing the first three items is',food_stuff_lt)
del food_stuff_lt
del food_stuff_tp
# Question 7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
verdict_1='Estonia' in nordic_countries
verdict_2='Iceland' in nordic_countries
print('Does Estonia exist in the Nordic Countries?',verdict_1)
print('Does Iceland exist in the Nordic Countries?',verdict_2)