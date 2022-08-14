print("Program Started!")
print("Please enter a word: ")
word=input()
list=(list(word))
for letter in list:
  print(f"The ASCII code for {letter} is {ord(letter)}")