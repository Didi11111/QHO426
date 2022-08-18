import matplotlib.pyplot as plt

def coffee_sleep(n):
  coffee = []
  sleep = []
  for i in range (n):
    coffee.append(int(input("Enter the coffee amount you drink per week: ")))
    sleep.append(int(input("Enter avarage sleep per night: ")))
  return coffee, sleep

print(coffee_sleep(6))

def movies():
  movie = {}
  for i in range(n):
    m_genre = input("Enter your favorite genre: ")
    movie[m_genre]= movie.get(m_genre, 0) + 1
  return movie  
    

def music(n=5):
  songs = {}
  for i in range(n):
    m_genre = input("Enter your favorite genre: ")
    songs[m_genre]= songs.get(m_genre, 0) + 1
  return songs
  
def mm_vs_dd(n=5):
  mm=0
  dd=0
  for i in range(n):
    ans=input("Who wins? MM or DD? ")
    if ans.lower()=="mm":
      mm+=1
    elif ans.lower()=="dd":
      dd+=1
  return [mm, dd]

def run():
  fig=plt.figure()
  ax1=fig.add_subplot(2,2,1)
  ax2=fig.add_subplot(2,2,2)
  ax3=fig.add_subplot(2,2,3)
  ax4=fig.add_subplot(2,2,4)
  
  n=input("Enter nr of students: ")
  c_s = coffee_sleep(n)
  ms=movies(n)
  ss=music(n)
  ax1.plot(c_s[0], c_s[1], "rx")
  ax1.set_xlabel("Coffee intake (cups per day)")
  ax1.set_ylabel("Coffee intake (cups per day)")
  ax1.set_title("Coffee vs Sleep")
  

  ax2.pie(ms.values(), labels=ms.keys(), autopct="%.f%%")
  ax2.set_title("Movie preferences")
  
  ax3.pie(ss.values(), labels=ss.keys(), autopct="%1f%%")
  ax3.set_title("Music preferences")

  ax4.bar(["Micky Mouse", "Donald Duck"], mm_vs_dd(n))
  ax4.set_xlable("Characters")
  ax4.set_ylable("Frequency")
  ax4.set_title("Big battle of the 2 Disney characters")
  plt.show()

run()
  