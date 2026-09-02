"""
print("Temp Check")

temp = int(input("Please put the temp today: "))

if temp < 15 or temp > 35:
    print("Wear a jacket")
else:
    print("Nice weather")
"""
"""
print("-------log in access------")

is_admin = True
is_banned = True

if is_admin == True and is_banned == False:
    print("Log in access")
else:
    print("log in denied")
"""
"""
print("----Weekend or holiday----")

day = input("Please indicate the day today: ")
is_holiday = False

if day == "Saturday" and is_holiday == True:
    print("No work today,very shappy")
elif day == "Saturday" or day == "Sunday" or day == "Holiday":
    print("no work today, happy")
else:
    print("We have work today!")
"""
"""

print("-----Valid age for ride----") #both conditions must met (and)

age = int(input("Please put in your age:"))
height = int(input("Please put in your height: "))

if age >= 10 and height > 140:
    print("you can ride")
else:
    print("You are not allowed kid!")

"""
""" -------------------------------------------------------------------
this means if password length is graeter than 8 and if any chararacter
in password is a didgit for means check evry digit in those password


print("-----Password strength-----")

Password = input("Please enter password: ")

while Password.lower() != "q": 
    if len(Password) > 8 and any(char.isdigit() for char in Password):
        print("Password is valid")
    else :
        print("Password is not valid")

    Password = input("Please enter password: ")
print("Thank you")
"""

"""
print("----- Traffic Light -----")

Traffic_light = input("Please put in the light: ")



if Traffic_light.lower() == "green" and not Traffic_light == "red":
    print("Go!!!!!")
else:
    print("Stoppppp!!!!!")

"""
"""   
print("----- Range check -----")

number = 200

if number >= 1 and not number <= 100 :
    print("out of range")
else:
    print("in range")

"""   
""" 

print("-----Weekend or holiday-----")

today = input("Please input the day today: ")
is_holiday = False
while today.lower() != "q": 
    if today.lower() == "saturday" or today.lower() == "sunday" or today.lower() == "holiday" and is_holiday == False:
        print("No work today")
    else:
        print("We have work today")
    today = input("Please input the day today: ")
print("thank you!")

 """ 


""" 
print("-----Valid age for ride-----")

age = int(input("Please put in your age: "))
height = int(input("Please put in your height: "))
if age >= 10 and not height <= 140 :
    print("You can get in!!!")
else:
    print("You can not get in")

 """ 

""" 
print("-----Password Strength-----")

Passrword = "abc123"

if len(Password) >= 8 and any(char.isdigit() for char in Password):
    print("password is VALID!!!!!!")
else:
    print("password is NOT VALID!!!!!")

""" 

""" 
print("-----Even and positive-----")

num = 8

if num % 8 == 0 and num > 0:
    print("Valid")
else:
    print("Not Valid")
 

""" 
""" 
print("-----XOR Style-----")

ticket = input("Please put (Y) if you have a ticket: ")
is_ticket_vip = input("Input (1) if your tciket is VIP (2) If not : ")

if ticket.lower() == "y" and not is_ticket_vip == "1" or ticket.lower() == "n" and not is_ticket_vip == "2":
    print("You can entry")
else:
    pint("you CANNOT enter")
""" 
#TODO:VALIDATE USER INPUT
# 1. username is no more that 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits
""" 
print("validate user input user")

name = input("Please put in your username: ")

if len(name) > 12:
    print("Name should not exceed 12 characters")
elif not name.find(" ") == -1:
    print("Name shuld not have sapce")
elif not name.isalpha():
    print("name should not have digits")
else:
    print("Name is valid")
""" 

""" 
time = 10

for x in range(1,11):
    print (x)

""" 
""" 
number = 21
for number in range(1,21):
    if number %  2 == 0:
        print(f"{number} even ") 
    else:
        print(f"{number} odd ")

""" 
user_number = int(input("Please input number: "))

for number in range(1,user_number):
    result = user_number * number
    