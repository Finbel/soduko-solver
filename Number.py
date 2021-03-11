class Number(object):

	# Define an unset number with all possibilities
    def __init__(self):
        self.possible = set([1,2,3,4,5,6,7,8,9])
        self.value = 0

    # Remove a possibility
    def remove(self, number):
        self.possible.discard(number)

    # Set the value of the number square
    def set(self,number):
    	self,value = number
    	self.possible.clear()

    # Check if a number is possible
    def is_possible(self,number):
    	return number in self.possible

    # Check if the number is set
    def is_set(self):
    	return self.value != 0