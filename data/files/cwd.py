import os

def cwd():
  path = os.getcwd()
  print(f"Current Working Directory: {path}")
  for file in os.listdir(path):
    print(file)
def run():
  print("Procesing.....")
  cwd()
run()