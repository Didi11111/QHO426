#creating a new file from old file and sort the data
def search(file_path):
  print("Searching...", end="")
  sections = []
  books = []
  #open the specified file(file-path) for reading
  with open(file_path) as file:
    #for each line in file
    for line in file:
      # get data from old file (from line start with section) and add to new file into section[]
      if line.startswith("Section"):
        section_name = line.split(":")[1]
        sections.append(section_name.strip())
      # get data from old file (from line start with somthing else) and add to new file into books[]
      else:
        books.append(line.strip())
  print("Done!")
  return (sections, books)
# saving new file
def save(file_path, data):
  print("Saving...", end="")
  with open(file_path, "w") as file:
    file.write(f"Sections: {data[0]}\n")
    file.write(f"Books: {data[1]}\n")
  print("Done!")


def run():
  data = search("data/files/txt/books.txt")
  save("data/files/txt/section-books.txt", data)

run()

  