# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 15:07:03 2020

@author: WELCOME
"""

from collections import deque
class binaryTree:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
class Solution:
    def isValidBST(self, root):
        if not root:
            return True
        queue=deque()
        queue.append([root,[float('-inf'),float('inf')]])
        while(queue):
            size=len(queue)
            for i in range(size):
                currentNode=queue.popleft()
                if currentNode[0].val>=currentNode[1][1] or currentNode[0].val<=currentNode[1][0]:
                    return False
                if currentNode[0].left:
                    queue.append([currentNode[0].left,[currentNode[1][0],currentNode[0].val]])
                if currentNode[0].right:
                    queue.append([currentNode[0].right,[currentNode[0].val,currentNode[1][1]]])
                    
                    
                    
        return True

treeNode=binaryTree(6)
treeNode.left=binaryTree(4)
treeNode.right=binaryTree(8)
treeNode.left.left=binaryTree(1)
print(Solution().isValidBST(treeNode))