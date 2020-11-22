# delete a node from BST, given the key and return the updated key in its place.

class Solution:
    def delNode(self, root, tar):
        if root is None:
            return root
            # initialize basic items
        parent = None
        node = root

        # traverse the tree
        while node and node.val != tar:
            # record the parent for later
            parent = node

            # traverse
            if tar < node.val:
                node = node.left
            else:
                node = node.right
            # If node is none after traversal then target doesn't exist in the tree
            if node is None:
                return root

        # if it has no children just remove it
        if node.left is None and node.right is None:
            if node == root:
                return None
            else:
                if parent.left == node:
                    parent.left = None
                else:
                    parent.right = None

        # if it has a right child swap with successor
        elif node.right is not None:
            # find successor
            suc = node.right
            while suc.left:
                suc = suc.left
            val = suc.val
            # recursively delete the successor
            node.right = self.delNode(node.right, val)
            # swap values
            node.val = val

        # if only left child, swap with predecessor
        else:
            # find predecessor
            pre = node.left
            while pre.right:
                pre = pre.right
            val = pre.val
            # recursively delete the successor
            node.left = self.delNode(node.left, val)
            # swap values
            node.val = val

        return root


if __name__ == '__main__':
    tester = Solution()
    ans = tester.delNode([5,3,6,2,4,None,7], 3)
    print(ans)
