# not sure this is correct

class Solution(object):
    def levelOrder(self, root):
      
        res = []
        self.dfs(root, 0, res)
        return reverse.res

    def dfs(self, root, level, res):
        if root:
            if len(res) < level + 1:
                res.insert(0, [])
            res[-(level+1)].append(root.val)
            self.dfs(root.left, level+1, res)
            self.dfs(root.right, level+1, res)