# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        treeNode=str(self.val)
        return treeNode
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        counter=0
        levels = {0:[root]}
        while counter in levels:
            
            for node in levels[counter]:
                if counter+1 not in levels and node.left != None:
                    levels[counter+1] = []
                if node.left != None:
                    levels[counter+1].append(node.left)
                    levels[counter+1].append(node.right)

            #Change the values
            if counter % 2 == 1 and counter in levels:
                for i in range(int(len(levels[counter])/2)):
                    levels[counter][i].val, levels[counter][-i-1].val = levels[counter][-i-1].val, levels[counter][i].val
            counter +=1
        print({i: [node.val for node in k] for i, k in levels.items()})
        return root
solution = Solution()
treeNode = TreeNode(2,TreeNode(3, TreeNode(8, None, None), TreeNode(13, None, None)), TreeNode(5, TreeNode(21, None, None), TreeNode(34, None,None)))#[2,3,5,8,13,21,34]
solution.reverseOddLevels(treeNode)

