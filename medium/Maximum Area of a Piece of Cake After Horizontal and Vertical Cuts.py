class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.extend([0,h])
        horizontalCuts.sort()
        verticalCuts.extend([0,w])
        verticalCuts.sort()
        
        max_h, max_w = 0, 0
        
        for i in range(1, len(horizontalCuts)):
            max_h = max(max_h, horizontalCuts[i] - horizontalCuts[i-1])
        
        for i in range(1, len(verticalCuts)):
            max_w = max(max_w, verticalCuts[i] - verticalCuts[i-1])
            
        return max_h * max_w % (1000000007)
