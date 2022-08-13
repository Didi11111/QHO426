print("How many bars should be charged?")
an=int(input())
charges=0
while an > charges:
  charges+=1
  print("Charging:", "█" * charges)
print("The battery is fully charged.")
