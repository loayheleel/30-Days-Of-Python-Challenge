# Day 5: 30 Days of python programming
# Exercise: Level 1
# Questions 1 ---> 25
list_1        = []
list_2        = ['paper','pen','book','ruler','compass']
length_list_2 =len(list_2)
print('The first item in the list is',list_2[0],'While the middle item is',list_2[2],'And the last item is',list_2[4])
mixed_data_types =['Loay',23,186,False,'0 Null Way']
it_companies=['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print('Here is a list for the biggest companies',it_companies)
print('The number of companies in the list is',len(it_companies))
print('The first company in the list is',it_companies[0],'While the middle company  is',it_companies[3],'And the last company',it_companies[6])
it_companies[3]='Samsung'
print('The list after modification is',it_companies)
it_companies.append('HP')
print('The new list is',it_companies)
it_companies.insert(6,'Nvidia')
it_companies[3] = it_companies[3].upper()
print('The modified list is',it_companies)
joined_list='#; '.join(it_companies)  
print('The joined list is',joined_list)
verdict_1='Nvidia'in it_companies
print('Is Nvidia present in the IT companies list?',verdict_1)
it_companies.sort()
print('The IT Companies list sorted in ascending order will be',it_companies)
it_companies.reverse()
print('The IT Companies list sorted in descending order will be',it_companies)
del it_companies[:3]
print('After removing some companies the list will be',it_companies)
del it_companies[-3:]
print('After removing more companies the list will be',it_companies)
it_companies.pop(1)
print('After further removing, the list will be',it_companies)
it_companies.pop(1)
print('After further removing, the list will be',it_companies)
it_companies.clear()
print('After removing all companies, the list will be',it_companies)
del it_companies
# Questions 26 & 27
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
complete_list= front_end + back_end
print('After merging both lists, the list will be',complete_list)
variable_full_stack=complete_list.copy()
variable_full_stack.insert(5,'Python')
variable_full_stack.insert(6,'SQL')
print('The updated list is',variable_full_stack)
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print('The ages after being sorted is',ages)
min_age= min(ages)
max_age= max(ages)
print('The maximum age in the list is',max_age)
print('The minimum age in the list is',min_age)
ages.append(min_age)
ages.append(max_age)
ages.sort()
print('The new age list is',ages)
age_median_1=ages[5]
age_median_2=ages[6]
median_age=(age_median_1+age_median_2)/2
print('The median of the ages list is',median_age)
total=sum(ages)
n=len(ages)
average_age=total/n
print('The average of the ages list is',average_age)
range=max_age-min_age
print('The range of the ages list is',range)
value_1   =abs(min_age-average_age)
value_2   =abs(max_age-average_age)
difference=abs(value_2-value_1)
final_verdict_1=value_1>value_2
final_verdict_2=value_2>value_1
print('Is the first value greater than the second value?',final_verdict_1)
print('Is the second value greater than the second value?',final_verdict_2)
print('The difference between both values is',difference)
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
n_2=len(countries)
index_middle=(len(countries)-1)/2
integer_mid=int(index_middle)
middle_country=countries[integer_mid]
print('Therefore,the middle country is',middle_country)
integer_mid_after=integer_mid+int(1)
First_list  = countries[0:integer_mid_after]
Second_list = countries[integer_mid_after:n_2]
print('The first part of the list is',First_list)
print('The second part of the list is',Second_list)
countries_other=['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first_country,second_country,third_country,*scandic = countries_other
print('The first country in the list is',first_country)
print('The second country in the list is',second_country)
print('The third country in the list is',third_country)

print('The rest of the countries (scandic) in the list is',scandic)
