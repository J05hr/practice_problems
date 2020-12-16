class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """

        # approach - format the ints into binary strings, skip over proper 1 bytes, if its 2-4 bytes make sure all the continuations are there

        # assumptions -  1 to 4 bytes long, bytes have to be ordered with continuations following


        # helper to check for correct continuations
        def checkCont(bData, n, idx):
            # check rational size first
            if len(bData) > n:
                bd = bData[idx+1:]
            else:
                return False
            # check for proper cont.
            for idx in range(n):
                if not bd[idx][0:2] == "10":
                    return False
            return True

        # helper to convert the int list to a list of binary strings
        def convetToBinary(data):
            newData = list()
            for item in data:
                newItew = bin(item)[2:].zfill(8)
                newData.append(newItew)

            print(newData)
            return newData



        bData = convetToBinary(data)
        idx = 0
        while idx < len(bData):
            # if there is a 1 at the beginning we will need to consider trailing
            if bData[idx][0:1] == "1":
                # invalid to start with 10, only valid as a continuation
                if bData[idx][0:2] == "10":
                    return False
                # 2 byte start
                elif bData[idx][0:3] == "110":
                    # check for 1 continuation
                    if not checkCont(bData, 1, idx):
                        return False
                    idx+=1

                # 3 byte start
                elif bData[idx][0:4] == "1110":
                    # check for 2 continuations
                    if not checkCont(bData, 2, idx):
                        return False
                    idx += 2

                # 4 byte start
                elif bData[idx][0:5] == "11110":
                    # check for 3 continuations
                    if not checkCont(bData, 3, idx):
                        return False
                    idx += 3

                # anything else invalid
                else:
                    return False

            # else its a 1 byte sting on its own its valid, continue
            idx += 1
        # at the end if we passed everything we can return true
        return True




test = [197, 130, 1]
test2 = [235, 140, 4]
test3 = [115,100,102,231,154,132,13,10]
sol = Solution()
print(sol.validUtf8(test3))