def treasure_map():
    row1 = ["⬜️","⬜️","⬜️"]
    row2 = ["⬜️","⬜️","⬜️"]
    row3 = ["⬜️","⬜️","⬜️"]
    map = [row1, row2, row3]
    print(f"{row1}\n{row2}\n{row3}")
    position = input("Where do you want to put the treasure? ")

    if(len(position) < 2):
        print("Invalid Input")
        return False

    vertical = int(position[1])
    horizontal = int(position[0])

    if(vertical >= 4 or horizontal >= 4):
        print("Invalid Input")
        return False

    map[vertical-1][horizontal-1] = "X"


    print(f"{row1}\n{row2}\n{row3}")
    return True

result = treasure_map()
while(result != True):
    result = treasure_map()
