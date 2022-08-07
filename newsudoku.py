# building array
sudoku = []
with open("sudoku.txt") as problem:
    fileread = problem.readlines()
for i in range(9):
    sudoku.append(list(map(int,fileread[i].split())))
options = {}

# initialise options with all and count blanks
blanks = 0
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            options["{}{}".format(i,j)] = {1,2,3,4,5,6,7,8,9}
            blanks += 1

#reduce options horizontal,vertical,box
def ophor(sud,opt,x,y):
    for j in range(9):
        if sud[x][j] != 0:
            opt["{}{}".format(x,y)].discard(sudoku[x][j])

def opver(sud,opt,x,y):
    for i in range(9):
        if sud[i][y] != 0:
            opt["{}{}".format(x,y)].discard(sudoku[i][y])

def opbox(sud,opt,x,y):
    for i in range((x//3)*3,(x//3)*3+3):
        for j in range((y//3)*3,(y//3)*3+3):
            if sud[i][j] != 0:
                opt["{}{}".format(x,y)].discard(sudoku[i][j])

while blanks>0:
    # reduce options for blanks
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                ophor(sudoku,options,i,j)
                opver(sudoku,options,i,j)
                opbox(sudoku,options,i,j)

    # fill in blanks
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0 and len(options["{}{}".format(i,j)]) == 1:
                sudoku[i][j] = list(options["{}{}".format(i,j)])[0]
                blanks -= 1
                del options["{}{}".format(i,j)]

for i in range(9):
    print(sudoku[i])