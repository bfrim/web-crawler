#Multiplies Matrix by another matrix
#Note: A matrix with one row should be defined as [[1,2,3]] not [1,2,3]
#Note 2: Matrix multiplication only works if a-columns = b-columns; there is no error-checking
def mult_matrix(a,b):
    result = []
    #Pick row we are multiplying
    for i in range(len(a)):
        matrix_row = []
        #All rows in a matrix should be the same so we will pick the first one to loop through different columns
        for j in range(len(b[0])):
            matrix_element = 0
            #Because there should be the same colums and rows we cycle through a's row and multiply as we keep going down the rows.
            for k in range(len(a[i])):
                matrix_element += a[i][k]*b[k][j]
            #append results
            matrix_row.append(matrix_element)
        result.append(matrix_row)
    return result

#Calcualtes Euclidean Distance of vectors (ex. [[1,2,3]])
def euclidean_dist(a,b):
    result = 0
    
    #There should not be more than 1 list in the vectors and they should be equal so acess a and apply the formula steps
    for i in range(len(a[0])):
        result += (a[0][i]-b[0][i])**2
    
    return result**0.5
