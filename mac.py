

from typing import Deque
from check_valid import check_valid2


def mac(A, domains, Z, zv, n, debug=False):
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

    for W in range(m):
        if(mark[W] == False and W != Z):
            q.append((Z, W))
            pair_mark[Z*m+W] = True
    if debug:
        print("\ninit: ", Z, zv)

    while len(q) > 0:

        X, Y = q.popleft()

        A[X] = domains[X][0]

        old_domain = domains[Y]
        domain = []

        for v in old_domain:
            A[Y] = v
            valid = check_valid2(A, X, Y, n)
            if valid:
                domain.append(v)

            if debug and (X, Y) == (6, 5):
                print("error: ", A)
                pass
            A.pop(Y, None)

        if debug:
            print((X, Y), A[X], " : ", old_domain, domain)

        if len(domain) == 0:
            return False

        if len(domain) == 1:
            A[Y] = domain[0]
            if len(old_domain) > 1:
                colnum = [n] * n
                rownum = [n] * n
                for W in A.keys():
                    colnum[W % n] -= 1
                    rownum[W//n] -= 1
                for W in range(n*n):
                    wi, wj = (W // n, W % n)
                    yi, yj = (Y // n, Y % n)
                    if(mark[W] == False and W != Y and W != X and pair_mark.get(Y*m+W) == None
                            and (wi == yi or wj == yj or (A.get(W) == None and (colnum[wj] == 1 or rownum[wi] == 1)))):
                        q.append((Y, W))
                        pair_mark[Y*m+W] = True

        domains[Y] = domain

        pair_mark.pop(X*m+Y, None)

    return domains
