table = []

def init_table():
	file = open("sudoku.txt", "r")
	countline = 0
	for lines in file:
		print("LINES > ",lines)
		countchar = 0
		countline += 1
		if countline < 10:
			for char in lines:
				print("CHAR > ",char)
				if countchar < 9 and int(char) > 0 and int(char) < 10:
					table.append(char)
					countchar += 1
				elif char != '\n':
					table.append(0)
					countchar += 1
		else:
			break
	#printSolut()

def compare(pos):
	numbers = set([])
	free = [1,2,3,4,5,6,7,8,9]
	offset = int(pos % 9) #27%9 = 0
	line = int(pos / 9) # 27/9 = 3
	for i in range(0,9):
		#columns
		if(table[i*9 + offset] != 0):
			numbers.add(table[i*9+offset])
		#row
		if(table[line*9+i] != 0):
			numbers.add(table[line*9+i])
		#3x3
		if( (int(offset/3)*3) + (int(line/3)*27) + (int(i/3)*9) + (i % 3) != 0):
			numbers.add(table[(int(offset/3)*3) + (int(line/3)*27) + (int(i/3)*9) + (i % 3)])
	for i in numbers:
		try:
			free.remove(int(i))
		except:
			pass
	if len(free) == 1:
		print("ADDING > ",free[0]," IN > (",line+1,",",offset+1,")")
		write(pos, free[0])
		return 1
	# TODO ------------------ Simulation for possible solutions ------------------
	return 0

def write(pos, value):
	table[pos] = value

def run():
	init_table()
	done = 0
	changed = 1
	while(done == 0 and changed == 1):
		changed = 0
		done = 1
		for i, x in enumerate(table):
			if x == 0:
				done = 0
				if (compare(i) == 1):
					changed = 1
	printSolut()

def printSolut():
	count = 0
	for i in table:
		print(" ",i,"|", end = '')
		count += 1
		if count == 9:
			print("\n---------------------------------------------")
			count = 0

run()