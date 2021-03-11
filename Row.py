class Row(object)

    def __init__(self, row_number):
        self.row_number = row_number
        self.possible_dict = {1:9,2:9,3:9,4:9,5:9,6:9,7:9,8:9,9:9}

    def update_possible(self,matrix)
    	temp_dictionary = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
    	for i in range(9):
    		for j in range(9):
    			if matrix[row_number][i].is_possible(j):
    				temp_dictionary[j] += 1
    	self.possible_dict = temp_dictionary
