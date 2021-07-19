
from check_complete import *
from select_variable import *
from value_ordering import *
from forward_checking import *

import sys
from os import walk
import os


cnt = 0


def backtrack(A, domains, n, log=False):
    global cnt
    cnt += 1
    debug = False and log

    if debug:
        print("cnt:", cnt)
        print_state(A, n)
        D = domains.copy()
        for Y in D.keys():
            D[Y] = "-" if A.get(Y) != None else len(D[Y])
        print_state(D, n)
        print()

    if(check_complete(A, n)):
        return A.copy()

    X = select_variable(A, domains, n)  # MRV
    D = value_ordering(A, domains, X, n, debug)  # LCV

    if debug:
        print("backtrack: ", len(D), X, D)
        print(domains[1])

    for vd in D:

        v = vd[0]
        new_domains = vd[1]

        if(debug):
            print("val:", v)
            print(new_domains)
            print()

        ok = True
        for Y in new_domains.keys():
            if len(new_domains[Y]) == 0:
                ok = False
                break
        if ok == False:
            continue

        A[X] = v
        result = backtrack(A, new_domains, n)
        A.pop(X, None)

        if result != "failure":
            return result

    return "failure"


sys.setrecursionlimit(10000000)


def read():
    PATH = "./puzzles/"
    _, _, filenames = next(walk(PATH))

    levels = [
        (
            os.path.basename(level.name).split(".")[0],
            level.read().strip(),
            level.close()
        )[0:2] for level in [open(PATH+name) for name in filenames]
    ]
    return levels


def extract_map(text):
    a = text.split()
    n = int(a[0])
    Map = []
    for i in range(n):
        Map.append([])
        for j in range(n):
            Map[i].append(a[2+i*n+j])
    return Map, n


def print_state(A, n):
    for i in range(n):
        for j in range(n):
            X = i*n+j
            v = A.get(X)
            if v == None:
                v = "-"
            print(v, end=" ")
        print()
    print()


def print_result(res, n):
    if(res == "failure"):
        print(res)
        return
    print_state(res, n)


def extract_dics(Map, n, R):
    A = {}
    D = {}
    for i in range(n):
        for j in range(n):
            v = Map[i][j]
            X = i * n + j
            D[X] = []
            if v == "-":
                D[X] = [x for x in range(R)]
            else:
                v = int(v)
                A[X] = v
                D[X] = [v]
    return A, D


def main(R):

    levels = read()

    for level in levels:
        print(level[0] + ":\n")
        Map, n = extract_map(level[1])
        A, D = extract_dics(Map, n, R)
        print_state(A, n)
        res = backtrack(A, D, n)
        print_result(res, n)
        print()


main(2)

exit()

print(
    backtrack(
        {0: 0, 1: 1, 2: 0, 3: 1}, {
            0: [0], 1: [1], 2: [0], 3: [1],
            4: [0, 1], 5: [0, 1], 6: [0, 1], 7: [0, 1],
            8: [0, 1], 9: [0, 1], 10: [0, 1], 11: [0, 1],
            12: [0, 1], 13: [0, 1], 14: [0, 1], 15: [0, 1]
        }, 4)
)

"""
print("ans",
      backtrack(
          {0: 1, 1: 0, 2: 0}, {
              3: [0, 1]
          }, 2)
      )

print(
    backtrack(
        {}, {
            0: [0, 1], 1: [0, 1],
            2: [0, 1], 3: [0, 1],
        }, 2)
)
"""
