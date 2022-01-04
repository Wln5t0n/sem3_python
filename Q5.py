#student class
class student:
	def __init__(self, roll,name): #to initialize roll and name
		self.roll=roll
		self.name=name
	def display(self): # i. to display student's information
		print(self.roll,self.name,self.age,self.marks)
	def setAge(self): # ii. to set age of the student
		self.age=int(input("Enter age : "))
	def setMarks(self): # iii. to set marks of the student
		self.marks=int(input("Enter marks : "))

s1=student(111,"Aarish") #creating objects
s2=student(222,"Manali")
#calling methods
s1.setAge()
s1.setMarks()
s2.setAge()
s2.setMarks()
s1.display()
s2.display()