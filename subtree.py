# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root, subRoot) -> bool:
        # write a recursive function to do this -- and do dfs
        if self.checker(root, subRoot) == True:
            return True
        else:
            return False
            
                
    # define the recursive function
    def checker(self, root, subRoot):
        while root.left != None and root.right != None:
            if root.left.val == subRoot.val:
                # search if left and right are same
                if root.left.left == subRoot.left and root.left.right == subRoot.right:
                    return True
                else:
                    continue

            if root.right.val == subRoot.val:
                if root.right.left == subRoot.left and root.right.right == subRoot.right:
                    return True
                else:
                    return False
            
            checker(root.left, subRoot)
            checker(root.right, subRoot)

root = [3,4,5,1,2,None,None,None,None,0]
subRoot = [4,1,2]

sol = Solution()
sol.isSubtree(root, subRoot)