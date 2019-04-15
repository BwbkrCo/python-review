# Assignment 1
# 1 : Create two variables - one with your name and one with your age
name = 'Brian'
age = 30

user_name = input("Enter your name: ")
user_age = input("Enter your age: ")

# 2 : Create function which prings your data as one string
def greeting(name, age):
    print("Hello " + name + ", I'm " + str(age))

greeting(name, age)

def print_user_data():
    print(user_name + " - " + user_age)

print_user_data()

# 3 : Create a function which prints ANY data (two arguments) as one string
def greet(name, age):
    print(name + str(age))

greet('brian', 24)    

def print_concatenated_data(el1,el2):
    print(el1 + " - " + el2)

print_concatenated_data(user_name,user_age)

# 4 : Create a function which caluclates and returns the number of decades you already lived 
# (e.g. 23 =2 decades)
age = int(input("Enter your age: "))
def decade_calc(age):
    if age >= 50:
        print("You've lived for 5 decades")
    elif age >= 40:
        print("You've lived for 4 decades")
    elif age >= 30:
        print("You've lived for 3 decades")
    elif age >= 20:
        print("You've lived for 2 decades")
    elif age >= 10:
        print("You've lived for 1 decade")

decade_calc(age)

def calculate_decades(age):
    decades_lived = age // 10
    return decades_lived

decades = calculate_decades(int(user_age))
print(decades)