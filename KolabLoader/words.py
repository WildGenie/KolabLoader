with open('words.txt') as fh:
    fh2 = open("out.txt", "w")
    for line in fh:
        # in python 2
        # print line
        # in python 3
        if(len(line) > 6 and len(line) < 12):
            fh2.write(line)

fh2.close()