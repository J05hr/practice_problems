
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

# TODO fix the recursive solution

class Solution:

    fDict = dict()
    visited = set()
    route = ""

    def add_route(self, start, des):

        if start in self.fDict:
            self.fDict[start].append(des)
        else:
            self.fDict.setdefault(start, [des])

    def print_all_routes(self, start, des):
        if start in self.fDict:

            if start not in self.visited:
                self.visited.add(start)
                self.route += start

                if start == des:
                    print(str(self.route))
                    self.visited = set()
                else:
                    for s in self.fDict[start]:
                        self.print_all_routes(s, des)

    def print_all_routes2(self, start, des):
        stack = list()
        route = str(start)

        stack.append(start)

        while len(stack):

            curStart = stack[-1]
            stack.pop(-1)

            if curStart not in route:
                route += curStart

            if curStart == des:
                print(route)
                route = ""

            else:
                for aPort in self.fDict[start]:
                    stack.append(aPort)




if __name__ == '__main__':
    tester = Solution()
    tester.add_route('a', 'b')
    tester.add_route('a', 'c')
    tester.add_route('b', 'a')
    tester.add_route('b', 'c')
    tester.add_route('c', 'a')
    tester.add_route('c', 'b')
    print(tester.print_all_routes2('a', 'c'))
