name = input("What is your name? ")
age = int(input("What is your age? "))

if age <= (int(18)):
    print("You are a child")
else:
    print("You're an adult!")

print("So you are", name, "And you are", age, "years old")

q = input("Is this corrent? (Cap sensitive) |Y| / |N|")

if q == ("Y"):
    print("So that is correct!")#
elif q == ("N"):
    print("So that is not correct")
else:
    print("You have selected a key that ain't suggested! Try again")

print("This is the end of the git test... i told you there is nothing here lmao")
