def printBoard(board):
    n = 0
    print(" ╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗ ")
    for i in ["a" , "b", "c", "d", "e", "f", "g", "h", "i"]:
        print(i + "║ " + str(board[n][0][0]) + " │ " + str(board[n][0][1]) + " │ " + str(board[n][0][2]) + " ║ " + str(board[n][1][0]) + " │ " + str(board[n][1][1]) + " │ " + str(board[n][1][2]) + " ║ " + str(board[n][2][0]) + " │ " + str(board[n][2][1]) + " │ " + str(board[n][2][2]) + " ║")
        print("Row " + str(n))
        n += 1
        if i is not "i":
            print(" ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢")
    print(" ╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝ ")
    print("   1   2   3   4   5   6   7   8   9 ")
    print(board[2][0][0])
#board = [[[3, 9, 1],[2, 8, 6],[5, 7, 4]],[[4, 8, 7],[3, 5, 9],[1, 2, 6]],[[6, 5, 2],[7, 1, 4],[8, 3, 9]],[[8, 7, 5],[4, 3, 1],[6, 9, 2]],[[2, 1, 3],[9, 6, 7],[4, 8, 5]],[[9, 6, 4],[5, 2, 8],[7, 1, 3]],[[1, 4, 6]],[6, 7, 3],[2, 5, 8]],[[5, 3, 7],[1, 4, 2],[9, 6, 7]],[[7, 2, 6],[8, 9, 5],[3, 4, 1]]] #for testin'!
printBoard(board)
for row in range(0, 9):
    for col in range(0, 9):
        for i in range(0, 3):
            print("Data for row {}, column {} and i {}".format(str(row), str(col), str(i)))
                print(board[row][col][i])
