def parse(file):
    with open(file, "r") as f:
        data1 = [str(line.replace("#", "S", ":").strip().split() for line in f if line.strip())]
        data2 = data1[1:]

    #print(data2)
    return data2