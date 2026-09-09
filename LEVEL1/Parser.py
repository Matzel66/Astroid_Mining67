with open("Files/level1_0_example.in", "r") as f:
    data1 = [line.strip().split() for line in f if line.strip()]
    data2 = data1[1:]

print(data2)