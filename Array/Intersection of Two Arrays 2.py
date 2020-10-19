class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        memes1 = dict()
        memes2 = dict()

        # make dicts for both
        for idx in range(len(nums1)):
            try:
                memes1[nums1[idx]].append(idx)
            except:
                memes1.setdefault(nums1[idx], [idx])

        for idx in range(len(nums2)):
            try:
                memes2[nums2[idx]].append(idx)
            except:
                memes2.setdefault(nums2[idx], [idx])

        if len(memes1) < len(memes2):
            dik = memes1
            odik = memes2
        else:
            dik = memes2
            odik = memes1

        for key in dik:
            for idx in range(len(dik[key])):
                try:
                    idxs = odik[key]
                    if len(idxs) > 0:
                        res.append(key)
                    idxs.pop(0)
                except:
                    pass

        return res

memes = Solution()

a1 = [4, 9, 5]
a2 = [9, 4, 9, 8, 4]

print(memes.intersect(a1, a2))