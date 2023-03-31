print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
user_input = input("\nShipwrecked! You and your shipmates were en route to an island rumored to hold treasure, and were hit by a rogue storm.\nIn a daze, you look around to find yourself alone on a stretch of beach, no ship or shipmates in sight. \nYou decide to look for other survivors.\nWalk left or right down the beach?: ")
if user_input.casefold() != "left":
  print("\nYou've fallen into a hole and broken your legs, suffering until your imminent death!\nGame over.") 
else:
  user_input = input("\nYou're met with a body of water that divides the land. To get across the lake you must swim, or you could walk several miles to go around it.\nSwim or walk? ")
  if user_input.casefold() != "walk":
    print("\nYour flesh is a welcome meal to the piranhas lurking below the water's surface.\nGame over.")
  else:
    user_input = input("\nAfter some time of walking through the dense jungle, something different stands out against the green terrain.\nA wall with three primary-colored doors, appearing practically untouched by the jungle.\nWhich door do you choose?: (Red/Blue/Yellow) ")
    if user_input.casefold() == "yellow":
      print("\nYou win!")
    elif user_input.casefold() == "red":
      print("\nUpon opening the red door you're engulfed in flames.\nGame over.")
    elif user_input.casefold() == "blue":
      print("\nA horde of beasts was behind the blue door and pummels you on sight.\nGame over.")
    else:
      print("\nGame over.")