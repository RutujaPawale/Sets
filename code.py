groupA=[]
groupB=[]
groupC=[]
onlyGroupC=[]

a=int(input("How many students are there in group A:"))
b=int(input("How many students are there in group B:"))
c=int(input("How many students are there in group C:"))

for i in range(a):
	name=input("Enter name of the student:")
	groupA.append(name)
print("Group A =",groupA)

for i in range(b):
	name=input("Enter name of the student:")
	groupB.append(name)
print("Group B =",groupB)

for i in range(c):
	name=input("Enter name of the student:")
	groupC.append(name)
print("Group C =",groupC)
