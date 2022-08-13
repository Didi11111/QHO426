print("What phrase do you see? ")
user_word = input()
print("Identifying...", end="")
for i in range(len(user_word)-1, -1, -1):
  print(f"{user_word[i]}", end="")