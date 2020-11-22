



def memes(inrange, factworddict):

    if inrange == 0 or len(factworddict) == 0:
        print("improper input, try again")
        return

    for idx in inrange:
        outword = ""
        for factword in factworddict:
            if idx % factword == 0:
                outword += factworddict[factword]
        if outword != "":
            print(outword)
        else:
            print(idx)


if __name__ == '__main__':
    therange = range(-10, 500)
    factwords = {3: "fizz", 5: "buzz"}
    memes(therange, factwords)








