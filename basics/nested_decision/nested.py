an1=input("What type of cover does the book have? enter hard or soft ")

if an1 == 'soft':
  an2=input("Is the book perfect-bound? enter yes or no")
  if an2 == 'yes':
    print("Perfect bound books are very popular!")
  else:
    print("Soft covers with coils or stitches are great for short books")
else:
  print("Books with hard covers can be more expensive!")