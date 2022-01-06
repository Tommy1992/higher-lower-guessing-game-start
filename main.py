"""
ToDo list:
1 - CHECK import random, art, game_data   
2 - CHECK printing logo1, logo2 VS, in between print Compare A: {var} and then Against B: {var2}, then "Who more follows, type..." 
3 - function to access and compare data(imported already), setting var2 to var1 after a right answer - then wait for input of answer again
3.1 - compare fct: Add utility, that not the same company/celeb is chosen to compare (or is there no chance with random.choice)
4 - global variables needed !?(i.e. score)
"""

from art import logo, vs
from game_data import data
import random as rnd
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

score = 0

a = rnd.choice(data)
aname = a["name"]
afoll = a["follower_count"]
adesc = a["description"]
acountry = a["country"]
b = rnd.choice(data)
bname = b["name"]
bfoll = b["follower_count"]
bdesc = b["description"]
bcountry = b["country"]

lose = False

print (logo)


def game():
  compare(score, lose,a,b,aname, afoll,adesc,acountry,bname,bfoll,bdesc,bcountry)

def compare(score, lose,a,b,aname, afoll,adesc,acountry,bname,bfoll,bdesc,bcountry):
  while lose == False:
    print (f"Compare A: {aname}, a {adesc}, from {acountry}.{vs}\nAgainst B: {bname}, a {bdesc}, from {bcountry}.\n")
    aORb = input("Who has more followers? Type 'A' or 'B'.") 
    if (aORb == "a" and afoll >= bfoll) or (aORb == "b" and bfoll >= afoll):
      cls()
      print (logo)
      score +=1
      print (f"You are right. Your new score is: {score}.\n{aname} has {afoll} million followers and {bname} has {bfoll} million followers.")
      aname = b["name"] #line is wanted with b[name]
      afoll = b["follower_count"]
      adesc = b["description"]
      acountry = b["country"]
      b = rnd.choice(data)
      bname = b["name"]
      bfoll = b["follower_count"]
      bdesc = b["description"]
      bcountry = b["country"]
    #newb(a,b, aname, afoll,adesc,acountry,bname,bfoll,bdesc,bcountry)
    else:
        lose = True
        print(f"Sorry, that's wrong.\n{aname} has {afoll} million followers and {bname} has {bfoll} million followers. Final score: {score}.")  #score return needed now after this line?

def newB(a,b,aname, afoll,adesc,acountry,bname,bfoll,bdesc,bcountry): #no pun intended
    aname = b["name"] #line is wanted with b[name]
    afoll = b["follower_count"]
    adesc = b["description"]
    acountry = b["country"]
    b = rnd.choice(data)
    bname = b["name"]
    bfoll = b["follower_count"]
    bdesc = b["description"]
    bcountry = b["country"]
    return (a,b,aname, afoll,adesc,acountry,bname,bfoll,bdesc,bcountry)

game()