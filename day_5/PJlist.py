# Slicing Items from a List
from statistics import median


fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits[0:3])
print(fruits[0:])
print(fruits[:3])
print(fruits[::3])
print(fruits[0:1:3])
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits) # ['lemon', 'mango', 'orange', 'banana']
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages) # [24, 25, 24, 26, 25, 24, 19, 22]
# To sort lists we can use sort() method or sorted() built-in functions. The sort() method reorders the list items in ascending order and modifies the original list. If an argument of sort() method reverse is equal to true, it will arrange the list in descending order.
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits) 
fruits = ['banana', 'orange', 'mango', 'lemon']
print(sorted(fruits))
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits = sorted(fruits,reverse=True)
print(fruits) 
empty=[]   
print(empty)  
more_than=[1,2,3,4,5,6] 
first,middle,last=more_than[0],+more_than[2], +more_than[-1]
print(first,middle,last)
mixed_data_types=["phelisia","single",5,2,"zimmerman/mathare",23]
print(mixed_data_types)
it_companies=["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle"," Amazon"]
uppercase=it_companies[0].upper()
print(it_companies)
neew='#'.join(it_companies)
print(neew)
print(it_companies[0])
print(it_companies[4])
print(it_companies[-1])
it_companies.sort()
it_companies.reverse()
slice_companies=it_companies[4:]
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend (back_end)
print(front_end)
full_stack= ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'Express', 'MongoDB']
full_stack.insert(9,"SQL")
print(full_stack)
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sort the list and find the min and max age
Smallest=min(ages)
print(Smallest)
biggest=max(ages)
print(biggest)
add=Smallest+biggest
print(add)
ages.append(add)
print(ages)
medium=median(ages)
print(medium)
total_ages=sum(ages)
print(total_ages)
total_length=len(ages)
print(total_length)
average_age=total_ages/total_length
print(average_age)
range_ages=biggest-Smallest
print(range_ages)

contries_list=['Afghanistan',
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
  'Zimbabwe']
countries_length=len(contries_list)
print(countries_length)
middle_index = countries_length//2
first_list=first_half = contries_list[:middle_index]
print(first_list)
second_list=contries_list[:middle_index]
print(second_list)

