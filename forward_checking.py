from check_valid import check_valid


def forward_checking(A, domains, n):

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
            if(check_valid(A, X, n)):
                domain.append(v)
            A.pop(X, None)

        res[X] = domain

    return res
