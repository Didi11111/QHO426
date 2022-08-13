print("How many live cables must I avoid?")
an=int(input())
lives=0
while an > lives:
  print("Avoiding...", end="")
  lives+=1
  print(f"...Done! {lives} live cable avoided!")
print("All live cables have been avoided.")