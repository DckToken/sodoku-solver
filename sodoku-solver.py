def printBoard(board):
	print(" ╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗ ").encode('utf-8')
	for i in ["a" , "b", "c", "d", "e", "f", "g", "h", "i"]:
		print(i + "║ " + board[0][0] + " │ " + board[0][0] + " │ " + board[0][0] + " ║ " + board[0][0] + " │ " + board[0][0] + " │ " + board[0][0] + " ║ " + board[0][0] + " │ " + board[0][0] + " │ " + board[0][0] + " ║")		
board = [[" "]]
printBoard(board)
