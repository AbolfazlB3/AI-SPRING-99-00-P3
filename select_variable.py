
def select_variable(A, domains, n):

    minimum = 3
    index = -1
    for d in domains.keys():
        if(A.get(d) == None):
            tmp = len(domains.get(d))
            if(tmp < minimum):
                minimum = tmp
                index = d

    return index
