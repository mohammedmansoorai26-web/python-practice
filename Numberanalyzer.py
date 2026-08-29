first = int(input("Enter first number :",))
second = int(input("Enter Second number:",))

#Type of first
print("---First number---")
if first%2 == 0 :
	print("Even")
else:
	print("Odd")
	
if first> 0 :
	print('Positive')
elif first<0 :
	print("Negative")
else:
	print("Zero")
print()
#Type of first
print("---Second number---")
if second%2 == 0 :
	print("Even")
else:
	print("Odd")
	
if second> 0 :
	print('Positive')
elif second<0 :
	print("Negative")
else:
	print("Zero")	
print()	
#Checking largest/smallest
print("---Comparison---")
if first > second:
	print("Largest =",first)
	print("Smallest = ",second)
elif second > first:
	print("Largest =",second)
	print("Smallest = ",first)
else:
	print("Both are equal")
	
	