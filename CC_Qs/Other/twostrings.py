
def twostrings(a, b):

    # loop through the lists
    for idx in range(len(a)):
        charlist1 = sorted(a[idx])
        charlist2 = sorted(b[idx])
        found = -1

        # loop through the chars in string 1 and try to find them in string 2
        for charidx in range(len(charlist1)):
            # skip a search if it doesnt make sense
            if charlist2[0] <= charlist1[charidx] <= charlist2[len(charlist1) - 1]:
                try:
                    found = charlist2.index(charlist1[charidx])
                    break
                except ValueError:
                    pass

        if found != -1:
            print("YES")
        else:
            print("NO")


if __name__ == '__main__':
    a = ['ac', 'cd', 'ef']
    b = ["af", "ee", "ef"]
    twostrings(a, b)