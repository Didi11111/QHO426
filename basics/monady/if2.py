h=input("Are you happy? y or n\n")
k=input("Do you know it? y or n\n")
if h.upper()=="Y" and k.upper()=="Y":
  print("Clap your hands")
elif h.upper()=="N" and k.upper()=="N":
  print("Boo-Hoo")
elif h.upper()=="N":
  print("Cheer up boss!!!!!")
else:
  print("This is not achievable")