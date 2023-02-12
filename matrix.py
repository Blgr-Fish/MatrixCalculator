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

# Create an identity matrix filled with 1 in the diagonal, else 0.
def createIdentityMatrix():
    matrix = []
    lines = input("How many Lines ? :") # str
    columns = input("How many Columns ? :") # str
    for i in range(int(lines)):
            matrix.append([])
            for j in range(int(columns)):
                matrix[i].append(int(i==j))
    return matrix

# Create a matrix with random values baed on the lines and columns given by the user
def createRandomMatrix():
    lines = input("How many Lines ? :") # str
    columns = input("How many Columns ? :") # str 
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
    
# Create a line permuted matrix two lines of a given matrix and its two lines and product it with the given matrix
def createLinePermutationMatrix(line1,line2,matrix):
    permutedMatrix = createIdentityMatrixWithParameters(numberOfLines(matrix),numberOfColumns(matrix))
    permutedMatrix[line1-1], permutedMatrix[line2-1] = permutedMatrix[line2-1], permutedMatrix[line1-1]

    return productMatrix(permutedMatrix,matrix)

# Create a column permuted matrix two lines of a given matrix and its two lines and product it with the given matrix
def createColumnPermutationMatrix(line1,line2,matrix):
    permutedMatrix = createIdentityMatrixWithParameters(numberOfLines(matrix),numberOfColumns(matrix))
    permutedMatrix[line1-1], permutedMatrix[line2-1] = permutedMatrix[line2-1], permutedMatrix[line1-1]

    return productMatrix(matrix,permutedMatrix)

# Sum 2 matrixes to make a third one
def addMatrix(matrix1,matrix2):
    matrix = []
    if numberOfColumns(matrix1) == numberOfColumns(matrix2):
        if numberOfLines(matrix1) == numberOfLines(matrix2):
            
            matrix = createEmptyMatrixWithParameters(numberOfLines(matrix1),numberOfColumns(matrix1))
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

selectMatrix = int(input("Menu:\n1.Create your own matrix\n2.Create a random matrix\n3.Create an Identity matrix\nValue : "))
matrix = []
if selectMatrix == 1 : 
    matrix = createMatrix()
elif selectMatrix == 2 :
    matrix = createRandomMatrix()
else :
    matrix = createIdentityMatrix()

showMatrix(matrix)
print()

operationMatrix = int(input("Operation:\n1.Sum a matrix\n2.Product a matrix\n3.Permute a matrix\n4.Transpose a matrix\nValue : "))
secondMatrix = []
resultMatrix = []
if operationMatrix == 1 :
    selectMatrix = int(input("Menu:\n1.Create your second own matrix\n2.Create a second random matrix\n3.Create a second Identity matrix\nValue : "))
    if selectMatrix == 1 : 
        secondMatrix = createMatrix()
    elif selectMatrix == 2 :
        secondMatrix = createRandomMatrix()
    else :
        secondMatrix = createIdentityMatrix()
    resultMatrix = addMatrix(matrix,secondMatrix)
elif operationMatrix == 2 :
    selectMatrix = int(input("Menu:\n1.Create your second own matrix\n2.Create a second random matrix\n3.Create a second Identity matrix\nValue : "))
    if selectMatrix == 1 : 
        secondMatrix = createMatrix()
    elif selectMatrix == 2 :
        secondMatrix = createRandomMatrix()
    else :
        secondMatrix = createIdentityMatrix()
    resultMatrix = productMatrix(matrix,secondMatrix)
elif operationMatrix == 3 :
    selectMatrix = int(input("Menu:\n1.Line permuntation\n2.Column permutation\nValue : "))
    

    if selectMatrix == 1 :
        permute1 = int(input("Select the line to permute : "))
        permute2 = int(input("Select the second line to permute : "))
        resultMatrix = createLinePermutationMatrix(permute1,permute2,matrix)

    else :
        permute1 = int(input("Select the column to permute : "))
        permute2 = int(input("Select the second column to permute : "))
        resultMatrix = createColumnPermutationMatrix(permute1,permute2,matrix)

else :

    resultMatrix = createTransposeMatrix(matrix)

showMatrix(resultMatrix)

    
    


    




