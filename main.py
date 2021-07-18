
from check_complete import *
from select_variable import *
from value_ordering import *
from forward_checking import *


def backtrack(A, domains):

    if(check_complete(A)):
        return [(x[0], x[1]) for x in A]

    X = select_variable(A, domains)
    D = value_ordering(A, domains, X)
    A = []

    for vd in D:

        v = vd[0]
        new_domains = vd[1]

        for d in new_domains:
            if len(d[1]) == 0:
                return "failure"

        A.append((X, v))
        result = backtrack(A, new_domains)
        A.pop()

        if result != "failure":
            return result

    return "failure"
