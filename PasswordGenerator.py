import random 
# A built-in module in Python that has methods 
# I can use to make random passwords.

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "!@#$%^&*()-=_+;':[],./<>?"
# These string values set to these variables are allowed 
# characters to use in a random generated password.

upper, lower, nums, syms = True, True, True, True
# I want to create a system that will allow what type of
# characters can be added to the random generated password.
# For example, if I want uppercase letters in my password,
# I assign the boolean variable, upper, a value of True.
# If I don't want symbols in my password, I can assign another
# boolean variable, syms, the value of False.

allowed = ""

if upper:
    allowed += uppercase_letters
if lower:
    allowed += lowercase_letters 
if nums:
    allowed += digits
if syms:
    allowed += symbols
# The all variable will hold all characters that are actually allowed.
# The if statements below mean that if a type of character is True, the 
# all will hold all characters of that type. 

length = 12 # the length variable is the number of characters in the password
amount = 1 # the amount variable is the number of passwords to generate

for x in range(amount):
    password = "".join(random.sample(allowed, length))
    print(password)
# The sample method takes in 2 parameters. The first parameter is the sequence of characters
# to take characters from and the 2nd parameter is the size of the returned sequence. 
# The returned sequence will be joined with the empty string in the password variable.
# The "" means there is nothing separating the characters in between. 