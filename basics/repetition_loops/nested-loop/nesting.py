print("Enter a sequence of characters consisting of dashes and two markers: ")
a=input()
print("Enter a character representing the marker: ")
b=input()
mark1_pos = -1
mark2_pos = -1
for position in range(len(a)):
   letter= a[position]
   if letter == b:
     if (mark1_pos == -1):
       mark1_pos = position
     else:
       mark2_pos = position
print(f"The distance between the markers is {mark2_pos - mark1_pos - 1}.")
    
  