

def shiftStrings(strng, left, right):

    if len(strng) < 2:
        return strng

    if len(strng) <= left:
        left = len(strng) % left

    if len(strng) <= right:
        right = len(strng) % right

    for move in range(right):
        strng = strng[1:] + strng[0]

    for move in range(left):
        strng = strng[len(strng)-1] + strng[:len(strng)-1]

    return strng


if __name__ == '__main__':
    s = "memes"
    s3 = "memes"
    s2 = "memes"

    print(shiftStrings(s, 2, 3))