print("What phrase do you see? ")
user_word = input()
reversed=""
print("Identifying...")
for letter in user_word:
  reversed=letter+reversed
print(f"{reversed}", end="")