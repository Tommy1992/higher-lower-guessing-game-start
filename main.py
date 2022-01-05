"""
ToDo list:
1 - import random, art, game_data   CHECK
2 - printing logo1, logo2 VS, in between print Compare A: {var} and then Against B: {var2}, then "Who more follows, type..."
3 - function to access and compare data(imported already), setting var2 to var1 after a right answer - then wait for input of answer again
4 - global variables needed !?(i.e. score)
"""

from art import logo, vs
from game_data import data
import random as rnd
print (logo)


def game():
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
  # print (b)
  # print (bfoll)
  print (f"Compare A: {aname}, a {adesc}, from {acountry}.{vs}\n Against B: {bname}, a {bdesc}, from {bcountry}.\n Who has more followers? Type 'A' or 'B'.")
  #comparing
  


game()


""" data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
"""