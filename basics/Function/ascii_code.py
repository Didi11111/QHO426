def ASCII():
  ch=input("Please enter a standard character:")
  if len(ch)==1:
    print(ord(ch))
  else:
    print("error")

def run():
  print("Program Started!")
  ASCII()

run()