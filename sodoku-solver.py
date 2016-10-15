def printBoard(board):
	print(" ╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗ ")
	for i in ["a" , "b", "c", "d", "e", "f", "g", "h", "i"]:
		print(i + "║ " + board[0][0] + " │ " + board[0][0] + " │ " + board[0][0] + " ║ " + board[0][0] + " │ " + board[0][0] + " │ " + board[0][0] + " ║ " + board[0][0] + " │ " + board[0][0] + " │ " + board[0][0] + " ║")
		if i is not "i":
			print(" ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢")
	print(" ╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝ ")
	print("   1   2   3   4   5   6   7   8   9 ")
board = [[" "]]
printBoard(board)
