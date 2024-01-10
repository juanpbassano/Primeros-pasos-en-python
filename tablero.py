def display_board(board):
    for i in range(4):
        print("+-----"*3,end="+\n")
        if i == 3:
            break
        for j in range(3):
            print("|     "*4)

display_board(1)