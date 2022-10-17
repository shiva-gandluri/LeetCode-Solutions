class Solution:
    def list_to_bst(self, mylist, start, end):
        if(end<start):
            return None
        mid = (start+end)//2
        node = TreeNode(mylist[mid],self.list_to_bst(mylist, start, mid-1),self.list_to_bst(mylist, mid+1, end))
        return node
        
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if(head is None):
            return None
        if(head.next is None):
            return TreeNode(head.val)
        mylist = []
        while(head is not None):
            mylist.append(head.val)
            head = head.next
        return self.list_to_bst(mylist,0,len(mylist)-1)
