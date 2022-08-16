def observed():
  observations=[]
  for i in range(7):
    value=input("Please enter an observation:")
    observations.append(value)
  return observations

def run():
  print("Counting observations...")
  list=observed()
  list_set=set()
  #repopulating set....
  for i in list:
    item=(i, list.count(i))
    list_set.add(item)
  #printing calculation
  for item in list_set:
    print(f"{item[0]} observed {item[1]} times.")
run()
    
    
  
  