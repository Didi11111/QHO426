print("What is your name human? ")
name=input()
print("How old are you?")
age=int(input())
print("How tall are you?")
height=float(input())
print("How much do you weight?")
weight=float(input())
BMI=weight/(height**2)
print(name, "You are", age, "years old and your BMI is:", BMI)
print(f"{name} You are {age} years old and your BMI is: {BMI:.2f}")