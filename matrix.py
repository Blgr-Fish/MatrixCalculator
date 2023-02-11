from random import randint
import copy

# Create a matrix based on the lines and columns given by the user
def createMatrix():
    columns = input("How many Columns ? :") # str
    lines = input("How many Lines ? :") # str
    matrix = []
    for i in range(int(lines)):
            matrix.append([])
            for j in range(int(columns)):
                matrix[i].append(int(input("number position "+ str(i)+","+str(j)+ " : ")))
    return matrix

# Create an empty matrix with lines and columns given in parameters
def createEmptyMatrixWithParameters(lines,columns):
    matrix = []
    for i in range(int(lines)):
            matrix.append([])
            for j in range(int(columns)):
                matrix[i].append(0)
    return matrix

# Create an identity matrix filled with 1 in the diagonal, else 0.
def createIdentityMatrixWithParameters(lines,columns):
    matrix = []
    for i in range(int(lines)):
            matrix.append([])
            for j in range(int(columns)):
                matrix[i].append(int(i==j))
    return matrix

# Create a matrix with random values baed on the lines and columns given by the user
def createRandomMatrix():
    columns = input("How many Columns ? :") # str
    lines = input("How many Lines ? :") # str
    matrix = []
    for i in range(int(lines)):
            matrix.append([])
            for j in range(int(columns)):
                matrix[i].append(randint(1,100))
    return matrix

# Create a transpose of a given matrix
def createTransposeMatrix(matrix):
    matrixOut = createEmptyMatrixWithParameters(numberOfColumns(matrix),numberOfLines(matrix))
    for i in range(numberOfLines(matrixOut)):
        for j in range(numberOfColumns(matrixOut)):
            matrixOut[i][j] = matrix[j][i]
    return matrixOut    
    
# Create a permuted matrix two lines of a given matrix and its two lines
def createPermutationMatrix(line1,line2,matrix):
    return 

# Sum 2 matrixes to make a third one
def addMatrix(matrix1,matrix2):
    matrix = []
    if numberOfColumns(matrix1) == numberOfColumns(matrix2):
        if numberOfLines(matrix1) == numberOfLines(matrix2):
            
            matrix = copy.deepcopy(matrix1) # we copy the elements of matrix1 into matrix using the copy module , else, matrix and matrix1 would be the same matrix
            for i in range(numberOfLines(matrix1)):
                for j in range(numberOfColumns(matrix1)):
                    matrix[i][j] = matrix1[i][j] + matrix2[i][j]
            
            return matrix
        else:
            print("numOfLines are different.")
    else:
        
        print("numOfColumns are different.")
    return matrix

# Product 2 matrixes to make a third one
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

# return the number of lines of a given matrix  
def numberOfLines(matrix):
    return len(matrix)

# return the number of columns of a given matrix
def numberOfColumns(matrix):
    return len(matrix[0])

# print the matrix 
def showMatrix(matrix):
    print("Matrix :")
    for lines in matrix :
        print(lines)

# print a specific line of a given matrix
def showLine(matrix, line):
    print("Line " + str(line) + " :")
    print(matrix[line])

# print a specific column of a given matrix
def showColumn(matrix, column):
    column_temp = []
    for line in matrix:
        column_temp.append(line[column])
    print("Column " + str(column) + " :")
    showMatrix(column_temp)




#---------------------------------------------------------

matrix1 = createRandomMatrix()
showMatrix(matrix1)
print()
matrixIdentity = createIdentityMatrixWithParameters(numberOfLines(matrix1),numberOfColumns(matrix1))
print()

transposematrix = createTransposeMatrix(matrix1)
showMatrix(transposematrix)
print()

showMatrix(matrix1)

"""matrix1 = createMatrix()
showMatrix(matrix1)

matrix2 = createMatrix()
showMatrix(matrix2)

matrix3 = productMatrix(matrix1,matrix2)
showMatrix(matrix3)"""