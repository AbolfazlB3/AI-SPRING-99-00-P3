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


def check_valid(A, index, n, debug=False):
    X = X_i(index, n)
    Y = Y_i(index, n)
    val = A.get(index)
    if(check3(A, index, n, val, X, Y) == False):
        if debug:
            print("check3")
        return False
    row = check_full_row(A, X, n)
    column = check_full_column(A, Y, n)
    if(row != False):
        for i in range(n):
            if(i != X and row == check_full_row(A, i, n)):
                if debug:
                    print("row eq", i, X)
                    print(row, check_full_row(A, i, n))
                return False
    if(column != False):
        for i in range(n):
            if(i != Y and column == check_full_column(A, i, n)):
                if debug:
                    print("col eq")
                return False
    r = 0
    w = 0
    for i in range(n):
        if(val == A.get(I(X, i, n))):
            r += 1
        if(val == A.get(I(i, Y, n))):
            w += 1
    if(r > n // 2):
        if debug:
            print("rowviol")
        return False
    if(w > n // 2):
        if debug:
            print("colviol")
        return False
    return True

def count(A, L, flag, n):
    r = 0
    w = 0
    if(flag == "R"):
        for i in range(n):
            if(0 == A.get(L + i)):
                r += 1
            if(1 == A.get(L + i)):
                w += 1
    else:
        for i in range(n):
            if(0 == A.get(L + i*n)):
                r += 1
            if(1 == A.get(L + i*n)):
                w += 1
    return (r <= n * 0.5 and w <= n * 0.5)

def check2(A, X1, Y1, index1, X2, Y2, index2, flag, val, n):
    if(flag == "R"):
        if(abs(Y2 - Y1) == 2):
            if(val == A.get((index1+index2)/2)):
                return False
        if(abs(Y2 - Y1) == 1):
            Y0 = min(Y1, Y2) - 1
            Y3 = max(Y1, Y2) + 1
            if(Y0 > -1):
                if(A.get(I(X1, Y0, n)) == val):
                    return False
            if(Y3 < n):
                if(A.get(I(X1, Y3, n)) == val):
                    return False
    if(flag == "L"):
        if(abs(X2 - X1) == 2):
            if(val == A.get((index1+index2)/2)):
                return False
        if(abs(X2 - X1) == 1):
            X0 = min(X1, X2) - 1
            X3 = max(X1, X2) + 1
            if(X0 > -1):
                if(A.get(I(X0, Y1, n)) == val):
                    return False
            if(X3 < n):
                if(A.get(I(X3, Y2, n)) == val):
                    return False
    return True

def check_valid2(A, index1, index2, n, debug=False):
    X1 = X_i(index1, n)
    Y1 = Y_i(index1, n)
    val1 = A.get(index1)
    X2 = X_i(index2, n)
    Y2 = Y_i(index2, n)
    val2 = A.get(index2)
    C1 = check_full_column(A, Y1, n)
    C2 = check_full_column(A, Y2, n)
    R1 = check_full_row(A, X1, n)
    R2 = check_full_row(A, X2, n)
    if(X1 != X2 and Y1 != Y2):
        if(C1 == C2 and C1 != False):
            return False
        if(R1 == R2 and R1 != False):
            return False
    if(X1 == X2 and Y1 != Y2):
        if(C1 == C2 and C1 != False):
            return False
        if(count(A, X2, "R", n) == False):
            return False
        if(val1 == val2):
            if(check2(A, X1, Y1, index1, X2, Y2, index2, "R", val1, n) == False):
                return False
    if(X1 != X2 and Y1 == Y2):
        if(R1 == R2 and R1 != False):
            return False
        if(count(A, Y2, "L", n) == False):
            return False
        if(val1 == val2):
            if(check2(A, X1, Y1, index1, X2, Y2, index2, "L", val1, n) == False):
                return False
    return True
