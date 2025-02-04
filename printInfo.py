#Take user infomation as input and output that infomation for validation

#input()
name = input("What is your name: ")
email = input("Enter your email address: ")
age = input("How old are you: ")
print("\n")

#validate inputed infomation
print("Is the following infomation correct ?\n")
print("Name:",name)
print("Email Address:",email)
print("Age:",age)
print("")

#user validation
response = input("Yes/No ? = ")
if response.lower() == "yes":
    print("All is in order, GoodBye")
else:
     print("Please restart the terminal and start again!")