#-----------------------------
#Password generator Code from Lab 1
#-----------------------------
'''
city = input("Which city did you grow up in?").strip().upper()
animal = input("What is your favorite animal?").strip().lower()
fav_num = int(input("What is your favorite number?"))
special_char = input("Choose a special character from these choices: !@#$%^&*").strip() #Can;t use "select" for some reason
user_password = city[:2] + animal[-2:] + str(fav_num*2) + len(city)*special_char #Use string concatenation
#print(f"{city[:2]}{animal[-2:]}{fav_num*2}{len(city)*special_char}")
print(f"Your generated password is: {user_password}")
'''

#is vs ==
list1 = [1,2,3]
list2 = [1,2,3]
list1 == list2 #True, checks "is the value of list1 and list2 the same?". Checks EQUALITY
list1 is list2 #False, is checks "are these the same object in memory?". Checks IDENTITY


#--------------- Password generator with validation with simple while loops ------------------
city = input("Which city did you grow up in?").strip().upper()
#If user did not write letters, ask user to re-input their hometown.

''' Following code will yield infinite while loops! 
while city != city.isalpha(): #won't work, city is a string, city.isalpha() is a boolean. Always give true, infinite loop!
    print("Invalid input, Try again!")
    city = input("Which city did you grow up in?").strip().upper()

while city is not city.isalpha(): #won't work, city is a string, city.isalpha() is a boolean. It will always give True
    print("Invalid input") #Infinite loop!

while city.isalpha() == False: #Technically correct way, but not "Pythonic code"
    print("Invalid input, Need to enter a valid city name!")
    city = input("Which city did you grow up in?").strip().upper()
'''
while not city.isalpha(): #Pythonic code, reads naturally, shorter and clearer
    print("Invalid input, Need to enter a valid city name!")
    city = input("Which city did you grow up in?").strip().upper()

#Do the same thing for animal
animal = input("What is your favorite animal? ").strip().lower()
while not animal.isalpha(): #Pythonic code, reads naturally, shorter and clearer
    print("Invalid input, Need to enter a valid animal name!")
    animal = input("What is your favorite animal? ").strip().lower()

fav_num = input("What is your favorite number? Enter a positive integer.").strip()
#while type(fav_num) != int #cannot do this because input always gives a string! You'll always get True, infinite loop
while not fav_num.isdigit(): #checks for positive integers (floats and negative numbers or strings with spaces will return False)
    print("Invalid input, Need to enter a valid positive integer number!")
    fav_num = input("What is your favorite number? Enter a positive integer.").strip()

fav_num = int(fav_num) #must be OUTSIDE while loop! Safe to convert fav_num string to integer now that we've validated it's a number

special_char = input("Choose a special character from these choices: !@#$%^&*").strip() #Can;t use "select" for some reason


user_password = city[:2] + animal[-2:] + str(fav_num*2) + len(city)*special_char #Use string concatenation




#_------------------------- Password generator with validation with no try/except-----------------------
allowed_chars = "!@#$%^&*"

# -------- CITY --------
city = input("Which city did you grow up in? ").strip()

while not city.isalpha():
    print("Invalid input. City must contain letters only.")
    city = input("Which city did you grow up in? ").strip()

city = city.upper()


# -------- ANIMAL --------
animal = input("What is your favorite animal? ").strip()

while not animal.isalpha():
    print("Invalid input. Animal must contain letters only.")
    animal = input("What is your favorite animal? ").strip()

animal = animal.lower()


# -------- FAVORITE NUMBER (INTEGER ONLY, NO try/except) --------
fav_input = input("What is your favorite number? ").strip()

while not (
    fav_input.isdigit() or
    (fav_input.startswith("-") and fav_input[1:].isdigit())
):
    print("Invalid input. Please enter a whole number (no decimals).")
    fav_input = input("What is your favorite number? ").strip()

fav_num = int(fav_input)


# -------- SPECIAL CHARACTER --------
special_char = input(
    "Choose ONE special character from these choices: !@#$%^&* "
).strip()

while len(special_char) != 1 or special_char not in allowed_chars:
    print("Invalid input. Please enter exactly ONE allowed special character.")
    special_char = input(
        "Choose ONE special character from these choices: !@#$%^&* "
    ).strip()


# -------- PASSWORD GENERATION --------
user_password = (
    city[:2] +
    animal[-2:] +
    str(fav_num * 2) +
    special_char * len(city)
)

print(f"\nYour generated password is: {user_password}")




'''
#--------------- Password generator with validation with try/except ------------------
allowed_chars = "!@#$%^&*"

# -------- CITY --------
city = input("Which city did you grow up in? ").strip()

while not city.isalpha():
    print("Invalid input. City must contain letters only.")
    city = input("Which city did you grow up in? ").strip()

city = city.upper()

# -------- ANIMAL --------
animal = input("What is your favorite animal? ").strip()

while not animal.isalpha():
    print("Invalid input. Animal must contain letters only.")
    animal = input("What is your favorite animal? ").strip()

animal = animal.lower()

# -------- FAVORITE NUMBER --------
valid_number = False
fav_num = None

while not valid_number:
    fav_input = input("What is your favorite number? ").strip()

    try:
        fav_num = int(fav_input)
        valid_number = True
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# -------- SPECIAL CHARACTER --------
special_char = input(
    "Choose ONE special character from these choices: !@#$%^&* "
).strip()

while len(special_char) != 1 or special_char not in allowed_chars:
    print("Invalid input. Please enter exactly ONE allowed special character.")
    special_char = input(
        "Choose ONE special character from these choices: !@#$%^&* "
    ).strip()

# -------- PASSWORD GENERATION --------
user_password = (
        city[:2] +
        animal[-2:] +
        str(fav_num * 2) +
        special_char * len(city)
)

print(f"\nYour generated password is: {user_password}")

'''