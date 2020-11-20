import math

def rearrangeWord(word):

    # no answer if just one or no letters
    if len(word) < 2:
        return "no answer"

    # use a list so its mutable
    charlist = list(word)

    # start from the back and find the first chance to increase
    for idx in range(len(charlist)-1, 0, -1):
        if charlist[idx] > charlist[idx-1]:
            # swap the first place to increase with the min larger number in the proceeding subsection and reverse the subsection
            for idx2 in range(idx, len(charlist)):
                if charlist[idx2] <= charlist[idx-1]:
                    # swap
                    temp = charlist[idx-1]
                    charlist[idx-1] = charlist[idx2-1]
                    charlist[idx2 - 1] = temp
                    # reverse
                    startpart = charlist[0:idx]
                    endpart = charlist[idx:]
                    endpart.reverse()
                    startpart.extend(endpart)
                    charlist = startpart
                    return "".join(charlist)
            else:
                return word


if __name__ == '__main__':
    word = 'bcdefa'

    print(rearrangeWord(word))