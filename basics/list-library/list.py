def interest():
  print("Enter your interest one after another and enter \"stop\" when done")
  s1=set()
  while True:
    interest= input()
    if interest.lower()=="stop":
      break
    else:
      s1.add(interest)
  return s1

def tinderDaSecond():
  print("First person:")
  p1 = interest()
  print("Second person:")
  p2 =interest()
  common = p1.interesction(p2)
  if len(common)>= 3:
    print("Oh yehe")
  else:
    print("Oh no")
      
tinderDaSecond()
    
    