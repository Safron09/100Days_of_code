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
print("You may be the frist who can find it!")
skeleton = input("Are you excited?\n")
print("Lets Begin!")
print("You sould type your answers same as they have been asked or you will be perished by cosmic power!")

choice1 = input("Would you like go left or right? \n")
if choice1.lower() == "left":
  print("You came to the room with slicing blades.")
  choice2 = input("Will you jump or sit? \n")
  if choice2.lower() == "jump":
    print("Yes, you dodged those blades!")
    choice3 = input("Are you going to run or hide? \n")
    if choice3.lower() == "hide":
      print("Tiger didnt see you, good job!")
      choice4 = input("You see 5 chests. One is yellow, second is red, third is green, fourth is blue, fifth is black. Wich one will you open? \n")
      if choice4.lower() == "black":
        print("YOU ARE TRULY A TREASURE HUNTER! THE GOLD IS YOURS!!! YOU WON")
      elif choice4.lower() == "red":
          print("Chest full of spiders! Game over! Youve died")
      elif choice4.lower() == "yellow":
        print("Toxins, nooo. Game over! You are poisined")
      elif choice4.lower() == "green":
        print("You just died")
      else:
        print("DAmn, you died")
    else:
        print("You can`t outrun your death! Game OVER! You died")
  else:
    print("What did you expected? Game OVER, yove been sliced!")
elif choice1 == "right":
  print("Wild boar ate your leg! Game OVER!")
else:
  print("FOLLOW THE RuLES, you died!")

print()
#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload