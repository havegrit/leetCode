class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        maxDepth = 0
        currDepth = 0
        isLeftNode = False
        prevNode = initRoot = root
        while root:
            currDepth = currDepth + 1
            if currDepth > maxDepth:
                maxDepth = currDepth
            if root.left != None:
                isLeftNode = True
                tempNode = root.left
                prevNode = root
                root = tempNode
            elif root.right != None:
                isLeftNode = False
                tempNode = root.right
                prevNode = root
                root = tempNode
            else:
                
                if isLeftNode:
                    prevNode.left = None
                else:
                    prevNode.right = None
                if root == initRoot:
                    break
                root = initRoot
                currDepth = 0

        return maxDepth