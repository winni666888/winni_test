with open (".\\text") as f:
    line=''
    for l in f.readlines():
        l=l.strip('\n')
        line=line+l
    print(line)


for i in  range(2,11):
    print(i)