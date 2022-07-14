def char():
  print("Please enter an ASCII code:")
  x=abs(int(input()))
  if x in range(32, 127):
    print(f"The character represented by the ASCII code {x} is {chr(x)}")
        

def run():
  print("Program Started!")
  char()

run()