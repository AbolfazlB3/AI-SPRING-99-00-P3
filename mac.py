

from typing import Deque
from check_valid import check_valid2


def mac(A, domains, Z, zv, n):
    m = n*n
    A = A.copy()
    domains = domains.copy()
    mark = [False] * m
    for Y in A.keys():
        mark[Y] = True

    q = Deque()
    domains[Z] = [zv]
    A[Z] = zv

    pair_mark = {}

    for W in range(n*n):
        if(mark[W] == False and W != Z):
            q.append((Z, W))
            pair_mark[Z*m+W] = True

    while len(q) > 0:

        X, Y = q.popleft()

        A[X] = domains[X][0]

        domain = []

        for v in domains.get(Y):
            A[Y] = v
            valid = check_valid2(A, X, Y, n)
            if valid:
                domain.append(v)
            A.pop(Y, None)

        if len(domain) == 0:
            return False

        if len(domain) == 1:
            A[Y] = domain[0]
            if len(domains[Y]) > 1:
                for W in range(n*n):
                    if(mark[W] == False and W != Y and W != X and pair_mark.get(Y*m+W) == None):
                        q.append((Y, W))
                        pair_mark[Y*m+W] = True

        domains[Y] = domain

        A.pop(X, None)
        pair_mark.pop(X*m+Y, None)

    return domains
