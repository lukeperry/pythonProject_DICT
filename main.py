
# Activity 1
print("Hello World, what are you doing?")

# Activity 2
x = 7
y = "cake"

print(x)
print(y)

# Activity 3
favorite_food = "pizza"
friend_name = "Tina"
favorite_drink = "soda"

print("I like " + favorite_food + ".")
print("I like eating " + favorite_food + " with my friend " + friend_name + ".")
print("We like to drink " + favorite_drink + ", too.")

# Activity 4
character_job = "pirate"
character_ride = "ship"
character_souvenir = "gold"
character_pet = "parrot"

print("There was once a " + character_job + " who loved adventure.")
print("The " + character_job + " would take her " + character_ride + " to unknown places.")
print("She brings home a lot of " + character_souvenir + ".")
print("Then she goes home to her pet " + character_pet + ", Chuckles")

# Activity 5
print("Roses are red, violets are blue.")

if 10 > 7:
    print("Ten is greater than seven!")
if 16 < 42:
    print("Sixteen is less than forty-two!")
    print("A long time ago in a galaxy far, far away...")

# Activity 6
x = 7
y = ("cake")
print(x)

# Activity 7: Function
def hello_function():

    print("Hello!")
hello_function()

hello_function()

def hello_function(name, lastname):
    print("Hello " + name +" "+ lastname + "!")
hello_function("Rose", "Gonzales")


def niceDay(name):
    print("Have a nice day " + name + "!")
niceDay("Luke")

# Activity 8: Input Function

name = input("Enter your name: ")
print("Hi, " + name + "!")

num1 = int(input("Please enter 1st number: "))
num2 = int(input("Please enter 2nd number: "))

print("Your two numbers are:", num1, " and ", num2)

def addNum(num1, num2):
    total = num1 + num2
    return (total)

num1 = int(input("Please enter 1st number: "))
num2 = int(input("Please enter 2nd number: "))

print("Total: ", addNum(num1, num2))


#def slam_book():
name = input("Please enter your name: ")
age = input("Please enter your age: ")
fav_color = input("Please enter your favorite color: ")
fav_movie = input("Please enter your favorite movie: ")
mobile_num = input("Please enter your mobile number: ")
motto = input("Please enter your motto: ")

 #   return name, age, fav_color, fav_movie, mobile_num, motto

#slamBook(name,age,fav_color,fav_movie,mobile_num,motto)
print("Hi! ", name, ", you are ", age, " years old, your favorite color is ", fav_color, "your favorite movie is, ", fav_movie," your mobile number is ", mobile_num, "your motto is ", motto)
#update