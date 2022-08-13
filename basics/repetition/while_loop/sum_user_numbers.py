print("How many numbers should I sum up? ")
user=int(input())
total=0

while user > 0:
  num=int(input(f"Please enter number {user}: "))
  user-=1
  total=total+num
print("The answer is ", total)