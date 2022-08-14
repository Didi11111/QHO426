def display_in_box(word):
    num_dashes = 4 + len(word)
    print("-" * num_dashes)
    print("| {} |".format(word))
    print("-" * num_dashes)
  
def display_lower_case(word):
  print(word.lower())
  
def display_upper_case(word):
  print(word.upper())

def display_mirrored(word):
  print(word[::-1])
# other type of reversing string
  #mirrored = ""
  #for letter in reversed(word):
    #mirrored += letter
  #print("{} | {}".format(word, mirrored)) 

def repeat(word):
  print("How many times to display the word: ")
  times=int(input())
  for i in range(times):
    # even repetition
    if i % 2 == 0:
      print(display_lower_case(word))
    # odd repetition
    else:
      print(display_upper_case(word))

def run():
  print("Enter a word: ")
  word=input()
  print("Chose the number from the menu: \n 1 - Display the word in a box \n 2 - Display the word in lower case \n 3 - display the word mirrored \n 4 - Display the word in upper case \n 5 - Repeat the word")
  user=int(input())
  if user == 1:
    display_in_box(word)
  elif user == 2:
    display_lower_case(word)
  elif user == 3:
    display_upper_case(word)
  elif user == 4:
    display_mirrored(word)
  elif user == 5:
    repeat(word)
  else:
    print("You must chose a number fro 1 to 5. Try again!")  

run()