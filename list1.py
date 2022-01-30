fruits = ['Orange','Mango','Kiwi','Graps','Apple']
print(fruits)
fruits.insert(1,'Pinapple')
fruits.append("Banana")
fruits.append("coconut")
fruits.insert(0,"cherry")
fruits[0] = "water melon"
print(fruits)
del fruits[0]
print(fruits[0])
print(fruits[0:3])
print(fruits[3:])
print(fruits*2)
vegis = [] #empty list
vegis.append("Potato")
vegis.append("Tomato")
vegis.append("Onion")
vegis.append("Garlic")
print(vegis)
fruits_vegis = fruits + vegis #it will create new list 
print(fruits_vegis)