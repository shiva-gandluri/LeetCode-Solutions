class Solution:
    def minDeletions(self, s: str) -> int:
        count = 0
        freq = list(dict(Counter(s)).values())   
        freq_set = set() 
        
        for element in freq: 
            while element in freq_set:
                element -= 1 
                count += 1 
            if element != 0:
                freq_set.add(element)
        
        return count  
