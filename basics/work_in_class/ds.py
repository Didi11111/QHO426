def shop():
  items = {"ipod": 500, "mouse": 9.99, "potatoes": 1.99, "gold": 99989.99, "bread":99.65}
  return items

def view_all(products = {}):
  for i, j in products.items():
    print(f"{i}______________£{j:.2f}")

def basket():
  b= []
  while True:
    item = input("Enter the item or \"stop\" to stop:")
    if item.upper()=="STOP":
      break
    q=int(input(f"Enter the quantity of {item}: "))
    for i in range(q):
      b.append(item.lower())
    return b
#print(basket())
    
  
def till(basket=[]):
  all_items = shop()
  total = 0.0
  for product in basket:
    if product in all_items:
      total+=all_items[product]
    else:
      print("Sorry mate, go to Lidl")
      
  return total

print(till(basket()))