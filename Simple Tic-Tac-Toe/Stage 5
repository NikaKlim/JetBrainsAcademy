a = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
t = "O"
def game_grid():
    print("---------")
    print("|", a[0], a[1], a[2], "|")  # 1.1   1.2   1.3
    print("|", a[3], a[4], a[5], "|")  # 2.1   2.2   2.3
    print("|", a[6], a[7], a[8], "|")  # 3.1   3.2   3.3
    print("---------")
    definite_win()


def definite_win():
    # определение победившего игрока
    if (a[0] == a[1] == a[2] or a[0] == a[4] == a[8] or a[0] == a[3] == a[6]) and a[0]!=" ":
        print(a[0], "wins")
    elif (a[1] == a[4] == a[7] or a[3] == a[4] == a[5]) and a[4]!=" ":
        print(a[4], "wins")
    elif (a[6] == a[7] == a[8] or a[6] == a[4] == a[2]) and a[6]!=" ":
        print(a[6], "wins")
    elif (a[2] == a[5] == a[8]) and a[2]!=" ":
        print(a[2], "wins")
    elif " " not in a:
        print("Draw")
    else:
        change()


def check_position(q1, q2):
    global pos
    if q1 == "1" and q2 == "1":
        pos = a[0]
        return pos
    elif q1 == "1" and q2 == "2":
        pos = a[1]
        return pos
    elif q1 == "1" and q2 == "3":
        pos = a[2]
        return pos
    elif q1 == "2" and q2 == "1":
        pos = a[3]
        return pos
    elif q1 == "2" and q2 == "2":
        pos = a[4]
        return pos
    elif q1 == "2" and q2 == "3":
         pos = a[5]
         return pos
    elif q1 == "3" and q2 == "1":
        pos = a[6]
        return pos
    elif q1 == "3" and q2 == "2":
        pos = a[7]
        return pos
    elif q1 == "3" and q2 == "3":
        pos = a[8]
        return pos


def change():
    global a, q, q1, q2, t
    q = input("Enter the coordinates: ").split(" ")
    q1 = q[0]
    q2 = q[1]
    if check_position(q1, q2) != " " and q1 in "123" and q2 in "123":
        print("This cell is occupied! Choose another one!")
        change()
    elif q1 not in "0123456789" or q2 not in "0123456789":
        print("You should enter numbers!")
        change()
    elif q1 not in "123" or q2 not in "123":
        print("Coordinates should be from 1 to 3!")
        change()
    else:
        global t
        if q1 == "1" and q2 == "1":
            if t=="O":
                t = "X"
                a[0] = "X"
            else:
                t = "O"
                a[0] = "O"
        elif q1 == "1" and q2 == "2":
            if t == "O":
                t = "X"
                a[1] = "X"
            else:
                t = "O"
                a[1] = "O"
        elif q1 == "1" and q2 == "3":
            if t == "O":
                t = "X"
                a[2] = "X"
            else:
                t = "O"
                a[2] = "O"
        elif q1 == "2" and q2 == "1":
            if t == "O":
                t = "X"
                a[3] = "X"
            else:
                t = "O"
                a[3] = "O"
        elif q1 == "2" and q2 == "2":
            if t == "O":
                t = "X"
                a[4] = "X"
            else:
                t = "O"
                a[4] = "O"
        elif q1 == "2" and q2 == "3":
            if t == "O":
                t = "X"
                a[5] = "X"
            else:
                t = "O"
                a[5] = "O"
        elif q1 == "3" and q2 == "1":
            if t == "O":
                t = "X"
                a[6] = "X"
            else:
                t = "O"
                a[6] = "O"
        elif q1 == "3" and q2 == "2":
            if t == "O":
                t = "X"
                a[7] = "X"
            else:
                t = "O"
                a[7] = "O"
        elif q1 == "3" and q2 == "3":
            if t == "O":
                t = "X"
                a[8] = "X"
            else:
                t = "O"
                a[8] = "O"
        game_grid()


game_grid()
