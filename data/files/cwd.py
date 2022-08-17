import os
# to find out the current diretory
def cwd():
  path = os.getcwd()
  print(f"Current Working Directory: {path}")
  #to print al files from current directory
  print(f"The directory contains the following: ")
  for file in os.listdir(path):
    print(file)

def run():
  print("Processing...")
  cwd()
run()