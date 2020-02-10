def importTxt(txt):
    with open(txt, "r") as a:
        list = []
        for line in a:
            elems = line.strip('\n').split('\t')
            list.append(elems)
    return list


natixis = importTxt("natixis stock.txt")
print(natixis[6][1])