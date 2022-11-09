from sim import *

armour = ["wrist","shoulders","back","head","neck","chest","waist","hands","finger","legs","feet","main_hand","off_hand", "trinket_1","trinket_2"]

# print(armour[1])

def build(armour_piece, name, id, ilvl):

    name = str(name).replace(" ","_").lower()
    props_NAME=f"{armour_piece}={name}"
    props_ID=f"id={id}"
    if(ilvl != -1):
        props_ILVL=f"iLevel={ilvl}"
        return f"{props_NAME},{props_ID},{props_ILVL}"
    else:
        return f"{props_NAME},{props_ID}"
    

def menu():

    print("SimCraft Gear Compare - Alpha")
    for x in range(len(armour)):
        print(f"\033[0;32m{x:^2}: {armour[x]:^15}\033[0;37m")
    
    
    print("\033[1;33mPlease input your selection:", end=' ')

    user_selection = input()

    user_selection = int(user_selection) # Converting the user input to a string
    
    if(user_selection == -1):
        return -1

    # Check that user_selection is in the proper range
    if (user_selection < 0 or user_selection > 14):
        return -2
        
    
    return user_selection
    
# Returns attributes in order, name, id and level
def get_attr():
    # TODO - Add enchantments
    print("\033[1;35mEnter Item Name:\033[0;37m", end=' ')
    x = input() # Item name
    print("\033[1;35mEnter Item ID for stats look up:\033[0;37m", end=' ')
    y = input() # Item ID
    print("\033[1;35mEnter Item Level (-1 if not specified):\033[0;37m", end=' ')
    z = input() # Item Level

    return (x,y,z)

def writeSIMCFile(output, armour_type):
    path = f"./gear_compare/{armour_type}.simc"
    file = open(path, "w")
    file.write(output)
    print(f"Writing SIMCFile for {armour_type}")
    return path

def main_loop():
    selection = menu()
    match selection:
        case -1:
            print("Exiting Gear Compare")
            exit()
        case -2:
            # print("this is -2")
            main_loop() # Restart the menu selection if it is invalid
        case num if num in range(0, 15):
            print("in the range")
            attr = get_attr()
            out = build(armour[selection],attr[0],attr[1],attr[2])

            # Pass 'out' to writeSIMCFile
            print(f"writeSIMCFile(output=[{out}],armour_type={armour[selection]})")
            writeSIMCFile(out, armour[selection])
        case other:
            print("Unexpected input -- Exiting")
            exit()


main_loop()


# writeSIMCFile("test", "test")
