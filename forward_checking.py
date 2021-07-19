from check_valid import check_valid


def forward_checking(A, domains, n, debug=False):

    res = {}

    mark = [False] * (n*n)

    for X in A.keys():
        mark[X] = True

    for X in domains.keys():

        if mark[X]:
            res[X] = [A[X]]
            continue

        domain = []

        for v in domains[X]:

            A[X] = v
            valid = check_valid(A, X, n, debug)
            if valid:
                domain.append(v)
            if debug and not valid:
                print("forward checking: ", X, valid)
            A.pop(X, None)

        res[X] = domain

    return res
