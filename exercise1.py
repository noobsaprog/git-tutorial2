"""
("-----------------grocery store----------------")

print("Hi welcome to our grocery")
cart1 = "₱500 : Lettuce | cucumber | carrots | ampalaya"
cart2 = "₱1000 : Basil | paprika | paminta | spicy powder"
cart3 = "₱2000 : meat | tofu | ground beef | seafood"

cart1_price = 500
cart2_price = 1000
cart3_price = 2000

print(f"cart 1 : {cart1}")
print(f"cart 2 : {cart2}")
print(f"cart 3 : {cart3}")

user_cart = input("Please put in the cart you chose:")
while user_cart != "q":
    if user_cart == "1":
        print(f"you choose: {cart1}")
        chosen_price = cart1_price
    elif user_cart == "2":
        print(f"you choose: {cart2}")
    elif user_cart == "3":
        chosen_price = cart2_price
        print(f"you choose: {cart3}")
        chosen_price = cart3_price
    else:
        print("invalid choice")
        user_cart = input("Please put in the cart you chose (or 'q' to quit):")

    try:
        bayad_ngcus = float(input(f"You selected {user_cart}, please pay the amount of the selected grocery: "))
        if bayad_ngcus >= chosen_price:
            user_pay = bayad_ngcus - chosen_price
            print(f"you pay {bayad_ngcus}, here is your change {user_pay}")
        else:
            print("Amount is insufficient, please add more")

    except ValueError:
        print("Please enter a valid number")

    buy_again = input("Do you want to buy again? (yes/no): ")
    if buy_again.lower() == "no":
        user_cart = "q"
    else:
        user_cart = input("Please put in the cart you chose:")

print("thank you for shopping with us")
"""


"""
brands = {
    "toyota": True,
    "mitsubishi": True,
    "honda": True,
    "yamaha": True,
    "suzuki": False
}

print(" Toyota \n Mitsubishi \n Honda \n Yamaha \n Suzuki")

customer = input("Please enter a brand of your choice: ").lower()
while customer != "q":
    if brands.get(customer):
        print("This is available")
    else:
        print("This is not available")
    customer = input("Please enter a brand of your choice: ").lower()
print("Thank you, come again")

"""

"""
print("calculator")

operator = input("Please choose your operation (+,x,/,-) : ")

first_num = float(input("Type 1st number:"))
sec_num = float(input("Type 2nd number:"))

if operator not in ["+","x","/","-"]:
    print("number or operator is invalid")
while operator.lower() != "q":
    if operator == "+":
        sum = first_num + sec_num
    elif operator == "x":
        sum = first_num * sec_num
    elif operator == "/":
        sum = first_num / sec_num
    elif operator == "-":
        sum = first_num - sec_num


    print(f"1st and 2nd num sum: {sum}")

    operator = input("Please choose your operation (+,x,/,-) : ")

print("calculate again")
    
"""






#validate user input exercise
# 1. username is no more that 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

name = input("Please put in your name: ")

if len(name) > 12:
    print("Name should not exceed more that 12 characters")
elif not name.find(" ") == -1: #this means if the result is not -1, meaning the code find space
    print("Name should not contain spaces")
elif not name.isalpha(): # this 
    print("Name should not contain numbers")
else:
    print(f"Hello {name}") 

   1:38 hour

# logical operator (or) = at least one condition must be true

temp = 25
is_raining = False

if temp > 35 or temp < 0 or is_raining:    # or logical operator needs one condition to be true
    print("the outdoor event is cancelled")
else:
    print("the outdoor event is still scheduled")
#------------------------------------------------------------------
#logical opeator (and) =  both conditions must be true

temp = 40
is_raining = True

if temp > 35 and is_sunny:                  # this means if both temp and is_sunny is true  print("the outdoor event is cancelled")   
    print("the outdoor event is cancelled")
else:
    print("the outdoor event is still scheduled")

#------------------------------------------------------------------

#logical opeator (not) =  both conditions must be true

name = input("Please put in your name: ")

if len(name) > 12:
    print("Name should not exceed more that 12 characters")
elif not name.find(" ") == -1: #this means if the result is not -1, meaning the code find space
    print("Name should not contain spaces")

#------------------------------------------------------------------