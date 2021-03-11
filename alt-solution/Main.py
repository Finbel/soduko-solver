from collections import Counter

def box_to_list(box_corners,matrix):
	lst = []
	for i in range(box_corners[0],box_corners[1]+1):
		for j in range(box_corners[2],box_corners[3]+1):
			lst.append(matrix[i][j])
	return lst

def print_matrix(matrix):
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			print(matrix[i][j], end="\t")
		print()

def index_to_box(i,j):
	if i<3:
		row_indices = (0,2)
	elif i>5:
		row_indices = (6,8)
	else:
		row_indices = (3,5)
	if j<3:
		column_indices = (0,2)
	elif j>5:
		column_indices = (6,8)
	else:
		column_indices = (3,5)		
	return row_indices,column_indices

def pop_mat():
	matrix = []
	for i in range(9):
		row = []
		for j in range(9):
			row.append(True)
		matrix.append(row)
	return matrix


def set_false(possibility_dictionary, i, j):
	for number in range(1,10):
		possibility_dictionary[number][i][j] = False
	return possibility_dictionary

def update_numbersets(possibilities,i,j):
	# Make it known cross row and column
	for k in range(9):
		possibilities[i][k] = False
		possibilities[k][j] = False
	# Make it known in the box
	return update_box(possibilities,i,j)


def update_box(possibilities,i,j):
	#get indices
	row_indices, col_indices = index_to_box(i,j)
	row_from,row_to = row_indices
	col_from,col_to = col_indices 
	#iterate through the box and set to false
	for a in range(row_from,row_to+1):
		for b in range(col_from,col_to+1):
			possibilities[a][b] = False
	return possibilities

def add_value_to_row(possibilities,value_matrix):
	for i in range(9):
		if Counter(possibilities[i])[True] == 1:
			found_one = True
			for j in range(9):
				if possibilities[i][j] == True:
					value_matrix[i][j] = value
	return (possibilities,value_matrix)

def add_value_to_column(possibilities,value_matrix):
	for i in range(9):
		column = [row[i] for row in possibilities]
		if Counter(column)[True] == 1:
			found_one = True
			for j in range(9):
				if possibilities[j][i] == True:
					possibilities[j][i] = False
					value_matrix[j][i] = value
	return (possibilities,value_matrix)

def update_possibilities(value_matrix, unknown_matrix, possibility_dictionary):
	for i in range(9):
		for j in range(9):
			if value_matrix[i][j] != 0 and unknown_matrix[i][j] == True:
				possibility_dictionary = set_false(possibility_dictionary,i,j)

				value = value_matrix[i][j]
				possibilities = possibility_dictionary[value]

				possibility_dictionary[value] = update_numbersets(possibilities,i,j)

				unknown_matrix[i][j] = False
	return possibility_dictionary

boxes = [[0,2,0,2],[3,5,0,2],[6,8,0,2],
		[0,2,3,5],[3,5,3,5],[6,8,3,5],
		[0,2,6,8],[3,5,6,8],[6,8,6,8]]

possibility_dictionary = {1:pop_mat(),2:pop_mat(),3:pop_mat(),
	4:pop_mat(),5:pop_mat(),6:pop_mat(),
	7:pop_mat(),8:pop_mat(),9:pop_mat()}


f = open("input.txt")
lines = f.readlines()

value_matrix = []
for line in lines:
	value_matrix.append([int(x) for x in list(line)[:-1]])

unknown_matrix = pop_mat()

print_matrix(value_matrix)
print()
iteration = 0
while(iteration < 10):

	possibility_dictionary = update_possibilities(value_matrix, unknown_matrix, possibility_dictionary)

	for value in range(1,10):
		possibilities = possibility_dictionary[value]
		# Check each row for singular True-value
		possibilities, value_matrix = add_value_to_row(possibilities, value_matrix)
		possibilities = update_possibilities(value_matrix, unknown_matrix, possibility_dictionary)[value]
		# Check each column for singular True-value
		possibilities, value_matrix = add_value_to_column(possibilities, value_matrix)
		possibilities = update_possibilities(value_matrix, unknown_matrix, possibility_dictionary)[value]
		# # Check each box for singular True-value
		for box in boxes:
			box_list = box_to_list(box,possibilities)
			if Counter(box_list)[True] == 1:
				found_one = True
				for i in range(box[0],box[1]+1):
					for j in range(box[2],box[3]+1):
						if possibilities[i][j] == True:
							possibilities[i][j] = False
							value_matrix[i][j] = value
	iteration += 1
	# print(found_one)
	# print(iteration < 100)
print()
print(iteration)
print()
print_matrix(value_matrix)