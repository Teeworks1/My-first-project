import random
for i in range(3):
  print(random.randint(10,20))

Members =["john","Reynold", "Endurance", "Makinde"]
leader =random.choice(Members)
print(leader)

from pathlib import Path

#path =Path("email")
#print(path.mkdir())

path =Path()
#path= path.glob("*.tf")
   #print(file)
print(path.glob("*.tf"))

height = 250.6
height *=2.5
number =(f"your height is: {height}cm")
print(number)

name = "Ochuko"
print(name.capitalize())

name = "ochuko"
print(name.upper())

print(name.replace("o", "u"))

age = int(input("how old are you ?: " ))
if age < 18:
 print("small boy")
elif age == 18:
 print("congrats") 
else:
 print("you don old")

 import time
 for seconds in range(10,0,-1):
   print (seconds)
   time.sleep(1)
print("Happy New Year!")

food = ['rice', "beans", "garri", "yam", "corn"]
print(food[0:2])

pasta =["sphagetti", "noodles", "macroni"]
fruits=["water_melon", "nut", "orange"]
desert=["ice-cream", "cake"]

food =[pasta, fruits, desert]

print(food[1][2])

pasta =("sphagetti", "noodles", "macroni")
print(pasta.index("sphagetti"))