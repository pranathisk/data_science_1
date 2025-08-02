"""
a = 33
b = 200
c = 20
if a > b:
    print('a is greater than b')
elif b > c:
    print('b is greater than c')
else :
    print('both conditions are not true')
"""

"""
#task 1
score = int(input("Enter your score(0-100): "))
if score >= 90:
    print("A")
    print("score",score)
elif score >= 80:
    print("B")
    print("score",score)
elif score >= 70:
    print("C")
    print("score",score)
else:
    print("F")
    print("score",score)
"""
"""
#task 2
age= int(input("Enter your age(0-60): "))
if age <= 14:
    print("Kids Ticket")
    print("age",age)
elif (age>=15)|(age<=40) :
    print("Regular Ticket")
    print("age",age)
else:
    print("Senior Citizen Ticket")
    print("age",age)
"""
"""
#task 3
temp= int(input("Enter your temp(0-50): "))
if (temp <=0) :
    print('stay inside')
elif (temp>=20)and(temp<=35) :
    print('wear a jacket')
elif (temp<=40) :
    print("is hot, but can go out")
else :
    print('very hot')
"""

#loops

"""
a = 1
while a < 10 :
    print(a)
    a += 1
print("loop ends")
"""
"""
year = 2000
print("All leap years (2000-2025) :")
while year < 2025 :
    print(year)
    year += 4
print('Ends here')
"""
"""
salary = 20000
# print("All leap years (2000-2025) :")
while salary < 25000:
    print(salary)
    salary += 2500
print('Ends here')
"""
"""
#forloop

fruits = ["apple","banana","cherry"]
for x in fruits:
    print(x)
"""