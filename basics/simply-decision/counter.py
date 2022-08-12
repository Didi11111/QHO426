first=int(input("Please enter first number: "))
second=int(input("Please enter second number: "))
third=int(input("Please enter third number: "))

count_even=0
count_odd=0
if first % 2 == 0:
  count_even+=1
else:
  count_odd+=1
if second % 2 == 0:
  count_even+=1
else:
  count_odd+=1
if third % 2 == 0:
  count_even+=1
else:
  count_odd+=1
print(f"There were {count_even} even and {count_odd} odd numbers.")