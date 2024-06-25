# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: optional[TreeNode]) -> bool:
        ''' TAG; got help'''

        def sym(root1, root2):
            
            if not root1 and not root2:
                # No more nodes to check / none of the nodes exist, and return true for symmetry 
                return True

            if not root1 or not root2:
                # caught mismatch; nodeA doesn't exist but nodeB does. 
                return False

            if root1.val != root2.val:
                # caught mismatch; nodeA's value doesnt match nodeB's value. 
                return False
            
            # if none of the above, it will return it self with the next values, as well as spawning a copy of it self with the opposite values.
            return sym(root1.left, root2.right) and sym(root1.right, root2.left)

        return sym(root, root)
