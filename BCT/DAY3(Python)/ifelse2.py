#wapp for checking the input is kid,child,teen or adult kid:0-5 child:6-11 teen:12-19 rest adult
age=int(input("enter your age"))
if age>=0 and  age<=5:
    print("it is a kid")
elif age>=6 and age<=11:
    print("it is a child")
elif age>=12 and age<=19:
    print("it is a teenager")
elif age>19:
    print("it is an adult")
else:
    print("enter a valid age")