
from check_valid import check_valid


def check_complete(A, n):
    return (len(A.keys()) == n*n)


def check_complete2(A, n):
    tmp = (len(A.keys()) == n*n)
    for i in range(n*n):
        tmp = tmp and check_valid(A, i, n)
        if tmp == False:
            return False
    return tmp
