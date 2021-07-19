from os import walk
import os


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
    text = text.split("\n")
    Map = []
    for i in range(1, len(text)):
        Map.append(text[i].split(" "))
    return Map, len(Map)


def print_map(Map):
    for i in range(len(Map)):
        for j in range(len(Map[i])):
            print(Map[i][j], end=" ")
        print()


def extract_dics(Map, n):
    A = {}
    domains = {}
    for i in range(n):
        for j in range(n):
            if(Map[i][j] != "-"):
                A[i*n + j] = int(Map[i][j])
            else:
                domains[i*n + j] = [1, 2]
    return A, domains


def do():
    l = read()
    L = []
    for i in l:
        m, n = extract_map(i[1])
        A, domains = extract_dics(m, n)
        L.append((i[0], m, A, domains, n))
    return L


def print_level(level, solved_level, t):
    print(level[0])
    print("n:", level[4])
    print("unsolved "+level[0]+":")
    print_map(level[1])
    print("A:")
    print(level[2])
    print("domains:")
    print(level[3])
    if(solved_level != None):
        print("unsolved "+level[0]+":")
        print_map(solved_level)
    if(t != None):
        print("time(ms):", t)
    print("##############################")


L = do()
l = L[0]
print_level(l, None, None)
