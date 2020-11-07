def zeroOne(mat):
    position = []
    for i in range(0, len(mat)):  # 3
        for j in range(0, len(mat[0])):  # 4
            if mat[i][j] == 1:
                position += [i,j]

    print(position)
    for i in range(0, len(position)-1,2):
        print(position[i])
        print(position[i+1])
        for k in range(0, len(mat)):
            mat[k][position[i+1]] = 1
        for k in range(0, len(mat[0])):
            mat[position[i]][k] = 1
    return (mat)