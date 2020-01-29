# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 15:07:03 2020

@author: WELCOME
"""
"""
DFS Solution
Working on Leetcode
Time complexity= O(N)
Spece Complexity = O(H) where H is the height of the tree
"""

class binaryTree:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
class Solution:
    def isValidBST(self, root):
        minimumValue=float('-inf')
        maximumValue=float('inf')
        def isValid(root,minimumValue,maximumValue):
            #Base
            if root==None:
                return True
            if root.val>=maximumValue or root.val<=minimumValue:
                return False
            
            
            #Logic
            case1=isValid(root.left,minimumValue,root.val)
            case2=isValid(root.right,root.val,maximumValue)
            return case1 and case2
                                  
        return isValid(root,minimumValue,maximumValue)

treeNode=binaryTree(6)
treeNode.left=binaryTree(4)
treeNode.right=binaryTree(8)
treeNode.left.left=binaryTree(1)
print(Solution().isValidBST(treeNode))