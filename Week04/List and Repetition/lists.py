from array import array

# LIST
name = ['Tahiry', 'Amber']
name.append('Ariela')
name.append('Keanu')
name.append('Nakoa')
print(name)
print(name[0:2]) # parents
print(name[2:5]) # kids

# ARRAY
scores = array('i')
scores.append(97)
scores.append(99)
print(scores)
print(scores[1])

# DICTIONARY
person = {'first': 'Tahiry'}
person['last'] = 'Ratsimanohatra'
person['last'] = 'Rakotomalalasoa'
print(person)
print(person['last'])
print(person.exists('last'))