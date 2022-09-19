#hola gente. 
#puedes utilizar y modificar el codigo a tu gusto 
#he dejado algunos link de plataformas para que ejecutes el codigo
#espero te sirva... SUERTE
#https://jupyter.org/try-jupyter/retro/notebooks/?path=Untitled.ipynb
#https://jupyter.org/try-jupyter/lab/
#https://py2.codeskulptor.org/

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def reverseNodes(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root == None:
            return
        
        self.reverseNodes(root.left)
        self.reverseNodes(root.right)
        
        hold = root.left
        root.left = root.right
        root.right = hold
        
        return root
    
    def printTree(self, root: Optional[TreeNode]):       
        def getHeight(node):
            if not node: return 0
            return 1 + max(getHeight(node.left), getHeight(node.right))
        
        h = getHeight(root)
        ans = [["" for _ in range(2**h - 1)] for _ in range(h)]
        
        def recur(node, l, r, i):
            if not node or l > r: return
            m = (l + r) // 2
            ans[i][m] = f"{node.val}"
            recur(node.left,l, m-1, i+1)
            recur(node.right,m+1,r, i+1)
        
        recur(root, 0, len(ans[0]), 0)
        return ans
    
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

sol = Solution()
sol.reverseNodes(root)
sol.printTree(root)