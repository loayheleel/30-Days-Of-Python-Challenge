# Day 13: 30 Days of python programming
# Question 1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_zeros=[i for i in numbers if i<0]
print(negative_zeros)
# Question 2
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
list_flat=[number for row in list_of_lists for number in row]
list_flat_2=[number for row in list_flat for number in row]
print(list_flat_2)
# Question 3
list_seq=[(i,1,i**2,i**3,i**4,i**5,i**6) for i in range(0,11)]
for row in list_seq:
    print(row)
# Question 4
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
countries_list=[[country[0][0].upper(),country[0][0][:3].upper(),country[0][1].upper()] 
for country in countries]
print (countries_list)
# Question 5
countries_list_2=[{'counrty':country[0][0].upper(),'city:':country[0][1].upper()} 
for country in countries]
for row in countries_list_2:
    print(row)
# Question 6
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
names_list=[' '.join(name[0]) for name in names]
print(names_list)
# Question 7
x1=2
x2=-3
y1=4
y2=1
m=lambda x_1,x_2,y_1,y_2:(y_2-y_1)/(x_2-x_1)
slope_1=m(x1,x2,y1,y2)
c=lambda x_1,y_1,slope: y_1-(slope*x_1)
print('The y-intercept of the line is',c(x1,y1,slope_1))
print('The slope of the line is',slope_1)