from mac import mac
from gui import GUI
from check_complete import *
from select_variable import *
from value_ordering import *
from forward_checking import *

import sys
from os import times, walk
import os
import time

cnt = 0


def toFrame(A, n):
    res = []
    for i in range(n):
        row = []
        for j in range(n):
            v = A.get(i*n+j)
            row.append("-" if v == None else str(v))
        res.append(row)
    return res


def backtrack(A, domains, n, frames, log=False):
    global cnt
    cnt += 1
    debug = False and log

    frames.append(toFrame(A, n))

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
        result = backtrack(A, new_domains, n, frames, log)
        A.pop(X, None)

        if result != "failure":
            return result

    return "failure"


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


def backtrack2(A, domains, n, frames, log=False):
    global cnt
    cnt += 1
    debug = False and log

    frames.append(toFrame(A, n))

    if debug:
        print("cnt:", cnt)
        print_state(A, n)
        D = domains.copy()
        for Y in D.keys():
            D[Y] = "-" if A.get(Y) != None else len(D[Y])
        print_state(D, n)
        print()

    if(check_complete(A, n)):
        return A.copy() if check_complete2(A, n) else "failure"

    X = select_variable(A, domains, n)  # MRV
    D = value_ordering(A, domains, X, n, debug)  # LCV

    if debug:
        print("backtrack: ", len(D), X, D)
        print(domains[1])

    for vd in D:

        v = vd[0]
        new_domains = mac(A, domains, X, v, n, debug)

        if new_domains == False:
            continue

        if debug:
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
        result = backtrack2(A, new_domains, n, frames, log)
        A.pop(X, None)

        if result != "failure":
            return result

    return "failure"


def solve_forward_checking(A, D, level, n, log=True):
    t1 = time.time_ns()
    if log:
        print(level[0] + ":\n")
        print_state(A, n)
    frames = []
    res = backtrack(A, D, n, frames)
    if log:
        print_result(res, n)
        print(len(frames))
        print()
        GUI(frames, n, level[0])
    t2 = time.time_ns()
    return len(frames), t2-t1


def solve_mac(A, D, level, n, log=True):
    t1 = time.time_ns()
    if log:
        print(level[0] + ":\n")
        print_state(A, n)
    frames = []
    res = backtrack2(A, D, n, frames)
    if log:
        print_result(res, n)
        print(len(frames))
        print()
        GUI(frames, n, level[0])
    t2 = time.time_ns()
    return len(frames), t2-t1


def main(R):
    sys.setrecursionlimit(100000000)
    levels = read()
    for level in levels:
        Map, n = extract_map(level[1])
        A, D = extract_dics(Map, n, R)
        D = forward_checking(A, D, n)

        n1, t1 = solve_forward_checking(A, D, level, n, False)

        n2, t2 = solve_mac(A, D, level, n, False)

        print(level[0], ":")
        print("Forward Checking:          ", n1, "frames ", t1/1000000, "ms")
        print("Maitaining Arc Consistensy:", n2,
              "frames ", t2/1000000, "ms\n\n")


main(2)
