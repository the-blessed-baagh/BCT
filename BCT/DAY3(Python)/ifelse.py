#write a python program if eligible for casting vote or not
age=int(input("enter your age"))
if age>=18:
    print("you are eligible to vote")
elif age<18:
    print("you are not eligible to vote")
else:
    print("enter a valid age")