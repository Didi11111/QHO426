print("Please enter a number:" )
num=int(input())
total=1
count=0
while count < num:
  count+=1
  total=total*count
  
print("The factorial is ", total)