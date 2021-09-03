age = int(input("Enter your age: "))

if age > 17:
    print("You are eligible to vote")

#elif age > 15 and age < 18:
elif age == 16 or age == 17:
    print("You are almost eligible to vote")

else:
    print("You are not eligible to vote")