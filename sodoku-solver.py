def printBoard(board):
	n = 0
	print(" ╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗ ")
	for i in ["a" , "b", "c", "d", "e", "f", "g", "h", "i"]:
		print(i + "║ " + str(board[n][0][0]) + " │ " + str(board[n][0][1]) + " │ " + str(board[n][0][2]) + " ║ " + str(board[n][1][0]) + " │ " + str(board[n][1][1]) + " │ " + str(board[n][1][2]) + " ║ " + str(board[n][2][0]) + " │ " + str(board[n][2][1]) + " │ " + str(board[n][2][2]) + " ║")
		n =+ 1
		if i is not "i":
			print(" ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢")
	print(" ╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝ ")
	print("   1   2   3   4   5   6   7   8   9 ")
board = [[[3, 7, 8],[4, 5, 9],[8, 9, 6]],[[2, 8, 4],[5, 6, 9],[2, 4, 5]]] #for testin'!
printBoard(board)
