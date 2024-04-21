# age = 20
# name = input('What is your name? ')


# print(name)




#type conversion lesson


# birthyear = input("Enter your birth year: ")
#
#
# age = 2024 - int(birthyear)
#
# print(age)

##calc exercise

# first = input("Enter first number: ")
# second = input("Enter second number: ")
#
# print(float(first) + float(second))


#STRINGS LESSON

# course = 'Python for beginners'
# print(course.upper())
#
# print(course.find('y'))
#
# print(course.replace('for', '4'))
#
# print('Python' in course)

#ARITHMETIC OPERATIONS

# print(10+3)
# x=10
# x+=3
#
# print(x)

#OPERATOR PRECEDENCE

# x =(10+3)*2
# print(x)

#COMPARISON OPERATORS
# x = 3 > 2
# print(x)
#
# x = 3 == 2
#
# print(x)

#LOGICAL OPERATORS
# price = 5
# print(price>10 and price<30)
# print(price>10 or price<30)
# print(not price>10)

#IF OPERATORS
# temperature = 25
# if(temperature>10):
#     print("Temperature is greater than 10")
# elif(temperature>20):
#     print("Temperature is greater than 20")


#WEIGHT CONVERTER EXERCISE

weight = int(input("Enter your weight: "))

unit = input("Enter your unit (K)g or (L)bs: ")

if unit.upper()=='K':
    print('Your weight in lbs' + str(float(weight*2.25)))
elif unit.upper()=='L':
    print('Your weight in kg' + str(float(weight*0.45)))
else:
    print('Invalid unit input')
