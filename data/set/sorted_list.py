def observed():
  observations=[]
  for i in range(5):
    value=input("Please enter an observation:")
    observations.append(value)
  return observations

def remove_observations(list_of_observations):
  is_running=True
  while is_running:
    print("Do you wish to remove an observation? yes/no: ")
    user=input()
    if user == 'yes':
      remove=input("What observation do you wish to remove? ")
      list_of_observations.remove(remove)
      print("Done!")
    else:
      is_running=False


def run():
  print("Counting observations...")
  list=observed()
  remove_observations(list)
  list_set=set()
  #repopulating set....
  for i in remove_observations(list):
    item=(i, remove_observations(list).count(i))
    list_set.add(item)
  #printing calculation
  for item in list_set:
    print(f"{item[0]} observed {item[1]} times.")
run()
    