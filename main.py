"""
ToDo list:
1 - CHECK import random, art, game_data   
2 - CHECK printing logo1, logo2 VS, in between print Compare A: {var} and then Against B: {var2}, then "Who more follows, type..." 
3 - function to access and compare data(imported already), setting var2 to var1 after a right answer - then wait for input of answer again
3.1 - compare fct:
4 - global variables needed !?(i.e. score)
"""

from art import logo, vs
from game_data import data
import random as rnd

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

print (logo)


def game():
  # print (b)
  # print (bfoll)
  print (f"Compare A: {aname}, a {adesc}, from {acountry}.{vs}\nAgainst B: {bname}, a {bdesc}, from {bcountry}.\n")
  #comparing code
  compare(score)

def compare(score):
  aORb = input("Who has more followers? Type 'A' or 'B'.") 
  if (aORb.lower == "a" and afoll >= bfoll) or (aORb.lower == "b" and bfoll >= afoll):
    score +=1
    print (f"You are right. Your new score is: {score}.\n{aname} has {afoll} followers and {bname} has {bfoll} followers.")
    return score
  else:
    print(f"Sorry, that's wrong.\n{aname} has {afoll} million followers and {bname} has {bfoll} million followers. Final score: {score}.")  #score return needed now after this line?



game()

""" data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
"""