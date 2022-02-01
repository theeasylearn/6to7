a = int(input("Enter first number")) 
b = int(input("Enter second number")) 
c = int(input("Enter third number")) 

result = a==b and b==c
print(result)

result = a==b or b==c
print(result)

result = not(a==b and b==c)
print(result)
