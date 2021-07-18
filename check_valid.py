def X_i(index, n):
    return index // n

def Y_i(index, n):
    return index % n

def I(x, y, n):
    return x * n + y

def check3(A, index, n, val, X, Y):
    tmp = (A.get(I(X - 2, Y, n)), A.get(I(X - 1, Y, n)), val, A.get(I(X + 1, Y, n)), A.get(I(X + 2, Y, n)))
    if(tmp[0] == tmp[2] and tmp[1] == tmp[2]):
        return False
    if(tmp[3] == tmp[2] and tmp[1] == tmp[2]):
        return False
    if(tmp[3] == tmp[2] and tmp[4] == tmp[2]):
        return False
    tmp = (A.get(I(X , Y - 2, n)), A.get(I(X , Y - 1, n)), val, A.get(I(X , Y + 1, n)), A.get(I(X, Y + 2, n)))
    if(tmp[0] == tmp[2] and tmp[1] == tmp[2]):
        return False
    if(tmp[3] == tmp[2] and tmp[1] == tmp[2]):
        return False
    if(tmp[3] == tmp[2] and tmp[4] == tmp[2]):
        return False
    return True

def check_full_row(A, index, n):
    row = []
    for i in range(n):
        tmp = A.get(X_i(index), i, n)
        if(tmp == None):
            return False
        row.append(tmp)
    return row

def check_full_column(A, index, n):
    column = []
    for i in range(n):
        tmp = A.get(i, Y_i(index), n)
        if(tmp == None):
            return False
        column.append(tmp)
    return column

def check_valid(A, index, n):
    X = X_i(index, n)
    Y = Y_i(index, n)
    val = A.get(index)
    if(check3(A, index, n, val, X, Y) == False):
        return False
    row = check_full_row(A, index, n)
    column = check_full_column(A, index, n)
    if(row != False):
        for i in range(n):
            if(row == check_full_row(A, i, n)):
                return False
    if(row != False):
        for i in range(n):
            if(column == check_full_column(A, i, n)):
                return False
    return True