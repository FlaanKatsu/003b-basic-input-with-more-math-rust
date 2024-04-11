#!python3
 
"""
Assignment 5:
Make a Mad Lib

Ask the user to enter a number of words, one for each of the underscored words in the following paragraph.  Once they have finished, display the following story to them with the replacements made in the Mad Lib

Today we picked apple from _PERSON 名1_'s Orchard. I had no idea there were so many different varieties of apples. I ate _ADJECTIVE A1_ apples
 straight off the tree that tasted like _FOOD 01_. Then there was a _ADJECTIVE A2_ apple that looked 
 like a _NOUN N1_.  When our bag was full, we went on a free hay ride to _PLACE L1_ and back. It ended at a hay pile where we got to _VERB 
 V1_ _ADVERB AV1_. I can hardly wait to get home and cook with the apples. We are going to make apple _FOOD F1_ and _THINGS O2_ pies!
"""

名1 = input("enter the name of someone, can be real or made up.(then press enter.)")
A1 = input("enter an adjective: ")
O1 = input("enter the name of a small object, preferably something that can be tasted: ")
A2 = input("enter the name of another adjective: ")
N1 = input("enter a noun: ")
L1 = input("enter a location: ")
V1 = input("enter a verb: ")
AV1 = input("ener an adverb: ")
F1 = input("enter a food: ")
O2 = input("enter a object, something consumable: ")
input("Press enter for the result...")
print(f"\n\nToday we picked apple from {名1}'s Orchard. I had no idea there were so many different varieties of apples. \nI ate {A1} apples straight off the tree that tasted like {O1}. Then there was a {A2} apple that looked like a {N1}. \nWhen our bag was full, we went on a free hay ride to {L1} and back. \nIt ended at a hay pile where we got to {V1} {AV1}. \nI can hardly wait to get home and cook with the apples. We are going to make apple {F1} and {O2} pies!\n\n")