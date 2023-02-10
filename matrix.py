def createMatrix():
    columns = input("How many Columns ? :") # str
    lines = input("How many Lines ? :") # str
    matrix = []
    for i in range(int(lines)):
            matrix.append([])
            for j in range(int(columns)):
                matrix[i].append(int(input("number position "+ str(i)+","+str(j)+ " : ")))
    return matrix

def createEmptyMatrixWithParameters(lines,columns):
    matrix = []
    for i in range(int(lines)):
            matrix.append([])
            for j in range(int(columns)):
                matrix[i].append(0)
    return matrix

def addMatrix(matrix1,matrix2):
    matrix = []
    if numberOfColumns(matrix1) == numberOfColumns(matrix2):
        if numberOfLines(matrix1) == numberOfLines(matrix2):
            
            matrix = matrix1
            for i in range(numberOfLines(matrix1)):
                for j in range(numberOfColumns(matrix1)):
                    matrix[i][j] = matrix1[i][j] + matrix2[i][j]
            
            return matrix
        else:
            print("numOfLines are different.")
    else:
        
        print("numOfColumns are different.")
    return matrix

def productMatrix(matrix1,matrix2):
    matrix = []
    if numberOfColumns(matrix1) == numberOfLines(matrix2):
        matrix= createEmptyMatrixWithParameters(numberOfLines(matrix1),numberOfColumns(matrix2))

        for i in range(numberOfLines(matrix1)):
                for j in range(numberOfColumns(matrix1)):
                    for k in range(numberOfColumns(matrix2)):
                        matrix[i][j] += matrix1[i][k] * matrix2[k][j]
        return matrix
    else:
        print("numberOfColumns of matrix1 is deifferent of numberOfLines of matrix2.")
        return matrix

    
def numberOfLines(matrix):
    return len(matrix)

def numberOfColumns(matrix):
    return len(matrix[0])

def showMatrix(matrix):
    print("Matrix :")
    for lines in matrix :
        print(lines)


def showLine(matrix, line):
    print("Line " + str(line) + " :")
    print(matrix[line])


def showColumn(matrix, column):
    column_temp = []
    for line in matrix:
        column_temp.append(line[column])
    print("Column " + str(column) + " :")
    showMatrix(column_temp)




#---------------------------------------------------------


matrix1 = createMatrix()
showMatrix(matrix1)

matrix2 = createMatrix()
showMatrix(matrix2)

matrix3 = productMatrix(matrix1,matrix2)
showMatrix(matrix3)