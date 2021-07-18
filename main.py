

import sys
from check_complete import *
from select_variable import *
from value_ordering import *
from forward_checking import *


def backtrack(A, domains, n):

    if(check_complete(A, n)):
        return A.copy()

    X = select_variable(A, domains, n)  # MRV
    D = value_ordering(A, domains, X, n)  # LCV

    for vd in D:

        v = vd[0]
        new_domains = vd[1]

        for Y in new_domains.keys():
            if len(new_domains[Y]) == 0:
                return "failure"

        A[X] = v
        result = backtrack(A, new_domains, n)
        A.pop(X, None)

        if result != "failure":
            return result

    return "failure"


print(sys.getrecursionlimit())
sys.setrecursionlimit(1000000000)

print(
    backtrack(
        {}, {
            0: [0, 1], 1: [0, 1], 2: [0, 1],
            3: [0, 1], 4: [0, 1], 5: [0, 1],
            6: [0, 1], 7: [0, 1], 8: [0, 1],
        }, 3)
)
