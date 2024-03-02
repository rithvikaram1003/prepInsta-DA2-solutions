positions = list(['🟩','🟩','🟩','🞨','🟫','🟫','🟫'])

print("[ 0 ,  1 ,  2 ,  3 ,  4 ,  5 ,  6 ]")
print(positions)

print(" ")

while True:
    pos = input("Press q to Quit \nEnter position of piece you want to move: ")

    if pos == 'q':
        print("You LOSE!")
        break

    pos = int(pos)

    if pos < 0 or pos > 6:
        print("Invalid Move")
        continue

    if positions[pos] == '🞨':
        print("Invalid Move")
        continue

    if positions[pos] == '🟩':
        if (pos + 1) <= 6 and positions[pos + 1] == '🞨':
            pass
        elif (pos + 2) <= 6 and positions[pos + 2] == '🞨' and positions[pos + 1] == '🟫':
            pass
        else:
            print("Invalid Move")
            continue

    if positions[pos] == '🟫':
        if (pos - 1) >= 0 and positions[pos - 1] == '🞨':
            pass
        elif (pos - 2) >= 0 and positions[pos - 2] == '🞨' and positions[pos - 1] == '🟩':
            pass
        else:
            print("Invalid Move")
            continue

    pos2 = 0

    if positions[pos] == '🟩':
        if positions[pos + 1] == '🞨':
            pos2 = (pos + 1)
        elif positions[pos + 2] == '🞨':
            pos2 = (pos + 2)
    elif positions[pos] == '🟫':
        if positions[pos - 1] == '🞨':
            pos2 = (pos - 1)
        elif positions[pos - 2] == '🞨':
            pos2 = (pos - 2)

    positions[pos], positions[pos2] = positions[pos2], positions[pos]

    print("[ 0 ,  1 ,  2 ,  3 ,  4 ,  5 ,  6 ]")
    print(positions)

    if positions == ['🟫','🟫','🟫','🞨','🟩','🟩','🟩']:
        print(" ")
        print("You WIN!")
        break
