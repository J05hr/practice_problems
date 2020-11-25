
'''
Given the following flight routes, print all possible routes between the airports C and D

  A ----> B
  B ----> A
  A ----> C
  C ----> A
  A ----> D
  D ----> A
  B ----> C
  C ----> B
  B ----> D
  D ----> B

  Expected output:

  C,A,B,D,
  C,A,D,
  C,B,A,D,
  C,B,D,

Implement a class called AirMap that has two methods:

1- add_route(start, destination)
    - adds a ONE WAY connecting flight from start to destination

2- print_all_routes(start, destination)
    - prints all possible routes from start to destination irrespective of hops
'''


class Solution:

    fDict = dict()
    currentRoute = list()
    vDict = set()
    stack = list()

    def add_route(self, start, des):

        if start in self.fDict:
            self.fDict[start].append(des)
        else:
            self.fDict.setdefault(start, [des])

    def print_all_routes(self, start, des):
        if start not in self.vDict:
            self.vDict.add(start)
            if start in self.fDict:
                self.currentRoute.append(start)
                for item in self.fDict[start]:
                    self.stack.append(item)

            while len(self.stack) > 0:
                curStart = self.stack[-1]
                self.stack.pop(-1)
                if curStart == des:
                    self.currentRoute.append(curStart)
                    print(str(self.currentRoute))
                    self.currentRoute = list()
                else:
                    self.print_all_routes(curStart, des)



if __name__ == '__main__':
    tester = Solution()
    tester.add_route('a', 'b')
    tester.add_route('a', 'c')
    tester.add_route('b', 'a')
    tester.add_route('b', 'c')
    tester.add_route('c', 'a')
    tester.add_route('c', 'b')
    print(tester.print_all_routes('a', 'c'))
