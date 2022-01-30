person = {'name':'ankit','surname':'patel','age':35,'weight':75.11,'gender':True}
print(person)
person['city'] = 'Bhavnagar'
person['ismarried'] = True
person['name'] = 'ANKIT'
person['age'] = 36
print(person)
del person['city']
print(person)
family = [] #list
family.append(person)
print(family)