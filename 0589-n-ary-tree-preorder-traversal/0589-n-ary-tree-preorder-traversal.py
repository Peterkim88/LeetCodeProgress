"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        if not root: return []
        
        q = deque([root])
        res = []
        
        while q:
            curr = q.popleft()
            res.append(curr.val)
            for c in reversed(curr.children):
                q.appendleft(c)
                
        return res
        
#         res = []
        
#         def dfs(node):
#             if not node: return
#             res.append(node.val)
            
#             for c in node.children:
#                 dfs(c)
            
#         dfs(root)
        
#         return res        