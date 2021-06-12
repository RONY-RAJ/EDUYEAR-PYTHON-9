name="rounak"
age="20"
salary= 141414.56

print(name,age,salary,sep="@")
print(name,age,salary,sep="")
print(name,age,salary,sep="\n")

print(name,age,salary,end="@")
print()
print(name,age,salary,end="")
print()

print("name :",name)
print("age :",age)
print("salary :",salary)

ex ="my name is {}, my age is {} and my salary is {}".format(name,age,salary)
print(ex)

str=f"my name is {name}, my age is {age} and my salary is {salary}".format(name,age,salary)
print(str)
