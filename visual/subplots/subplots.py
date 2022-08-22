import csv
def read_data():
  data={"survived": [], "sex": [], "fare": [], "age": []}
  with open("visual/subplots/titanic.csv") as f:
   csv_reader = csv.reader(f)
   next(csv_reader) # overlook 0 row
  for row in csv_reader:
    survived =row[1].strip()
    sex=row[14].strip()
    age=row[4].strip()
    fare=row[8].strip()
    if (survived !=" and sex!=" and age!="" and fare!=""):
      data["survived"].append(int(survived))
      data["age"].append(int(round(float(age))))
      if sex =="0":
        data["sex"].append("male")
      elif sex =="1":
        data["sex"].append("female") 
      data["fare"].append(round(float(fare), 2))
 #for row in csv_reader:
   #if row[1]!="" and row[4]!="" and row[8]!="" and row[14]!="" and row[4]!=" " and row[14] is not None and row[8]!=" " :
     #data["survived"].append(row[1].strip())
     #if int(row[14].strip()) == 0:
       #data["sex"].append("male")
     #elif int(row[14].strip()) == 1:
       #data["sex"].append("female")
     #data["fare"].append(int(round(float(row[8].strip()), 2)))
     #data["age"].append(int(round(float(row[4].strip()))))

  read_data()
print(read_data())
        
      
