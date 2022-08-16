def directions():
  directions=["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
  return directions
 
def menu():
  print("Please select a direction: ")
  menu = directions()
  for index in range(len(menu)):
    print(f"{index}: {menu[index]}")
  index=int(input())
  return menu[index]
  
def run():
  route=[]
  print("Working out escape route...")
  for i in range(5):
    route.append(menu())
  print(f"Escape route: {route}")
  
run() 
