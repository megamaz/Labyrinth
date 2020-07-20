print("loading...")
import random, arcade, time, sys
import Labyrinthfacts
from Labyrinthfacts import fact
objx = 0
objy = 0
map_pos = ""
test_area = ""
for i in range(10):
    letters = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
    test_area += random.choice(letters)
print(test_area)
print("\n" * 500)
print(f'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Welcome to my game! It is still a WIP, you have early access. (version 1.11.2)
LAST UPDATE:
 - How to play
BUG FIXES:

DEBUG FEATURES (Temporary):
- Current map
- Current position
- Spawn area choosing
- Shows in which direction you can move

 CURRENT MAPS (code):
 - home_1
 - village
 - home_hallway
 - home_room
 - forest
 - castle_FM
 - castle_FL
 HOW TO PLAY:
  - A map will show up. 
     - █ are walls. You cannot walk through them.
     - You are O. You can move around by typing in U D L R (up down left right)
     - = are paths. They switch the map to another area.
 CREDITS AND HELP!
 github
 - megamaz (main worker, idea for game)
 - lmazuel (helper)
''')
print("Fun fact:")
fact()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print()
wallpos = []
trappos = []
monsterpos = []
pathpos = []
fakewallpos = []
inviswall = []
map_poss = ["home_1", "home_hallway", "home_room", "forest", "castle_fm", "castle_fl", test_area]
map_pos = str(input("Enter code spawn area. (said in description above.) "))
map_pos = map_pos.lower()
if not map_pos in map_poss:
    map_pos = random.choice(map_poss)
def Dialogue(dialogue):
    letters = 0
    print("")
    print("\n" * 100)
    while letters != (len(dialogue) + 2):
        print("\n" * 45)
        time.sleep(0.03)
        print(dialogue[:letters])
        letters += 1
    print("\n" * 45)
def clear_map():
    wallpos.clear()
    trappos.clear()
    monsterpos.clear()
    pathpos.clear()
    fakewallpos.clear()
def tree(objx, objy):
    wallpos.append((objx, objy))
    objx += 1
    fakewallpos.append((objx, objy))
    objx -= 2
    fakewallpos.append((objx, objy))
    objx += 1
    objy += 1
    fakewallpos.append((objx, objy))
    objy -= 2
    fakewallpos.append((objx, objy))
def MAP():
    if map_pos == "village":
        clear_map()
        wallpos.append((2,3))
        wallpos.append((2,4))
        wallpos.append((3,3))
        wallpos.append((3,4))
        wallpos.append((4,4))
        wallpos.append((4,3))
        wallpos.append((6,3))
        wallpos.append((6,4))
        wallpos.append((7,3))
        pathpos.append((7,4))
        wallpos.append((8,3))
        wallpos.append((8,4))
        wallpos.append((2,6))
        wallpos.append((2,7))
        wallpos.append((3,6))
        wallpos.append((3,7))
        wallpos.append((4,6))
        wallpos.append((4,7))
        wallpos.append((6,6))
        wallpos.append((6,7))
        wallpos.append((7,6))
        wallpos.append((7,7))
        wallpos.append((8,6))
        wallpos.append((8,7))
        pathpos.append((9,8))
        inviswall.append((9,9))
    
    elif map_pos == "home_1":
        clear_map()
        objx = 1
        objy = 1
        while objx != 9:
            wallpos.append((objx,objy))
            objx+= 1
        while objy != 9:
            wallpos.append((objx, objy))
            objy+=1
        while objx != 6:
            wallpos.append((objx, objy))
            objx -= 1
        pathpos.append ((objx, objy))
        objx -= 1
        while objx != 1:
            wallpos.append((objx, objy))
            objx -= 1
        while objy != 0:
            wallpos.append((objx, objy))
            objy -= 1
        objx = 8
        objy = 4
        while objy != 8:
            wallpos.append((objx, objy))
            objy += 1
        objx = 4
        objy = 5
        wallpos.append((objx, objy))
        objy = 6
        wallpos.append((objx,objy))
        objx = 2
        objy = 5
        wallpos.append((objx, objy))
        objy = 6
        wallpos.append((objx,objy))
        pathpos.append((2,2))
    
    elif map_pos == "home_hallway":
        clear_map()
        objx = 9
        objy = 4
        while objx != 7:
            wallpos.append((objx, objy))
            objx -=1
        pathpos.append((objx,objy))
        objx -= 1
        while objx != 3:
            wallpos.append((objx, objy))
            objx -= 1
        pathpos.append((objx,objy))
        objx -= 1
        while objx != 0:
            wallpos.append((objx, objy))
            objx -= 1
        objy = 7
        objx = 9
        while objx != 5:
            wallpos.append((objx,objy))
            objx -= 1
        pathpos.append((objx, objy))
        objx -= 1
        while objx != 0:
            wallpos.append((objx, objy))
            objx -= 1
        pathpos.append((9,6))
    elif map_pos == "home_room":
        clear_map()
        objx = 3
        objy = 3
        while objx != 7:
            wallpos.append((objx, objy))
            objx += 1
        objx -= 1
        while objy != 8:
            wallpos.append((objx, objy))
            objy += 1
        objy -= 1
        objx -= 1
        wallpos.append((objx, objy))
        while objy != 10:
            wallpos.append((objx, objy))
            objy += 1
        objy -= 1
        objx -= 1
        pathpos.append((objx, objy))
        objx -= 1
        while objy != 6:
            wallpos.append((objx, objy))
            objy -= 1
        objy += 1
        while objx != 2:
            wallpos.append((objx, objy))
            objx -= 1
        while objy != 2:
            wallpos.append((objx, objy))
            objy -= 1
        objy += 1
        objx = 5
        objy = 5
        fakewallpos.append((objx, objy))
        objy -= 1
        fakewallpos.append((objx, objy))
    elif map_pos == "forest":
        clear_map()
        objx = 3
        objy = 3
        wallpos.append((objx, objy))
        objx += 1
        fakewallpos.append((objx, objy))
        objx -= 2
        fakewallpos.append((objx, objy))
        objx += 1
        objy += 1
        fakewallpos.append((objx, objy))
        objy -= 2
        fakewallpos.append((objx, objy))
        objx = 8
        objy = 2
        wallpos.append((objx, objy))
        objx += 1
        fakewallpos.append((objx, objy))
        objx -= 2
        fakewallpos.append((objx, objy))
        objx += 1
        objy += 1
        fakewallpos.append((objx, objy))
        objy -= 2
        fakewallpos.append((objx, objy))
        objx = 5
        objy = 5
        wallpos.append((objx, objy))
        objx += 1
        fakewallpos.append((objx, objy))
        objx -= 2
        fakewallpos.append((objx, objy))
        objx += 1
        objy += 1
        fakewallpos.append((objx, objy))
        objy -= 2
        fakewallpos.append((objx, objy))
        objx = 6
        objy = 8
        wallpos.append((objx, objy))
        objx += 1
        fakewallpos.append((objx, objy))
        objx -= 2
        fakewallpos.append((objx, objy))
        objx += 1
        objy += 1
        fakewallpos.append((objx, objy))
        objy -= 2
        fakewallpos.append((objx, objy))
        pathpos.append((1,1))
        pathpos.append((9,9))
    elif map_pos == "castle_fm":
        clear_map()
        objx = 2
        objy = 2
        wallpos.append((objx, objy))
        objx += 1
        fakewallpos.append((objx, objy))
        objx -= 2
        fakewallpos.append((objx, objy))
        objx += 1
        objy += 1
        fakewallpos.append((objx, objy))
        objy -= 2
        fakewallpos.append((objx, objy))
        objx = 6
        objy = 3
        wallpos.append((objx, objy))
        objx += 1
        fakewallpos.append((objx, objy))
        objx -= 2
        fakewallpos.append((objx, objy))
        objx += 1
        objy += 1
        fakewallpos.append((objx, objy))
        objy -= 2
        fakewallpos.append((objx, objy))
        objy = 5
        objx = 1
        wallpos.append((objx, objy))
        while objy != 10:
            objy+= 1
            wallpos.append((objx, objy))
        objy = 7
        objx = 2
        while objy != 10:
            while objx != 10:
                wallpos.append((objx, objy))
                objx += 1
            objy += 1
            objx = 2
        objx = 9
        objy = 5
        wallpos.append((objx, objy))
        objy += 1
        wallpos.append((objx, objy))
        objy += 1
        wallpos.append((objx, objy))
        objy += 1 
        wallpos.append((objx, objy))
        objx = 1
        objy = 1
        pathpos.append((objx, objy))
        objx = 5
        objy = 8
        wallpos.remove((objx, objy))
        pathpos.append((objx, objy))
        pathpos.append((1, 4))
    elif map_pos == "castle_fl":
        clear_map()
        tree(2, 5)
        tree(4, 3)
        (objx, objy) = (9, 5)
        wallpos.append((objx, objy))
        while objy != 9:
            wallpos.append((objx, objy))
            objy += 1
        while objx != 3:
            wallpos.append((objx, objy))
            objx -= 1
        wallpos.append((objx, objy))
        objy -= 1
        while objx != 9:
            wallpos.append((objx, objy))
            objx += 1
        wallpos.append((objx, objy))
        objy -= 1
        while objx != 2:
            wallpos.append((objx, objy))
            objx -= 1
        pathpos.append((9, 4))
    elif map_pos == test_area: #test area
        clear_map()
        pathpos.append((1, 1))
        trappos.append((1, 2))
        monsterpos.append((1, 3))
        wallpos.append((1,4))
        fakewallpos.append((1,5))
        inviswall.append((1,6))
        
MAP()    
print()
if map_pos != "forest":
    X = 5
    Y = 5
else:
    (X, Y) = (4, 4)
if (X, Y) in wallpos:
    wallpos.remove((X, Y))

for trap in trappos:
    if trap in wallpos:
        wallpos.remove(trap)
    
print("Map generated")

def show_map():
    for y in range(0,10):
        line = ""

        for x in range(0,10):
            if (x,y) in wallpos:
                line += "█"
            elif (x, y) == (X, Y):
                line += "O"
            elif (x, y) in trappos:
                line += "X"
            elif (x, y) in monsterpos:
                line += "%"
            elif (x, y) in pathpos:
                line+= "="
            elif (x, y) in fakewallpos:
                line += "#"
            elif (x, y) in inviswall:
                line += " "
            else:
                line += " "
            
        print(line)
    print()
print("\n" * 100)
while True:
    print("Your position: (" + str(X) + ", " + str(Y) + ")")
    print("Your map: " + map_pos)
    if map_pos == test_area:
        print("(test area)")
    upPossible = False
    downPossible = False
    leftPossible = False
    rightPossible = False

    leftprint = False
    rightprint = False
    upprint = False
    downprint = False

    TRAPupPossible = True
    TRAPdownPossible = True
    TRAPleftPossible = True
    TRAPrightPossible = True
    MAP()
    show_map()

    print("You can move:")
    if (X - 1, Y) not in wallpos and X > 1:
        print(" - Left")
        leftprint = True
        leftPossible = True
    if (X + 1, Y) not in wallpos and X < 9:
        print(" - Right")
        rightprint = True
        rightPossible = True
    if (X, Y - 1) not in wallpos and Y > 1:
        print(" - Up")
        upprint = True
        upPossible = True
    if (X, Y + 1) not in wallpos and Y < 9:
        print(" - Down")
        downprint = True
        downPossible = True
    if (X - 1, Y) not in inviswall and X > 1:
        if not leftprint:
            print(" - Left")
        leftPossible = True
    if (X + 1, Y) not in inviswall and X < 9:
        if not rightprint:
            print(" - Right")
        rightPossible = True
    if (X, Y - 1) not in inviswall and Y > 1:
        if not upprint:
            print(" - Up")
        upPossible = True
    if (X, Y + 1) not in inviswall and Y < 9:
        if not downprint:
            print(" - Down")
        downPossible = True
    if downPossible == False:
        print()
    if upPossible == False:
        print()
    if leftPossible == False:
        print()
    if rightPossible == False:
        print()
    if all([not upPossible, not downPossible, not leftPossible, not rightPossible]):
        print("You're stuck between four walls!!!!")
        break
    move = input("Which way will you move? U / D / L / R / Q: ")
    move = move.upper()
    if move == "U":
        print("You moved up one square.")
        if not upPossible:
            Y = ((-1 * Y) % 9) + 1
        else:
            Y -= 1
    elif move == "D":
        print("You moved down one square.")
        if not downPossible:
            Y = Y % 9
        else:
            Y += 1
    elif move == "L":
        print("You moved left one square.")
        if not leftPossible:
            X = ((-1 * X) % 9) + 1
        else:
            X -= 1
    elif move == "R":
        print("You moved right one square.")
        if not rightPossible:
            X = X % 9
        else:
            X += 1
    elif move == "Q":
        print("Alright. Stopping game.")
        break
    else:
        print("Unrecognized movement option. Please enter U / D / L / R / Q")
    if (X, Y) in trappos:
        print("You landed in a trap. You died!")
        sys.exit()
    if (X, Y) in monsterpos:
        print("A monster killed you.")
        sys.exit()
    if (X, Y) in pathpos:
        if map_pos == "home_1" and (X, Y) == (2, 2):
            map_pos = "home_hallway"        
            X = 9
            Y = 5
        elif map_pos == "home_hallway" and (X, Y) == (9, 6):
            map_pos = "home_1"
            X = 2
            Y = 3
        elif map_pos == "home_1" and (X, Y) == (6,9):
            map_pos = "village"
            X = 7
            Y = 5
        elif map_pos == "village" and (X, Y) == (7,4):
            map_pos = "home_1"
            X = 6
            Y = 8
        elif map_pos == "village" and (X, Y) == (9,8):
            map_pos = "forest"
            X = 1
            Y = 2
        elif map_pos == "forest" and (X, Y) == (1,1):
            map_pos = "village"
            X = 9
            Y = 7
        elif map_pos == "home_room" and (X, Y) == (4, 9):
            map_pos = "home_hallway"
            X = 3
            Y = 4
        elif map_pos == "home_hallway" and (X, Y) == (3, 4):
            map_pos = "home_room"
            X = 4
            Y = 9
        elif map_pos == "forest" and (X, Y) == (9, 9):
            map_pos = "castle_fm"
            (X, Y) = (1, 1)
        elif map_pos == "castle_fm" and (X, Y) == (1, 1):
            map_pos = "forest"
            (X, Y) = (9, 9)
        elif map_pos == "castle_fl" and (X, Y) == (9, 4):
            map_pos = "castle_fm"
            (X, Y) = (2, 4)
        elif map_pos == "castle_fm" and (X, Y) == (1, 4):
            map_pos = "castle_fl"
            (X, Y) = (8, 4)
    print("\n" * 100)
    if X == 0:
        X = 1
print()
print("Game code ended.")