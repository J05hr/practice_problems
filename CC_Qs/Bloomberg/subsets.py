# https://leetcode.com/problems/subsets


class Solution:
    def subsets(self, nums):

        def sub(nums, r):
            if len(r) == 0:
                for num in nums:
                    r.append([num])

            for reIdx in range(len(r)):
                re = r[reIdx]
                sub = list()
                sub.append(re[0])
                for numIdx in range(len(nums)):
                    num = nums[numIdx]
                    if num not in sub:
                        sub.append(num)
                    prev = re.copy()
                    if num not in prev:
                        prev.append(num)
                    if sub != prev:
                        if len(sub) > 1:
                            r.append(sub.copy())
                        if len(prev) > 1:
                            r.append(prev)
                    elif len(prev) > 1:
                        r.append(prev)
            return r

        # results array
        res = list()
        # always add an empty subset
        res.append([])
        # return on empty array or singleton
        if len(nums) == 0:
            return res
        if len(nums) == 1:
            res.append([nums[0]])
            return res

        r = list()
        r = sub(nums, r)
        res.extend(r)
        return res


    # cascading
    # Let's start from empty subset in output list.
    # At each step one takes new integer into consideration and generates new subsets from the existing ones.
    def subsets2(self, nums):
        output = [[]]

        for num in nums:
            output += [curr + [num] for curr in output]

        return output


    def subsets3(self, nums):
        output = [[]]

        for num in nums:
            newSub = list()
            for item in output:
                a = item.copy()
                a.append(num)
                newSub.append(a)
            for item in newSub:
                output.append(item)

        return output


if __name__ == '__main__':
    tester = Solution()
    # ans = tester.subsets([1,2,3])
    ans2 = tester.subsets3([3,2,4,1])
    print(ans2)
