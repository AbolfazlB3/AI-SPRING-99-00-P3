from forward_checking import forward_checking


def value_ordering(A, domains, X, n, debug=False):
    res = []
    for v in domains.get(X):
        A[X] = v
        new_domains = forward_checking(A, domains, n, debug)
        res.append((v, new_domains))
        A.pop(X, None)
    res = sorted(res, key=lambda x: -sum([len(x[1][y]) for y in x[1].keys()]))
    return res
