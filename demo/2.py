import csv
import matplotlib.pyplot as plt

def gather_data(n=1): #num of people I ask
  with open("june_data.csv", "w") as file: #creating a file  "w" - write, "r" - read, "a" - add at the end info
    csv_writer = csv.writer(file) #it will rewrite info after all running
    for i in range (n):
      h = float(input("Enter your height: "))
      w = float(input("Enter your weight: "))
      csv_writer.writerow([h, w])

# gather_data(3) - nr of times asked from pleople
def retrieve_data(): #reading data from file into separated lists
  with open("june_data.csv") as file:
    hs=[]
    ws=[]
    csv_reader=csv.reader(file) # read info from file
    for row in csv_reader:
      hs.append(float(row[0]))
      ws.append(float(row[1]))
  return hs, ws

def graphs(): #to creat graph
  x, y = retrieve_data()
  plt.plot(x, y, "ro-") 
  plt.show() # to display a graph

gather_data(3) # call function
  
