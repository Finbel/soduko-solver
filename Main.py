from Number import Number

# Create the empty sudoku board
matrix = []
for i in range(9):
	row = []
	for j in range(9):
		row.append(Number())
	matrix.append(row)

