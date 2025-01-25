################ Printing Outputs #############

# print("Hello World" + " " + "Cloud Security")

# print("Hello World","Cloud Security")

######### Variables #################

# name = "obama"
# age = 60
# body_temp = 85.5
# democratoc = True

# children_ages = [15, 18]

# child_bio = {
#     "Name":" Sasha",
#     "Age": 15
# }

# print("My Name is ", name, "and I am ", age, "Years Old", "And My body Temperature is", body_temp)

# print(type(name))
# print(type(age))
# print(type(body_temp))
# print(type(democratoc))
# print(type(children_ages))
# print(type(child_bio))


################################## Mathematical Calculations ######################

# numbers_add = 5 + 5
# numbers_sub = 20 - 10
# print(numbers_add, numbers_sub)

# year_of_birth = 1991

# current_year = 2025

# age = current_year - year_of_birth

# print(age)


####################### Input from The User #####################

# year_of_birth = int(input("Please Enter Your Year of Birth: "))

# current_year = int(input("Please Enter The Current Year: "))

# age = current_year - year_of_birth

# #print(type(year_of_birth))
# print(age)


################# Conditionals ###################

# year_of_birth = int(input("Please Enter Your Year of Birth: "))

# current_year = int(input("Please Enter The Current Year: "))

# age = current_year - year_of_birth


# if age > 80:

#     print("You are too Old to be a US President")

# elif age <= 40:

#     print("You are too Young to be a US President")
# else:
#     print("You are Elligible to be a US President")

# Write a program that takes a number from a user 
# If the numnber is divisible by 3 print Foo
#If the number is divisible by 5 print Bar
#If the number is divisible by both three and 5 print foo bar

# num = int(input("Please Enter Any Number: "))

# if num % 3 == 0 and num % 5 == 0:
#     print("Foo Bar")
# elif num % 5 == 0:
#     print("Bar")
# elif num % 3 == 0:
#     print("Foo")
# else:
#     print("The", num, " you entered is Neither Divisible by 3 or 5, please try Again")

######################## Loops ###########################

num = [1,2,3,4,5,6,7,8,9,10]

# names = {
#     "first_name": "obama",
#     "Age" : 60
# }

# print(names["first_name"])
# print(names["Age"])

############################################# 

# num.append(11)

# #print(num)

# num.append(12)

# num.sort()
# print(num)

# numbers = range(1,100)

# multiples_three_five = []

# for num in numbers:
#     if num % 3 != 0 and num % 5 != 0:
#         multiples_three_five.append(num)

# print(multiples_three_five)

names = [
    {
    "first_name": "barack",
    "last_name": "obama",
    "age": 60
},
{
    "first_name": "joe",
    "last_name": "biden",
    "age": 82
}
]

# names = {
#     "first_name": "barack",
#     "last_name": "obama",
#     "age": 60
# }

#print(names[1]["first_name"])

# for key, value in names.items():
#     print(key, str(value))

# for item in names:
#      for key, value in item.items():
#         print(key, str(value))


################# Temperature Conversion #####################

# Write a program that takes a temperature in Celsius from a user and converts it to Fahrenheit

#F = (°C x 9/5) + 32. 

# temp_c = float(input("Please Enter Temperature in Celcius: "))

# temp_f = ((temp_c * 9/5) + 32)

# print("The Temperature Value of", temp_c, "is equivalent to", temp_f , "in Fahrenheit")  


################# Functions ########################

def celcius_to_fahrenheit(temp_c):
    temp_f = ((temp_c * 9/5) + 32)
    return temp_f

clovis = float(input("Please Enter Temperature in Celcius: "))

temp_value = celcius_to_fahrenheit(clovis)


############## Tell is if the weather is too bad #############

if temp_value <= 40:
    print("The Temperature today is", temp_value, "So the Weather is too bad today so School is Cancelled")
else:
    print("The Temperature today is", temp_value,"so the Weaher is Ok to go out")