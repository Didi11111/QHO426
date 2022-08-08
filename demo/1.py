#reading a txt file
with open("song.txt") as song:
  s = song.read()
  s1=s.lower().replace(",","").split()
  print(s1)
  #print uniq words (set) separated by ~
  print("~"*30)
  print(set(s1))
  print("~"*30)
  #counting words in dictionary
  dictio = {}
  for token in s1:
    dictio[token] = dictio.get(token, 0) + 1 # check if dictionary contains key(token) if does will be increased by 1 for every key if no will be created akey with a value 1. get() - access the dictionary
print(dictio) #print dictionary
print("~"*30)
print(f"To write a viral song, you need {len(set(s1))} uniq words")
    