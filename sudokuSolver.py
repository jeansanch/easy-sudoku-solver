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
# pattern is
# 12#4#6789
# 235#781##

def compare(pos):
0  1  2    3  4  5    6  7  8
9  10 11   12 13 14   15 16 17
18 19 20   21 22 23   24 25 26

27 28 29   30 31 32   33 34 35
36 37 38   39 40 41   42 43 44
45 46 47   48 49 50   51 52 53

54 55 56   57 58 59   60 61 62
63 64 65   66 67 68   69 70 71
72 73 74   75 76 77   78 79 80

	numbers = set([])
	offset = pos % 9
	line = pos / 9
	for i in range(0..9)
		#columns
		if(table[i*9 + offset] != 0):
			numbers.add(table[i*9+offset])
		#row
		if(table[line*9+i] != 0):
			numbers.add(table[line*9+i])
		#3x3
		if( ((offset/3)*3) + ((line/3)*9) + ((i/3)*9) + (i % 3) != 0)
			numbers.add(table[((offset/3)*3) + ((line/3)*9) + ((i/3)*9) + (i % 3)])

def write(pos[x,y?], value):

def run():
	done = 1
	while(done == 1):
		for i, x in enumerate(table):
			if x == 0:
				compare(i)