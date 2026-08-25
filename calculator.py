a = float(input("Enter number :",))
op = input("Select one of four (+,-,*,/) :",)
b = float(input("Enter number :",))

if op == "+":
	print(f"Sum = {a+b}")
elif op == "-":
	print(f"Sum = {a-b}")
elif op == "*":
	print(f"Sum = {a*b}")
elif op == "/":
	if b == 0 :
		print("Division by zero impossible")
	else :
	    print(f"Sum = {a+b}")
	 
else:
	print("Invalid operator")		