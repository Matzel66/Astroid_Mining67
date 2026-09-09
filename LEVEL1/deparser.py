l = []

def makefile(l):
    with open("Out/level1_1_small.out", "w") as f:
        f.write(str(len(l)) + "\n")
        for values in l:
            f.write(str(values[0]) + " " + str(values[1]) + "\n")