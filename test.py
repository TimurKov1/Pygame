for i in range(1, 10000000):
    if sum(list(map(lambda x: int(x) ** len(str(i)), list(str(i))))) == i:
        print(i)