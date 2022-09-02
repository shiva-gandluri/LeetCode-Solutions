class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque([root])
        result = []
        
        while queue:
            size = len(queue) # size = number of nodes at current level
            i, sum_nodes = 0,0  #. sum_nodes = sum of nodes at current level
            while i < size:   
                curr = queue.popleft()
                sum_nodes += curr.val
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                i+=1
            result.append(sum_nodes/size)
        
        return result
