# https://leetcode.com/discuss/interview-question/406663/Bloomberg-or-Phone-Screen-or-Min-Steps-to-Generate-Number

from collections import deque


class Solution:

    def min_steps(self, n):
        q = deque([(1, 0)])
        seen = set()

        while q:
            res, ops = q.popleft()

            if res == n:
                return ops
            if res // 3 not in seen:
                q.append((res // 3, ops + 1))
                seen.add(res // 3)

            if res * 2 not in seen:
                q.append((res * 2, ops + 1))
                seen.add(res * 2)


if __name__ == '__main__':
    tester = Solution()
    ans = tester.min_steps(11)
    print(ans)
