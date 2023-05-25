"""
User will input (3ages).Find the oldest one

"""
ages = []
count = 0
while count < 3:
    age = int(input("Enter age:  "))
    ages.append(age)
    count += 1

print("The biggest age is ", max(ages))

age1 = int(input("Enter age:  "))
age2 = int(input("Enter age:  "))
age3 = int(input("Enter age:  "))

if age1 > age2 and age1 > age3:
    print("Bigger age ", age1)
elif age1 < age2 and age1 < age3:
    if age2 > age3:
        print("Bigger age ", age2)
    else:
        print("Bigger age ", age3)

age1 = int(input("Enter age:  "))
age2 = int(input("Enter age:  "))
age3 = int(input("Enter age:  "))

max = age1
if age2 > max:
    max = age2
if age3 > max:
    max = age3

print("Bigger age: ", max)


