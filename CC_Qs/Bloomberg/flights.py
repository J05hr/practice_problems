
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

    def add_route(self, start, des):
        if start in self.fDict:
            self.fDict[start].append(des)
        else:
            self.fDict.setdefault(start, [des])

    # recursive approach, we pass the whole route string into "start" and the last char is the next start
    # DFS style traversal, time bigO(nodes+edges), space bigO(nodes) if we have a DS with O(1) lookup
    def print_all_routes(self, start, des):
        cStart = start[-1]

        # stop if airport not in dict
        if start in self.fDict:

            # if we arnt at the goal recurse through all the children
            if cStart not in start[:-1] and cStart != des:
                for child in self.fDict[cStart]:
                    self.print_all_routes(start+child, des)
            # if we hit the goal dest then print
            else:
                print(start)
        else:
            return "airport {} not found".format(start)

    # iterative stack approach, DFS style traversal, time bigO(nodes+edges), space bigO(nodes)
    def print_all_routes2(self, start, des):
        stack = list()
        # stop if airport not in dict
        if start in self.fDict:
            stack.append(start)

            while len(stack):
                cRoute = stack[-1]
                cStart = cRoute[-1]
                stack.pop(-1)

                if cStart != des:
                    for aPort in self.fDict[cStart]:
                        if aPort not in cRoute:
                            stack.append(cRoute + aPort)
                else:
                    print(cRoute)
        else:
            print("airport {} not found".format(start))

if __name__ == '__main__':
    tester = Solution()
    tester.add_route('a', 'b')
    tester.add_route('a', 'c')
    tester.add_route('c', 'b')
    tester.add_route('c', 'a')
    tester.add_route('b', 'c')
    tester.add_route('b', 'a')
    tester.print_all_routes2('a', 'c')
