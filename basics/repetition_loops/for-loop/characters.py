print("What strange markings do you see? ")
user_word = input()
print("Identifying...")
for position in range(0, len(user_word), 1):
  print(f"index{position}:{user_word[position]}")