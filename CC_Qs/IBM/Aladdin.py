
def aladdin(stops, dists):
    # basic checks
    if len(stops) != len(dists):
        return -1

    # loop through the stops
    for idx in range(len(stops)):

        stopidx = len(stops)-1
        if idx != 0:
            stopidx = idx-1

        curMagic = 0
        curidx = idx
        failed = False
        # check if we can take the path by walking the steps
        while curidx != stopidx:
            curMagic += stops[curidx]
            if curMagic - dists[curidx] < 0:
                failed = True
                break
            else:
                curMagic -= dists[curidx]
                # loop if at the end
                if curidx+1 >= len(stops):
                    curidx = 0
                else:
                    curidx += 1

        if not failed:
            return idx

    return -1

if __name__ == '__main__':
    a = [2, 4, 5, 2]
    b = [4, 3, 1, 3]
    print(aladdin(a, b))