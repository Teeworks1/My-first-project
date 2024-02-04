#name = input ("what is your name? ")
#color= input ("what is your favorite Color? ")
#print ("what is your name? ")
#print ( name +  " likes "  + color)

weight_in_pounds =input("what is your weight in pounds?" )
weight_in_kg = int(weight_in_pounds) * 0.05
print(weight_in_kg)

first = "John"
last =  "Smith"
msg = f'{first} + [{last}] is a coder'
print(msg)

course = "Python for Beginners"
if len(course)<5:
 print("pls enter an 8 letter course title")
elif len(course)>20:
 print("Too Many words, Pls look at the guidelines")
else:
 print("good to go")
print("Welcome to Python Course")

weight =input("weight:"   )
unit= input("Lb(s) or Kg(s): ")
if unit == "L":
  converted = int(weight) * 0.45
  print(f" you are {converted} lbs")
else:
  print(f"you are {int(weight)/ 0.05} Kgs")

secret_number = 9  
guess_count = 0
guess_limit = 3
while guess_count< guess_limit:
  guess= int(input("Guess: "))
  guess_count +=1
  if guess == secret_number:
    print("You Won!")
    break
else:
  print('sorry you failed!')

#name =input(">: ")
#start == "start game"
#while name!= quit:
 #if name == help:
  #print ('''start- to start the game)
     #stop - to stop the game
     #quit - exit game''')  
 #elif  name == start:
   #print ("car started")
 #elif  name == stop:
   #print ("car stopped")  
#else:
   #print("quit game")
 
#matrix = [
          #1 ,2, 3,
          #4 ,5, 6,
          #7, 8, 9
#]

#print (matrix[0, 2])

numbers =[2,3,4,5,6,7,8]
numbers2 =numbers.copy()
numbers.append(20)
print(numbers)

numbers =[1,2,4,5,6,7,8,1]
uniques =[]
for item in numbers:
  if item not in uniques:
   uniques.append(item)
print(uniques)

customer ={
  "name" : "Ochuko",
  "email": "ochuko.ebireri@wealtsimple.com",
  "has_good_credit": "yes" 
}
print(customer["name"])

name =input("phone: " )
phone_number = {
  "1": "one",
  "2": "two",
  "3": "three",
  "4": "four"
}
output =""
for ch in name:
  output += phone_number.get(ch, "!") + " "
print(output)

def greet_user(first_name, last_name):
  print(f"welcome {first_name} {last_name}")
  print("nice to meet you")

print("Hey !")
greet_user("Chuks","Tellen")
print("enjoy your time here")

def square(numbers):
  return(numbers*numbers)
print(square(2))


class Point:
  def __init__(self, x ,y):
    self.x =x
    self.y =y
  def move(self):
    print("move")
  def draw(self):
    print("draw")

point1 =Point(10,20)
point1.draw()
print(point1.x)



import converters

print(converters.lbs_to_kgs(70))

import  utils

from utils import find_max

numbers= [1,2,3,4,5,6,7,8,100]
max = find_max(numbers)
print(max)

