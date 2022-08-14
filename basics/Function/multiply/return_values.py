def sum_weights(weight_1, weight_2):
  total = weight_1 + weight_2
  return total

def calc_avg_weight(weight_1, weight_2):
  avg = sum_weights(weight_1, weight_2)/2
  return avg

def run():
  print("Enter the weight of first bot: ")
  weight_1=float(input())
  print("Enter the weight of first bot: ")
  weight_2=float(input())
  print("Choose one of the folowing calculation 'sum' or 'avg': ")
  user=input()
  if user == "sum":
    user = sum_weights(weight_1, weight_2)
    print(f"The total of Beep's and Bop's weight is {user:.2f}")
  elif user == "avg":
    user = calc_avg_weight(weight_1, weight_2)
    print(f"The average of Beep's and Bop's weight is {user:.2f}")
  else:
    print("I do not understend you, Try again!")

run()
  
    
  
  