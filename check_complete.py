
from check_valid import check_valid


def check_complete(A, n):
    return (len(A.keys()) == n*n)


def check_valid_state(A, n):
    for i in A.keys():
        if(check_valid(A, i, n) == False):
            return False
    return True
