# Day 8: 30 Days of python programming
# Question 1 & 2
dog={}
dog['name']=  'Stormy'
dog['color']= 'Black and White'
dog['breed']= 'Husky'
dog['legs'] = 4
dog['age']  = 2
# Question 3 -----> 11
student={}
student['first_name']='Loay'
student['last_name']='Heleel'
student['gender']='Male'
student['age'] = 23
student['marital status']=False
student['skills']=['Python','PLC']
student['country']='Egypt'
student['city'] = 'Alexandria'
student['address']= {}
student['address']['street']='Fake Street'
student['address']['zipcode']='0016'
print('The dictionary of the student is',student)
len(student)
value_1=student.get('skills')
print('The skills that the student have is',value_1)
print('The data type of the skills that the student have is',type(student['skills']))
student['skills'].append('Arduino')
print('The new dictionary is',student)
keys= student.keys()
values= student.values()
print('The keys of the student dictionary is \n',keys,'\n While the values of the student dictionary is \n',values)
tuples_list=student.items()
print('The dictionary of the student in form of lists of tuples is',tuples_list)
student.pop('marital status')
print('The new dictionary will be',student)
del dog