def X_i(index, n):
    return index // n


def Y_i(index, n):
    return index % n


def I(x, y, n):
    return x * n + y


def check3(A, index, n, val, X, Y):
    tmp = (A.get(I(X - 2, Y, n)), A.get(I(X - 1, Y, n)),
           val, A.get(I(X + 1, Y, n)), A.get(I(X + 2, Y, n)))
    if(tmp[0] == tmp[2] and tmp[1] == tmp[2] and X - 2 > -1):
        return False
    if(tmp[3] == tmp[2] and tmp[1] == tmp[2] and X - 1 > - 1 and X + 1 < n):
        return False
    if(tmp[3] == tmp[2] and tmp[4] == tmp[2] and X + 2 < n):
        return False
    tmp = (A.get(I(X, Y - 2, n)), A.get(I(X, Y - 1, n)),
           val, A.get(I(X, Y + 1, n)), A.get(I(X, Y + 2, n)))
    if(tmp[0] == tmp[2] and tmp[1] == tmp[2] and Y - 2 > -1):
        return False
    if(tmp[3] == tmp[2] and tmp[1] == tmp[2] and Y - 1 > - 1 and Y + 1 < n):
        return False
    if(tmp[3] == tmp[2] and tmp[4] == tmp[2] and Y + 2 < n):
        return False
    return True


def check_full_row(A, rowind, n):
    row = []
    for i in range(n):
        tmp = A.get(I(rowind, i, n))
        if(tmp == None):
            return False
        row.append(tmp)
    return row


def check_full_column(A, colind, n):
    column = []
    for i in range(n):
        tmp = A.get(I(i, colind, n))
        if(tmp == None):
            return False
        column.append(tmp)
    return column


def check_valid(A, index, n):
    X = X_i(index, n)
    Y = Y_i(index, n)
    val = A.get(index)
    if(check3(A, index, n, val, X, Y) == False):
        # print("check3")
        return False
    row = check_full_row(A, index, n)
    column = check_full_column(A, index, n)
    if(row != False):
        for i in range(n):
            if(i != X and row == check_full_row(A, i, n)):
                #print("row eq", i, X)
                #print(row, check_full_row(A, i, n))
                return False
    if(column != False):
        for i in range(n):
            if(i != Y and column == check_full_column(A, i, n)):
                #print("col eq")
                return False
    r = 0
    w = 0
    for i in range(n):
        if(val == A.get(I(X, i, n))):
            r += 1
        if(val == A.get(I(i, Y, n))):
            w += 1
    if(r > n // 2):
        # print("rowviol")
        return False
    if(w > n // 2):
        # print("colviol")
        return False
    return True
