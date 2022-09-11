class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        power = 0
        decimalVal = 0
        temp = head
        
        while(temp):
            temp = temp.next
            power += 1
        power -= 1
        
        temp = head
        while(temp):
            decimalVal += (temp.val * 2 ** power)
            power -= 1
            temp = temp.next
        
        return decimalVal    
