"""
H-Tree Construction

An H-tree is a geometric shape that consists of a repeating pattern resembles the letter “H”.

It can be constructed by starting with a line segment of arbitrary length, drawing two segments of the same length at right angles to the first through its endpoints, and continuing in the same vein, reducing (dividing) the length of the line segments drawn at each stage by √2.

Here are some examples of H-trees at different levels of depth:

alt depth = 1

alt depth = 2

alt depth = 3

Write a function drawHTree that constructs an H-tree, given its center (x and y coordinates), a starting length, and depth. Assume that the starting line is parallel to the X-axis.

Use the function drawLine provided to implement your algorithm. In a production code, a drawLine function would render a real line between two points. However, this is not a real production environment, so to make things easier, implement drawLine such that it simply prints its arguments (the print format is left to your discretion).

Analyze the time and space complexity of your algorithm. In your analysis, assume that drawLine's time and space complexities are constant, i.e. O(1).

Constraints:

    [time limit] 5000ms

    [input] double x

    [input] double y

    [input] double length

    [input] double depth
        0 ≤ depth ≤ 10

"""
import math


class Solution:
    drawing = []

    def draw_htree(self, x, y, length, depth):

        node1 = (x - length / 2, y + length / 2, length / math.sqrt(2))  # (x,y,length)
        node2 = (x - length / 2, y - length / 2, length / math.sqrt(2))
        node3 = (x + length / 2, y + length / 2, length / math.sqrt(2))
        node4 = (x + length / 2, y - length / 2, length / math.sqrt(2))
        nodes = [node1, node2, node3, node4]

        self.drawing.append(self.draw_line(x - length / 2, y, x - length / 2, y))
        self.drawing.append(self.draw_line(x - length / 2, y - length / 2, x - length / 2, y + length / 2))
        self.drawing.append(self.draw_line(x + length / 2, y - length / 2, x + length / 2, y + length / 2))

        if depth != 1:
            for node in nodes:
                self.draw_htree(node[0], node[1], node[2], depth - 1)

    def draw_line(self, x1, y1, x2, y2):
        return (x1, y1), (x2, y2)




if __name__ == '__main__':
    tester = Solution()
    ans = tester.draw_htree(1, 1)
    print(ans)
