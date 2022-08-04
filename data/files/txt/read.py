def search(location):
  print("Searching...")
  with open(location) as file:
    for lines in file.readlines():
      print(f"Looked in {lines.strip()}")
  print("...Done!")

def run():
  search("data/files/txt/locations.txt")
run()