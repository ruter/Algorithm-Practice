#-*- coding: UTF-8 -*-

"""
LeetCode 226. Invert Binary Tree
Link: https://leetcode.com/problems/invert-binary-tree/
Recursive version
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        if root == None:
            return
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
