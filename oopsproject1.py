class Check:
	def __init__(self,number1,number2,number3):
		self.number1= number1
		self.number2 = number2
		self.number3 = number3
	
	def largest(self):
		if self.number1 >= self.number2 and self.number1 >= self.number3  :
			return f"Largest = {self.number1}"
		elif self.number2 >= self.number1 and self.number2 >= self.number3 :
			return f"Largest = {self.number2}"
		elif self.number3 >= self.number2 and self.number3 >= self.number1 :
			return f"Largest = {self.number3}"
			
	def smallest(self):
		if self.number1 <= self.number2 and self.number1 <= self.number3 :
			return f"Smallest = {self.number1}"
		elif self.number2 <= self.number1 and self.number2 <=self.number3 :
			return f"Smallest  = {self.number2}"
		elif self.number3 <=self.number2 and self.number3 <= self.number1 :
			return f"Smallest = {self.number3}"
	
	def equal(self):
		if self.number1 == self.number2 or self.number2 == self.number3 or self.number1 == self.number3 :
			return "Two numbers are equal"
		else:
			return "No two numbers are equal "

number1 = int(input("Enter number :",))
number2 = int(input("Enter number :",))
number3= int(input("Enter number :",))

comparison = Check(number1,number2,number3)
print(comparison.largest())
print(comparison.smallest())
print(comparison.equal())
