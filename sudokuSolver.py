table = []

def init_table:
	file = open("sudoku.txt", "r")
	countline = 0
	for lines in file:
		while countline < 9
			countchar = 0
			countline++
			for char in lines:
				if countchar < 9 && char > 0 && char < 10
					table.append(char)
					countchar++
				else
					table.append(0)
					countchar++


def is_finished:
	flag = True
	for x in table:
		if x != 0:
			flag = False
			break
	return flag

def compare:


def write: